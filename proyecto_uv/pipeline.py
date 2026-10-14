"""Pipeline bronze -> silver -> gold para el dataset de taxis de NYC.

Lee de la carpeta datos/:
    viajes_2024_01.parquet   (viajes)
    zonas.csv                (catalogo de zonas)

Escribe en:
    datos/bronze/            copia fiel de lo que llego
    datos/silver/            datos limpios, con tipos correctos
    datos/gold/              tabla lista para consumo (ingresos por borough)
    datos/quarantine/        registros rechazados, con el motivo
    datos/metricas/          resumen de la ultima corrida (JSON)

Es idempotente: cada corrida reemplaza por completo los archivos de salida,
asi que correrlo dos veces deja exactamente el mismo resultado.

Uso:
    uv run python pipeline.py
    DATOS_DIR=/ruta/a/datos uv run python pipeline.py
"""

import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import duckdb
import pandera.polars as pa
import polars as pl
from pandera.errors import SchemaErrors

log = logging.getLogger("pipeline")

# ---------------------------------------------------------------- configuracion
ARCHIVO_VIAJES = "viajes_2024_01.parquet"
ARCHIVO_ZONAS = "zonas.csv"

# Mes que esperamos en este lote (inicio incluido, fin excluido)
MES_INICIO = datetime(2024, 1, 1)
MES_FIN = datetime(2024, 2, 1)

# Si mas de esta fraccion de filas termina en cuarentena, avisamos fuerte.
# Es un parametro de ejemplo, ajustalo a tu caso.
UMBRAL_CUARENTENA = 0.05

# Solo conservamos las columnas que usamos. Protege contra schema drift.
COLUMNAS = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
    "PULocationID",
    "DOLocationID",
    "payment_type",
    "fare_amount",
    "tip_amount",
    "total_amount",
]

# Columnas que no pueden venir vacias para que un viaje sea util
CLAVES = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "trip_distance",
    "total_amount",
]

# Contrato de la capa silver (Pandera, backend polars)
SCHEMA_SILVER = pa.DataFrameSchema(
    {
        "tpep_pickup_datetime": pa.Column(pl.Datetime, nullable=False),
        "tpep_dropoff_datetime": pa.Column(pl.Datetime, nullable=False),
        "passenger_count": pa.Column(pl.Int64, nullable=True),
        "trip_distance": pa.Column(pl.Float64, pa.Check.gt(0), nullable=False),
        "PULocationID": pa.Column(pl.Int32, pa.Check.in_range(1, 265), nullable=False),
        "DOLocationID": pa.Column(pl.Int32, pa.Check.in_range(1, 265), nullable=False),
        "payment_type": pa.Column(pl.Int64, nullable=True),
        "fare_amount": pa.Column(pl.Float64, nullable=True),
        "tip_amount": pa.Column(pl.Float64, nullable=True),
        "total_amount": pa.Column(pl.Float64, pa.Check.ge(0), nullable=False),
        "viaje_id": pa.Column(pl.String, nullable=False, unique=True),
    },
    strict=True,
)


# ------------------------------------------------------------------- utilidades
def encontrar_datos() -> Path:
    """Busca la carpeta datos/ aqui o un nivel arriba (util dentro de proyecto_uv/)."""
    if os.environ.get("DATOS_DIR"):
        return Path(os.environ["DATOS_DIR"])
    for candidato in (Path("datos"), Path("../datos")):
        if (candidato / ARCHIVO_VIAJES).exists():
            return candidato
    raise FileNotFoundError(
        f"No encontre {ARCHIVO_VIAJES} en datos/ ni en ../datos/. "
        "Corre primero las celdas de descarga del notebook o define DATOS_DIR."
    )


def escribir_parquet(df: pl.DataFrame, ruta: Path) -> None:
    """Escribe a un archivo temporal y lo renombra. Reemplaza, nunca agrega."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    tmp = ruta.with_name(ruta.name + ".tmp")
    df.write_parquet(tmp)
    os.replace(tmp, ruta)


def cronometrar(metricas: dict, etapa: str, inicio: float) -> None:
    metricas["segundos"][etapa] = round(time.perf_counter() - inicio, 2)


# ----------------------------------------------------------------------- bronze
def construir_bronze(datos: Path) -> Path:
    """Copia fiel del origen, mas una columna que dice de donde vino."""
    destino = datos / "bronze" / ARCHIVO_VIAJES
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_name(destino.name + ".tmp")
    (
        pl.scan_parquet(datos / ARCHIVO_VIAJES)
        .with_columns(pl.lit(ARCHIVO_VIAJES).alias("_origen"))
        .sink_parquet(tmp)
    )
    os.replace(tmp, destino)

    zonas = pl.read_csv(datos / ARCHIVO_ZONAS)
    escribir_parquet(zonas, datos / "bronze" / "zonas.parquet")
    return destino


# ----------------------------------------------------------------------- silver
def construir_silver(datos: Path, metricas: dict):
    """Tipos correctos, 5 validaciones, duplicados y cuarentena."""
    zonas = pl.read_parquet(datos / "bronze" / "zonas.parquet")
    ids_zona = zonas["LocationID"].cast(pl.Int32).to_list()

    crudo = (
        pl.scan_parquet(datos / "bronze" / ARCHIVO_VIAJES)
        .select(COLUMNAS)
        .with_columns(
            pl.col("PULocationID").cast(pl.Int32),
            pl.col("DOLocationID").cast(pl.Int32),
            pl.col("passenger_count").cast(pl.Int64),
            pl.col("payment_type").cast(pl.Int64),
            pl.col("trip_distance", "fare_amount", "tip_amount", "total_amount").cast(
                pl.Float64
            ),
        )
        .collect()
    )

    # Cada regla es una expresion que vale True cuando el registro FALLA.
    # fill_null(False) evita que un nulo "se escape" de la regla por accidente;
    # los nulos los atrapa la primera regla.
    reglas = {
        "nulos_en_columnas_clave": pl.any_horizontal(pl.col(CLAVES).is_null()),
        "distancia_no_positiva": (pl.col("trip_distance") <= 0).fill_null(False),
        "importe_negativo": (pl.col("total_amount") < 0).fill_null(False),
        "zona_inexistente": (
            ~pl.col("PULocationID").is_in(ids_zona)
            | ~pl.col("DOLocationID").is_in(ids_zona)
        ).fill_null(False),
        "fuera_del_mes": ~pl.col("tpep_pickup_datetime")
        .is_between(MES_INICIO, MES_FIN, closed="left")
        .fill_null(False),
    }

    # Cuantos registros incumplen cada regla (una fila puede incumplir varias)
    conteo = crudo.select(
        [expr.sum().alias(nombre) for nombre, expr in reglas.items()]
    ).row(0, named=True)
    metricas["fallas_por_regla"] = {k: int(v) for k, v in conteo.items()}

    # Motivo de rechazo = la primera regla que falla, en el orden del diccionario
    motivo = pl.coalesce(
        [pl.when(expr).then(pl.lit(nombre)) for nombre, expr in reglas.items()]
    ).alias("motivo")

    viaje_id = pl.concat_str(
        [
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "PULocationID",
            "DOLocationID",
            "total_amount",
        ],
        separator="|",
    ).alias("viaje_id")

    marcado = crudo.with_columns(viaje_id, motivo)
    rechazados = marcado.filter(pl.col("motivo").is_not_null())
    buenos = marcado.filter(pl.col("motivo").is_null())

    # Unicidad: si el mismo viaje llega dos veces, nos quedamos con el primero
    es_repetido = ~pl.col("viaje_id").is_first_distinct()
    repetidos = buenos.filter(es_repetido).with_columns(
        pl.lit("duplicado").alias("motivo")
    )
    silver = buenos.filter(~es_repetido).drop("motivo")
    cuarentena = pl.concat([rechazados, repetidos])

    metricas["filas_bronze"] = crudo.height
    metricas["filas_silver"] = silver.height
    metricas["filas_cuarentena"] = cuarentena.height
    metricas["duplicados"] = repetidos.height
    return silver, cuarentena


def validar_contrato(silver: pl.DataFrame) -> None:
    """Pandera como ultima puerta: si algo se colo, el pipeline se detiene."""
    try:
        SCHEMA_SILVER.validate(silver, lazy=True)
    except SchemaErrors as error:
        log.error("El contrato de silver fallo:\n%s", error.failure_cases)
        raise


# ------------------------------------------------------------------------- gold
def construir_gold(silver: pl.DataFrame, datos: Path) -> pl.DataFrame:
    zonas = pl.read_parquet(datos / "bronze" / "zonas.parquet").with_columns(
        pl.col("LocationID").cast(pl.Int32)
    )
    return (
        silver.join(zonas, left_on="PULocationID", right_on="LocationID", how="left")
        .group_by("Borough")
        .agg(
            pl.len().alias("viajes"),
            pl.col("total_amount").sum().round(2).alias("ingreso_total"),
            pl.col("total_amount").mean().round(2).alias("ticket_promedio"),
            pl.col("trip_distance").sum().round(1).alias("millas_totales"),
        )
        .sort(["viajes", "Borough"], descending=[True, False])
    )


def conciliar(datos: Path, filas_silver: int) -> None:
    """Cuadra cuentas con DuckDB leyendo los parquet: silver = suma de gold."""
    con = duckdb.connect()
    silver_n = con.sql(
        f"SELECT COUNT(*) FROM read_parquet('{datos / 'silver' / 'viajes.parquet'}')"
    ).fetchone()[0]
    gold_n = con.sql(
        f"SELECT SUM(viajes) FROM read_parquet('{datos / 'gold' / 'ingresos_borough.parquet'}')"
    ).fetchone()[0]
    if not (silver_n == gold_n == filas_silver):
        raise RuntimeError(
            f"No cuadra: silver={silver_n}, gold={gold_n}, esperado={filas_silver}"
        )
    log.info("Conciliacion OK: silver y gold suman %s viajes", f"{silver_n:,}")


# ------------------------------------------------------------------------- main
def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    metricas: dict = {"segundos": {}}
    t0 = time.perf_counter()

    datos = encontrar_datos()
    log.info("Carpeta de datos: %s", datos.resolve())

    t = time.perf_counter()
    construir_bronze(datos)
    cronometrar(metricas, "bronze", t)
    log.info("BRONZE listo")

    t = time.perf_counter()
    silver, cuarentena = construir_silver(datos, metricas)
    cronometrar(metricas, "silver", t)
    log.info(
        "SILVER listo: %s filas, %s en cuarentena",
        f"{metricas['filas_silver']:,}",
        f"{metricas['filas_cuarentena']:,}",
    )
    for regla, n in metricas["fallas_por_regla"].items():
        log.info("  regla %-26s fallas: %s", regla, f"{n:,}")

    validar_contrato(silver)
    escribir_parquet(silver, datos / "silver" / "viajes.parquet")
    escribir_parquet(cuarentena, datos / "quarantine" / "viajes_rechazados.parquet")

    fraccion = metricas["filas_cuarentena"] / max(metricas["filas_bronze"], 1)
    if fraccion > UMBRAL_CUARENTENA:
        log.warning("Cuarentena alta: %.1f%% de las filas", fraccion * 100)

    t = time.perf_counter()
    gold = construir_gold(silver, datos)
    escribir_parquet(gold, datos / "gold" / "ingresos_borough.parquet")
    cronometrar(metricas, "gold", t)
    log.info("GOLD listo: %s boroughs", gold.height)

    conciliar(datos, metricas["filas_silver"])

    metricas["segundos"]["total"] = round(time.perf_counter() - t0, 2)
    ruta_metricas = datos / "metricas" / "ultima_corrida.json"
    ruta_metricas.parent.mkdir(parents=True, exist_ok=True)
    ruta_metricas.write_text(json.dumps(metricas, indent=2, ensure_ascii=False))
    log.info("Terminado en %s s", metricas["segundos"]["total"])
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        log.exception("El pipeline fallo")
        sys.exit(1)

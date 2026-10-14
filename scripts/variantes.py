#!/usr/bin/env python3
"""Tareas con variantes: parámetros por alumno, hoja de respuestas y calificación.

Cada alumno recibe un número de variante (1 a 10). Con ese número, las tareas de las
sesiones 4, 5, 6, 7 y 9 usan parámetros distintos, así que la misma pregunta da un
resultado distinto para cada quien.

Comandos:
  python3 scripts/variantes.py snippet
      Imprime la celda de Python que va en los notebooks (variantes, MI_VARIANTE y la
      función codigo_entrega).

  python3 scripts/variantes.py clave --datos datos --salida clave/clave_variantes.csv
      Calcula la respuesta correcta de cada variante con el dataset real
      (datos/viajes_2024_01.parquet y datos/zonas.csv). La carpeta clave/ NO se sube a git.

  python3 scripts/variantes.py calificar --clave clave/clave_variantes.csv \
      --entregas entregas/entregas.csv --salida entregas/resultado.csv
      Compara los códigos de entrega de los alumnos contra la clave.
      entregas.csv tiene las columnas: alumno,codigo

Requiere: pip install polars
"""
import argparse
import csv
import sys
from pathlib import Path

VARIANTES = {
    1: {"borough": "Manhattan", "tipo_pago": 1, "distancia_min": 2, "pasajeros_min": 1, "distancia_max": 10},
    2: {"borough": "Queens", "tipo_pago": 1, "distancia_min": 3, "pasajeros_min": 2, "distancia_max": 12},
    3: {"borough": "Brooklyn", "tipo_pago": 1, "distancia_min": 1, "pasajeros_min": 1, "distancia_max": 15},
    4: {"borough": "Manhattan", "tipo_pago": 2, "distancia_min": 2, "pasajeros_min": 2, "distancia_max": 18},
    5: {"borough": "Bronx", "tipo_pago": 1, "distancia_min": 1, "pasajeros_min": 1, "distancia_max": 20},
    6: {"borough": "Queens", "tipo_pago": 2, "distancia_min": 5, "pasajeros_min": 1, "distancia_max": 25},
    7: {"borough": "Brooklyn", "tipo_pago": 2, "distancia_min": 1, "pasajeros_min": 2, "distancia_max": 30},
    8: {"borough": "Manhattan", "tipo_pago": 1, "distancia_min": 5, "pasajeros_min": 3, "distancia_max": 35},
    9: {"borough": "Bronx", "tipo_pago": 2, "distancia_min": 2, "pasajeros_min": 1, "distancia_max": 40},
    10: {"borough": "Queens", "tipo_pago": 1, "distancia_min": 1, "pasajeros_min": 3, "distancia_max": 50},
}

# Qué mide cada tarea con variante. Las columnas son los nombres que lleva el código de entrega.
TAREAS = {
    "S04": ("n", "ticket"),
    "S05": ("zona", "ingreso"),
    "S06": ("n", "duracion"),
    "S07": ("hora", "n"),
    "S09": ("n",),
}


def snippet():
    filas = ",\n".join(f"    {k}: {v!r}" for k, v in VARIANTES.items())
    print(f'''# Tu número de variante: te lo da el instructor (del 1 al 10)
MI_VARIANTE = ...

VARIANTES = {{
{filas},
}}

def codigo_entrega(sesion, **resultados):
    """Imprime el código que pegas en el formulario de entrega."""
    partes = [sesion, f"V{{MI_VARIANTE}}"] + [f"{{k}}={{v}}" for k, v in resultados.items()]
    print("|".join(partes))

# Usa tus parámetros así:  params = VARIANTES[MI_VARIANTE]
''')


def _cargar(datos):
    import polars as pl

    d = Path(datos)
    viajes = pl.read_parquet(d / "viajes_2024_01.parquet")
    zonas = pl.read_csv(d / "zonas.csv")
    return pl, viajes, zonas


def calcular(pl, viajes, zonas, p):
    r = {}
    con_zona = viajes.join(zonas, left_on="PULocationID", right_on="LocationID", how="left")

    # S04: viajes de la zona y el pago, y ticket promedio
    s4 = con_zona.filter((pl.col("Borough") == p["borough"]) & (pl.col("payment_type") == p["tipo_pago"]))
    r["S04"] = {"n": s4.height, "ticket": round(s4["total_amount"].mean(), 2)}

    # S05: zona con más ingreso dentro del borough
    s5 = (
        con_zona.filter(pl.col("Borough") == p["borough"])
        .group_by("Zone")
        .agg(pl.col("total_amount").sum().alias("ingreso"))
        .sort(["ingreso", "Zone"], descending=[True, False])
        .head(1)
    )
    r["S05"] = {"zona": s5["Zone"][0], "ingreso": round(s5["ingreso"][0], 2)}

    # S06: viajes largos con pasajeros, duración promedio en minutos (dt.total_minutes)
    s6 = viajes.filter(
        (pl.col("trip_distance") > p["distancia_min"]) & (pl.col("passenger_count") >= p["pasajeros_min"])
    ).with_columns(
        (pl.col("tpep_dropoff_datetime") - pl.col("tpep_pickup_datetime")).dt.total_minutes().alias("duracion_min")
    )
    r["S06"] = {"n": s6.height, "duracion": round(s6["duracion_min"].mean(), 2)}

    # S07: hora pico de recogida dentro del borough
    s7 = (
        con_zona.filter(pl.col("Borough") == p["borough"])
        .with_columns(pl.col("tpep_pickup_datetime").dt.hour().alias("hora"))
        .group_by("hora")
        .agg(pl.len().alias("n"))
        .sort(["n", "hora"], descending=[True, False])
        .head(1)
    )
    r["S07"] = {"hora": s7["hora"][0], "n": s7["n"][0]}

    # S09: registros que caen a cuarentena por la regla propia de distancia máxima
    r["S09"] = {"n": viajes.filter(pl.col("trip_distance") > p["distancia_max"]).height}
    return r


def clave(datos, salida):
    pl, viajes, zonas = _cargar(datos)
    salida = Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["variante", "sesion", "campo", "valor"])
        for v, p in VARIANTES.items():
            for ses, campos in calcular(pl, viajes, zonas, p).items():
                for campo, valor in campos.items():
                    w.writerow([v, ses, campo, valor])
    print("clave escrita en", salida)


def _igual(a, b):
    a, b = str(a).strip(), str(b).strip()
    try:
        return abs(float(a) - float(b)) <= 0.011
    except ValueError:
        return a.lower() == b.lower()


def calificar(clave_csv, entregas_csv, salida):
    ref = {}
    with open(clave_csv, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ref[(int(r["variante"]), r["sesion"], r["campo"])] = r["valor"]

    resultados = []
    with open(entregas_csv, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            alumno, codigo = fila.get("alumno") or "?", (fila.get("codigo") or "").strip()
            if not codigo:
                continue
            try:
                ses, var, *campos = [x.strip() for x in codigo.split("|")]
                variante = int(var.lstrip("Vv"))
                datos = {k.strip(): v.strip() for k, v in (c.split("=", 1) for c in campos)}
            except ValueError:
                resultados.append((alumno, "?", "?", "formato", "codigo ilegible"))
                continue
            for campo in TAREAS.get(ses, ()):
                esperado = ref.get((variante, ses, campo))
                dado = datos.get(campo)
                if esperado is None or dado is None:
                    estado = "falta"
                else:
                    estado = "ok" if _igual(dado, esperado) else "mal"
                resultados.append((alumno, ses, variante, campo, estado))

    salida = Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["alumno", "sesion", "variante", "campo", "estado"])
        w.writerows(resultados)
    print("resultado escrito en", salida)
    for r in resultados:
        if r[-1] != "ok":
            print("revisar:", r)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("snippet")
    c = sub.add_parser("clave")
    c.add_argument("--datos", default="datos")
    c.add_argument("--salida", default="clave/clave_variantes.csv")
    g = sub.add_parser("calificar")
    g.add_argument("--clave", default="clave/clave_variantes.csv")
    g.add_argument("--entregas", required=True)
    g.add_argument("--salida", default="entregas/resultado.csv")
    a = ap.parse_args()
    if a.cmd == "snippet":
        snippet()
    elif a.cmd == "clave":
        clave(a.datos, a.salida)
    else:
        calificar(a.clave, a.entregas, a.salida)


if __name__ == "__main__":
    sys.exit(main())

# Proyecto final: un pipeline documentado en Deepnote

Este es el proyecto final del curso Ingeniería de Datos desde Cero. Vale 40% de la evaluación final. Se asigna al cierre de la sesión 8, se pide avance en la sesión 9 y se entrega y presenta en la sesión 10.

## Qué entregas

- Un proyecto de Deepnote con un notebook que corre de arriba hacia abajo (Run all) sin errores.
- Ese notebook contiene todo el trabajo: ingesta, capas, validaciones, análisis, gráficas y explicación escrita.
- Una presentación de 3 a 5 minutos en la sesión 10, usando el mismo notebook publicado. No hacen falta diapositivas.
- El enlace del proyecto, enviado por el medio que indique el instructor.

La evaluación usa la rúbrica de `RUBRICA.md` (100 puntos).

## Opciones de dataset

| Opción | Dataset | Idea de pregunta |
|---|---|---|
| 1 | NYC TLC Yellow Taxi enero 2024 y `taxi_zone_lookup.csv` (el dataset del curso, ver `docs/DATASETS.md`) | ¿Dónde y a qué hora se concentra el ingreso? ¿Cómo cambia la propina según el método de pago? |
| 2 | Ecobici CDMX, portal `datos.cdmx.gob.mx` | ¿Cómo cambian los viajes por estación y horario? Verificar disponibilidad de los datos y las columnas reales antes de elegirlo. |
| 3 | Un dataset libre, aprobado por el instructor | Debe ser de una fuente abierta, caber en la máquina de Deepnote (5 GB de RAM), y permitir un JOIN entre una tabla de hechos y una de catálogo. |

Si propones un dataset libre, envía al instructor: el enlace, una descripción de dos líneas, el nombre de las dos tablas para el JOIN y la pregunta que quieres responder. Otras fuentes de datos abiertos: `inegi.org.mx/datosabiertos` y `datos.gob.mx`.

## Requisitos

Tu proyecto debe tener, como mínimo:

1. **Ingesta** desde un archivo Parquet o CSV.
2. **Al menos un JOIN** entre una tabla de hechos y una de dimensión (por ejemplo, viajes con zonas).
3. **Al menos tres agregaciones** (por ejemplo, por zona, por hora y por método de pago).
4. **Capas bronze, silver y gold**, cada una escrita en su carpeta.
5. **Al menos tres validaciones de calidad de datos**, con cuarentena de los registros inválidos.
6. **Documentación en Markdown** que explique cada paso y por qué se hizo.
7. **Al menos dos visualizaciones**, con título y ejes con nombre.
8. **Publicado en Deepnote**, con enlace que se pueda abrir sin pedir permisos.

## Plantilla de estructura del notebook

Usa estas secciones, en este orden. Cada una tiene una celda de Markdown que explica y las celdas de código.

```text
# Título del proyecto
## 0. Resumen
   - Pregunta que respondes
   - Dataset y fuente
   - Hallazgo principal en una o dos frases
   - Cómo reproducirlo (Run all, qué archivos se descargan)
## 1. Preparación
   - Imports, rutas y carpetas de las capas
## 2. Ingesta y capa bronze
   - De dónde vienen los datos, cuántas filas y columnas, esquema
   - Bronze: copia fiel del origen
## 3. Calidad de datos y capa silver
   - Perfil de calidad (qué tan sucio viene)
   - Las validaciones: qué regla, qué dimensión de calidad, por qué
   - Cuarentena con motivo y cuántos registros cayeron
   - Contrato con Pandera
## 4. Capa gold: JOIN y agregaciones
   - El JOIN y qué columnas aporta
   - Las tres agregaciones, cada una con la pregunta que responde
## 5. Visualizaciones
   - Dos o más gráficas con título, ejes y una frase de lectura
## 6. Hallazgos
   - Tres a cinco conclusiones, con números tomados de los datos
## 7. Límites y siguientes pasos
   - Qué no se pudo hacer, qué supuestos hay, qué mejorarías
## 8. Verificación
   - Una celda que revisa que las capas existen
```

### Esqueleto de código (opción 1, taxis)

Si usas el dataset de taxis, estas celdas funcionan después de correr el pipeline de la sesión 9. Si usas otro dataset, cambia las columnas y las reglas. Los pasos son los mismos.

Lectura de las capas y resumen del flujo:

```python
import json
from pathlib import Path

import plotly.express as px
import polars as pl

DATOS = Path("datos")

silver = pl.read_parquet(DATOS / "silver" / "viajes.parquet")
gold = pl.read_parquet(DATOS / "gold" / "ingresos_borough.parquet")
cuarentena = pl.read_parquet(DATOS / "quarantine" / "viajes_rechazados.parquet")

total_leidos = silver.height + cuarentena.height
print(f"Viajes que entraron al pipeline: {total_leidos:,}")
print(f"Viajes que pasaron a silver:     {silver.height:,}")
print(f"Viajes en cuarentena:            {cuarentena.height:,} ({cuarentena.height / total_leidos:.2%})")
```

JOIN y tres agregaciones:

```python
zonas = pl.read_parquet(DATOS / "bronze" / "zonas.parquet").with_columns(pl.col("LocationID").cast(pl.Int32))

# Un solo JOIN (hecho + dimensión) que usamos para las tres agregaciones
enriquecido = silver.join(zonas, left_on="PULocationID", right_on="LocationID", how="left")

# Agregación 1: ingresos por borough
por_borough = (
    enriquecido.group_by("Borough")
    .agg(pl.len().alias("viajes"), pl.col("total_amount").sum().round(2).alias("ingreso_total"))
    .sort("ingreso_total", descending=True)
)

# Agregación 2: viajes por hora del día
por_hora = (
    enriquecido.group_by(pl.col("tpep_pickup_datetime").dt.hour().alias("hora"))
    .agg(pl.len().alias("viajes"))
    .sort("hora")
)

# Agregación 3: propina promedio por método de pago (porcentaje sobre la tarifa)
por_pago = (
    enriquecido.filter(pl.col("fare_amount") > 0)
    .group_by("payment_type")
    .agg(
        pl.len().alias("viajes"),
        (pl.col("tip_amount") / pl.col("fare_amount")).mean().mul(100).round(1).alias("propina_pct"),
    )
    .sort("viajes", descending=True)
)
print(por_borough, por_hora.head(3), por_pago, sep="\n")
```

Dos visualizaciones:

```python
fig1 = px.bar(
    por_borough,
    x="Borough",
    y="ingreso_total",
    title="Ingreso total por borough de origen",
    labels={"ingreso_total": "Ingreso total (USD)", "Borough": "Borough"},
)

fig2 = px.line(
    por_hora,
    x="hora",
    y="viajes",
    markers=True,
    title="Viajes por hora del día",
    labels={"hora": "Hora del día", "viajes": "Viajes"},
)
fig2.update_xaxes(dtick=1)

# fig1.show() y fig2.show() dibujan las gráficas en Deepnote
```

Resumen escrito con números reales:

```python
# Un resumen escrito con datos reales: el texto se actualiza solo si cambian los datos.
mejor = por_borough.row(0, named=True)
pico = por_hora.sort("viajes", descending=True).row(0, named=True)

resumen = f"""
**Hallazgos**

- El borough con más ingreso es **{mejor['Borough']}** con {mejor['ingreso_total']:,.2f} dólares en {mejor['viajes']:,} viajes.
- La hora con más viajes es las **{pico['hora']}:00**, con {pico['viajes']:,} viajes.
- {cuarentena.height:,} viajes ({cuarentena.height / total_leidos:.2%}) se rechazaron en calidad de datos.
"""
print(resumen)
# En Deepnote puedes mostrarlo con: from IPython.display import Markdown; Markdown(resumen)
```

Para el pipeline bronze, silver y gold con validaciones y cuarentena, usa el código de la sesión 9 (`docs/guia/S09.md`) o el script `proyecto_uv/pipeline.py`. Con otro dataset, la función `validar_y_separar` de la tarea de la sesión 9 sirve de base.

Plotly debe estar en los requisitos del proyecto de Deepnote. Los valores finales con el dataset real: verificar en la nube.

## Calendario sugerido

| Cuándo | Qué se hace |
|---|---|
| Cierre de la sesión 8 | Se asigna el proyecto. Elige tu dataset y envía una propuesta de cinco líneas (pregunta, dataset, capas, validaciones previstas, gráficas). Crea el notebook con la plantilla y ejecuta la ingesta. |
| Sesión 9 | Avance obligatorio: pipeline con las tres capas y al menos 3 validaciones, con cuarentena. Comprueba la idempotencia (correrlo dos veces no duplica). |
| Entre la sesión 9 y la 10 | Agrega el JOIN, las tres agregaciones, las dos gráficas y empieza la documentación. |
| Sesión 10, bloque de taller | Terminas, haces la revisión entre pares con la lista de verificación y aplicas los comentarios. |
| Sesión 10, minuto 120 | Se entrega el enlace del proyecto. |
| Sesión 10, presentaciones | Presentas en 3 a 5 minutos (el instructor define el reparto según el tamaño del grupo). |

Las fechas exactas de calendario las define el instructor.

## Formato de entrega

- **Qué se entrega:** el enlace al proyecto de Deepnote.
- **Nombre del proyecto:** `Proyecto final - Nombre Apellido`.
- **Acceso:** abre sin pedir permisos. Usa enlace compartido en nivel View o una app publicada con la visibilidad que permita tu plan (verificar en tu cuenta qué opciones tienes). Para la revisión entre pares comparte en nivel Comment.
- **Estado del notebook:** reinicia la máquina y haz Run all antes de entregar. No debe haber errores ni celdas que dependan de variables que no estén definidas arriba.
- **Primera sección:** el resumen (pregunta, dataset, hallazgo y cómo reproducirlo).
- **Datos:** el notebook descarga o lee los archivos por sí mismo, desde una URL pública o desde `datos/` generada en el propio notebook. Sin rutas que solo existan en tu computadora.
- **Datos personales:** no publiques datos personales ni sensibles.
- **Cómo se envía:** formulario o canal indicado por el instructor, con tu nombre, el enlace y el dataset elegido.

## Consejos

- Primero que corra, luego que se vea bien.
- Un proyecto pequeño y completo vale más que uno grande y a medias.
- Escribe el resumen del principio al final, cuando ya sabes qué encontraste.
- Cada validación debe tener una razón: qué dimensión de calidad protege (completitud, validez, unicidad, consistencia, oportunidad).
- Cada gráfica debe responder una pregunta, con título y ejes con nombre.
- Pide a alguien que haga Run all en tu proyecto antes de entregar.

## Recursos

- Guías de sesión: `docs/guia/S08.md`, `docs/guia/S09.md` y `docs/guia/S10.md`.
- Pipeline de referencia: `proyecto_uv/pipeline.py`.
- Rúbrica y lista de verificación para pares: `RUBRICA.md`.

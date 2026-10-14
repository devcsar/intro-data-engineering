# Databricks notebook source
# MAGIC %md
# MAGIC # Sesión 8: Databricks y el lakehouse
# MAGIC
# MAGIC **Curso Ingeniería de Datos desde Cero, Impact Click**
# MAGIC
# MAGIC En este notebook vas a:
# MAGIC
# MAGIC - Subir el parquet de taxis a un volumen de Unity Catalog
# MAGIC - Crear una tabla Delta gestionada
# MAGIC - Consultarla con SQL y con PySpark
# MAGIC - Ver su historial y viajar en el tiempo
# MAGIC - Hacer una visualización
# MAGIC
# MAGIC **Antes de empezar:**
# MAGIC
# MAGIC - Conecta el notebook a **Serverless** (selector de compute, arriba a la derecha). En Free Edition es la única opción.
# MAGIC - Ejecuta las celdas de arriba hacia abajo, con Shift + Enter.
# MAGIC - Nombres usados aquí: catálogo `workspace`, esquema `curso_de`, volumen `taxi`, tabla `yellow_taxi`. Si tu catálogo por defecto se llama distinto, usa buscar y reemplazar (verificar en tu cuenta).

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Crear esquema y volumen
# MAGIC
# MAGIC Unity Catalog organiza todo en tres niveles: `catálogo.esquema.objeto`. Un **volumen** es el lugar para guardar archivos (como nuestro parquet) bajo el mismo gobierno que las tablas.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.curso_de;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.curso_de.taxi;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Subir el parquet al volumen (paso manual, en la interfaz)
# MAGIC
# MAGIC El notebook no puede descargar el archivo por internet porque Free Edition limita la salida a un conjunto de dominios de confianza (verificar si CloudFront está permitido en tu cuenta). Se sube a mano:
# MAGIC
# MAGIC 1. Ten en tu computadora el archivo `yellow_tripdata_2024-01.parquet` (viene de la sesión 1, o se descarga de la URL del curso en tu navegador).
# MAGIC 2. En la barra lateral: **New**, luego **Add or upload data**, luego **Upload files to a volume**.
# MAGIC 3. Elige el volumen `workspace.curso_de.taxi`.
# MAGIC 4. Arrastra el archivo y confirma.
# MAGIC 5. Repite con `taxi_zone_lookup.csv` (lo guardaste como `zonas.csv` en la sesión 1, sube ese).
# MAGIC
# MAGIC Luego ejecuta la celda de abajo para confirmar que los archivos están.

# COMMAND ----------

RUTA_VOLUMEN = "/Volumes/workspace/curso_de/taxi"
RUTA_VIAJES = f"{RUTA_VOLUMEN}/yellow_tripdata_2024-01.parquet"
RUTA_ZONAS = f"{RUTA_VOLUMEN}/zonas.csv"
TABLA = "workspace.curso_de.yellow_taxi"

# Si falta algún archivo, esta celda lo dice con claridad
for archivo in dbutils.fs.ls(RUTA_VOLUMEN):
    print(archivo.name, f"{archivo.size / 1_000_000:.1f} MB")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Crear la tabla Delta (gestionada)
# MAGIC
# MAGIC Leemos el parquet con Spark y lo guardamos como tabla. Al usar `saveAsTable` sin ruta, la tabla es **gestionada**: Databricks decide dónde viven los archivos y se encarga de ellos.

# COMMAND ----------

viajes = spark.read.parquet(RUTA_VIAJES)

(
    viajes.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable(TABLA)
)

print("Tabla creada:", TABLA)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS filas FROM workspace.curso_de.yellow_taxi;

# COMMAND ----------

# MAGIC %md
# MAGIC ### ¿Gestionada o externa?
# MAGIC
# MAGIC En la columna `Type` de este resultado debe decir `MANAGED`. Una tabla externa diría `EXTERNAL` y tendría una ruta propia que tú controlas.

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED workspace.curso_de.yellow_taxi;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Consulta SQL
# MAGIC
# MAGIC La misma pregunta de la sesión 1: viajes y ticket promedio por método de pago.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   payment_type,
# MAGIC   COUNT(*) AS viajes,
# MAGIC   ROUND(AVG(total_amount), 2) AS ticket
# MAGIC FROM workspace.curso_de.yellow_taxi
# MAGIC GROUP BY payment_type
# MAGIC ORDER BY viajes DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. La misma consulta en PySpark
# MAGIC
# MAGIC Dos lenguajes, el mismo motor. Spark es **perezoso**: las transformaciones (`groupBy`, `agg`, `orderBy`) solo arman el plan, y las acciones (`display`, `show`, `count`) lo ejecutan.

# COMMAND ----------

from pyspark.sql import functions as F

pagos = (
    spark.table(TABLA)
    .groupBy("payment_type")
    .agg(
        F.count("*").alias("viajes"),
        F.round(F.avg("total_amount"), 2).alias("ticket"),
    )
    .orderBy(F.desc("viajes"))
)

display(pagos)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Historial y time travel
# MAGIC
# MAGIC Delta guarda un registro de cada cambio. Primero miramos el historial, luego hacemos un cambio (borrar viajes con distancia cero) y comparamos antes y después.

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY workspace.curso_de.yellow_taxi;

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM workspace.curso_de.yellow_taxi WHERE trip_distance = 0;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY workspace.curso_de.yellow_taxi;

# COMMAND ----------

# Buscamos la versión del DELETE y la anterior, sin tener que adivinar números
historial = spark.sql(f"DESCRIBE HISTORY {TABLA}")
version_delete = historial.filter("operation = 'DELETE'").agg(F.max("version")).first()[0]

if version_delete is None:
    print("No se encontró un DELETE en el historial. Ejecuta la celda del DELETE primero.")
else:
    version_antes = version_delete - 1
    antes = spark.sql(f"SELECT COUNT(*) AS n FROM {TABLA} VERSION AS OF {version_antes}").first()["n"]
    despues = spark.sql(f"SELECT COUNT(*) AS n FROM {TABLA}").first()["n"]
    print(f"Versión antes del DELETE: {version_antes}")
    print(f"Filas antes:   {antes:,}")
    print(f"Filas después: {despues:,}")
    print(f"Filas borradas: {antes - despues:,}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Deshacer el cambio
# MAGIC
# MAGIC `RESTORE` regresa la tabla a una versión anterior. Reemplaza el número por la `version_antes` que imprimió la celda de arriba.

# COMMAND ----------

# Escribe aquí el número de version_antes que imprimió la celda anterior, por ejemplo 3.
# Mientras valga None, esta celda no hace nada (así Run all no deshace tu trabajo sin querer).
VERSION_A_RESTAURAR = None

if VERSION_A_RESTAURAR is None:
    print("Pendiente: escribe la versión a restaurar.")
else:
    display(spark.sql(f"RESTORE TABLE {TABLA} TO VERSION AS OF {VERSION_A_RESTAURAR}"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Visualización
# MAGIC
# MAGIC Viajes por hora del día. Al ejecutar la celda aparece una tabla. Haz clic en el signo **+** junto a "Table", elige **Visualization**, tipo **Line** o **Bar**, eje X `hora`, eje Y `viajes`. Toma una captura.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   HOUR(tpep_pickup_datetime) AS hora,
# MAGIC   COUNT(*) AS viajes
# MAGIC FROM workspace.curso_de.yellow_taxi
# MAGIC GROUP BY HOUR(tpep_pickup_datetime)
# MAGIC ORDER BY hora;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Ejercicio opcional: la tabla de zonas y un JOIN
# MAGIC
# MAGIC Crea la tabla `zonas` desde el CSV y calcula viajes por `Borough`.

# COMMAND ----------

zonas = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(RUTA_ZONAS)
)
zonas.write.format("delta").mode("overwrite").saveAsTable("workspace.curso_de.zonas")
display(zonas.limit(5))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT z.Borough, COUNT(*) AS viajes
# MAGIC FROM workspace.curso_de.yellow_taxi t
# MAGIC LEFT JOIN workspace.curso_de.zonas z ON t.PULocationID = z.LocationID
# MAGIC GROUP BY z.Borough
# MAGIC ORDER BY viajes DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Limpieza (opcional)
# MAGIC
# MAGIC Si quieres borrar lo creado hoy, quita el `#` de las líneas. No es necesario: las tablas no consumen tu cuota de cómputo.

# COMMAND ----------

# spark.sql("DROP TABLE IF EXISTS workspace.curso_de.yellow_taxi")
# spark.sql("DROP TABLE IF EXISTS workspace.curso_de.zonas")
# spark.sql("DROP VOLUME IF EXISTS workspace.curso_de.taxi")
# spark.sql("DROP SCHEMA IF EXISTS workspace.curso_de")

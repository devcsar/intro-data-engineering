# Registro de verificación en la nube

Aquí se anota lo que se comprueba ejecutando los notebooks en Deepnote real. Una fila por prueba. Esta tabla la llena Claude Code durante la construcción y el instructor en los ensayos.

## Corridas

| Fecha | Sesión | Dónde | Resultado | Tiempo de Run all | Notas |
|---|---|---|---|---|---|
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | Error: `ModuleNotFoundError: No module named 'polars'` | 12 s hasta detenerse | `requirements.txt` subido como archivo del proyecto no se instala solo. El run se detiene en el primer error. |
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | Error en el bloque SQL: `This SQL cell is not linked with a connected integration` | 50 s | La celda de instalación ya funcionaba. El MCP creó el SQL sin `sql_integration_id` (no acepta `deepnote-dataframe-sql`). |
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | **OK** (status success, sin errores) | 39 s | Tras corregir el SQL con `deepnote sync` (push). Descarga de 2,964,624 filas en 1 s, guardar el parquet 16 s, SQL 2.5 s. La verificación imprime los 3 "Pendiente" esperados. |
| 2026-10-15 | 2 | Deepnote (run detached, MCP) | Se detiene en la celda rota 1 del taller (`NameError: distancia_kms`), como se diseñó | ~60 s hasta la celda rota | Todo lo anterior corre bien. La verificación antes del taller marca Pendiente los 5 ejercicios sin resolver. La versión con soluciones se probó en local: "Sesión 2 completa". |
| 2026-10-15 | 3 | Deepnote (run detached, MCP) | **OK** (status success) | ~4 min 3 s | Máquina Basic, sin problemas de memoria ni de disco. Compresión 29 s, CSV escrito 13.6 s, NDJSON 29.3 s, lecturas de vuelta 21 s y 75 s. La limpieza final deja solo el Parquet y `zonas.csv`. |
| 2026-10-15 | 4 | Deepnote (run detached, MCP) | **OK** (status success) | ~55 s | 26 bloques SQL con `deepnote-dataframe-sql` corren. La salida del bloque SQL es un DataFrame de pandas (con `.columns` y `len()`), y los nulos salen como `<NA>`. `duckdb.sql()` encuentra los DataFrames de Polars (`viajes`, `zonas`, `zonas_reducida`). La verificación marca los 5 ejercicios Pendiente. |
| 2026-10-15 | 5 | Deepnote (run detached, MCP) | Primeros 2 intentos: `stopped`, "Execution was aborted" (el kernel se reinició) en el bloque SQL del star schema | ~50 s | Causa aislada con notebooks temporales (ya borrados): reutilizar la MISMA CTE dos veces (`dim_zona` como origen y destino) en un bloque SQL de Deepnote cierra el kernel en unos 3 s. No es memoria: la misma consulta con `duckdb.sql()` corre en 0.6 s usando +600 MB. Dos `JOIN` a la tabla `zonas` directa sí funcionan. |
| 2026-10-15 | 5 | Deepnote (run detached, MCP) | **OK** (status success) | ~51 s | Tras definir dos CTEs, `dim_zona_origen` y `dim_zona_destino`. |

## Valores reales del dataset (reemplazan los "verificar en la nube" de las guías)

| Sesión | Dato | Valor | Cómo se obtuvo |
|---|---|---|---|
| 1 | Viajes con más de un pasajero (`viajes_compartidos`) | 604,258 | Solución de la guía ejecutada con Polars 1.43.2 sobre el mismo parquet, desde `uv run` local (no en la nube) |
| 1 | Viaje más caro: `total_amount` y zona | 5000.0 en la zona 264 (Unknown, N/A) | Igual. Hay 2 viajes empatados en 5000.0, ambos de la zona 264 y con distancia 0.0 |
| 2 | Viajes largos (más de 5 millas) en las primeras 100 distancias (`n_largos`) | 19 (promedio de esas 100: 3.34 millas) | Solución de la guía con Polars 1.43.2 desde `uv run` local |
| 3 | Tamaño y lectura de CSV | 342.0 MB, 21.29 s (5.8 veces el Parquet) | Run en la nube, celdas 8.3 y 8.4 |
| 3 | Tamaño y lectura de NDJSON | 1,178.4 MB, 75.18 s (20.0 veces el Parquet) | Run en la nube |
| 3 | Tamaño y lectura de Parquet | 58.8 MB, 1.59 s | Run en la nube. Compresión: sin comprimir 269.3 MB, snappy 84.5 MB, zstd 58.8 MB |
| 3 | Columnas que cambian de tipo al leer el CSV | `VendorID`, `tpep_pickup_datetime`, `tpep_dropoff_datetime`, `PULocationID`, `DOLocationID` | Las fechas llegan como String y los tres enteros pasan de Int32 a Int64 |
| 3 | Tipo de `PULocationID` en el Parquet | Int32 | Esquema del Parquet |
| 3 | Zonas: CSV contra Parquet (tarea 2) | 10,467 bytes contra 4,968 bytes | Ejecución local |
| 3 | Plan de `scan_parquet().select().filter().explain()` | Incluye `PROJECT 3/19 COLUMNS` y `SELECTION: col("total_amount") > 100.0` | Run en la nube. Row groups del Parquet: 25 |
| 4 | Viajes con origen en 264 y 265 | 10,360 (Unknown) y 1,658 (Outside of NYC) | Run en la nube |
| 4 | Resumen de totales | 2,964,624 viajes, 79,456,384.28 dólares, ticket 26.80, mínimo -900.0, máximo 5000.0 | Run en la nube |
| 4 | Viajes sin pasajeros (`passenger_count` nulo) | 140,162 | Run en la nube |
| 4 | Tipos de pago con más de 1000 viajes | 5 (1, 2, 0, 4 y 3) | Ejecución local con DuckDB |
| 4 | Tarea: distancia cero / total negativo | 60,371 / 35,504 viajes (suman -893,379.04) | Ejecución local con DuckDB |
| 5 | Tamaño en memoria normalizado contra desnormalizado | 376 MB (19 columnas) contra 519 a 520 MB (23 columnas) | Local y nube |
| 5 | Bronze contra silver | 2,964,624 contra 2,872,021 (92,603 menos) | Ejecución local |
| 5 | Viajes con distancia mayor al promedio (`ej1_n`) | 623,986 | Ejecución local |
| 5 | Fechas fuera de enero 2024 en `tpep_pickup_datetime` | 18 viajes (2002-12-31, 2009-01-01, 2023-12-31 y 2024-02-01) | Ejecución local |
| | | | |

## Preguntas abiertas a confirmar

- [x] `requirements.txt` se instala solo en la copia del alumno, o hace falta la celda `%pip install`. Resultado (2026-10-14): NO se instala solo. Con el archivo subido al proyecto, `import polars` falla. Hace falta una celda de instalación. `uv` NO viene instalado en la máquina (`uv: command not found`), así que la celda de la sesión 1 hace `!pip install -q uv` y luego `!uv pip install -q --python {sys.executable} -r requirements.txt`. Probado en la nube: instala en unos 15 s.
- [x] Bloque SQL `deepnote-dataframe-sql` consulta DataFrames en memoria (sesión 1). Sí funciona, pero solo si el bloque lleva `sql_integration_id: deepnote-dataframe-sql`, y el MCP no puede ponerlo. Se fijó empujando el `.deepnote` con `deepnote sync`.
- [x] Run all se detiene en la primera celda con error (taller de errores de la sesión 2). Sí se detiene (2026-10-15). El taller va al final, después de la verificación.
- [x] Tiempos y espacio de CSV y NDJSON de la sesión 3 en la máquina Basic. Run all completo tarda unos 4 minutos y no hay problemas de memoria ni de disco (pico de unos 1.9 GB en `datos/` antes de la limpieza).
- [x] `pyarrow` disponible en el proyecto (la demostración de Arrow de la sesión 3 corre).
- [x] Bloques SQL con CTE, `QUALIFY` y `VALUES` en `deepnote-dataframe-sql`. Sí corren (sesiones 4 y 5), con una excepción: una misma CTE usada dos veces en un bloque SQL cierra el kernel (ver arriba). La salida de un bloque SQL es un DataFrame de pandas con `.columns` y `len()`.
- [ ] Mermaid se dibuja en Markdown de Deepnote. NO verificado: desde WSL no hay navegador y la API no devuelve el render. El notebook S05 trae el diagrama en un bloque Markdown con tres formas (lista, dibujo en texto y código Mermaid), así que sirve aunque no se dibuje. Falta que alguien abra S05 en Deepnote y mire la sección 8.
- [ ] Salida real de `explain()` (sesión 6)
- [ ] Plotly se muestra en el notebook (sesión 7)
- [ ] `databricks/S08_notebook.py` ensayado en una cuenta Free de Databricks
- [ ] Cuota diaria y catálogo por defecto en Databricks Free Edition
- [ ] Terminal de Deepnote disponible en cuenta Free y `uv` preinstalado (sesión 9)
- [ ] Un usuario con cuenta Free puede publicar y compartir por enlace (sesión 10)
- [ ] CloudFront accesible desde Deepnote
- [ ] La clave de variantes (`scripts/variantes.py clave`) coincide en la nube con la variante 1 de S04
- [ ] Forms de entrega creado y probado con un código de entrega real

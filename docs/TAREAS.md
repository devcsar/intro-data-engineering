# Tareas y evaluación del trabajo de los alumnos

Como el material del curso es abierto y las soluciones están en las guías, la tarea no puede depender de que el alumno "encuentre la respuesta". Por eso se evalúan cuatro cosas: que el notebook corra, que sepa modificar un ejemplo, que resuelva un problema nuevo con sus propios parámetros y que lo explique con sus palabras.

## Qué se evalúa

| Nivel | Qué demuestra | Cómo se ve |
|---|---|---|
| Ejecutar | Puede correr un notebook completo y repetible | Run all sin errores, sin celdas fuera de orden |
| Modificar | Puede cambiar un ejemplo de clase | Mismo código con otra zona, otro pago, otro rango |
| Crear | Puede resolver un problema nuevo | Tarea con variante, sin ejemplo al lado |
| Explicar | Entiende por qué lo hizo así | Texto breve en Markdown dentro del notebook |

## Tipos de tarea por sesión

| Sesión | Tarea | Variante | Qué se entrega |
|---|---|---|---|
| 1 | 10 ejercicios cortos de Python (preparan la sesión 2) | No | Notebook ejecutado y una explicación de 3 líneas |
| 2 | Cuaderno de ejercicios y "arregla esto" (3 celdas rotas distintas a las de clase) | No | Notebook ejecutado y explicación del error más difícil |
| 3 | Tabla comparativa CSV contra Parquet con conclusión escrita | No, pero cada quien usa los números de su propia corrida | Tabla y conclusión de mínimo 3 frases |
| 4 | Consulta SQL con join y agregación | **Sí** (borough y tipo de pago) | Código de entrega y explicación |
| 5 | CTE con window function y diagrama del star schema | **Sí** (borough) | Código de entrega, diagrama y explicación |
| 6 | Pipeline lazy con filtro y duración | **Sí** (distancia y pasajeros mínimos) | Código de entrega y lectura de `explain()` |
| 7 | Análisis por hora con join | **Sí** (borough) | Código de entrega y una gráfica |
| 8 | Tabla creada y consulta en Databricks | No | Captura de pantalla |
| 9 | Pipeline con regla propia de validación | **Sí** (distancia máxima) | Código de entrega y registro de cuarentena |
| 10 | Proyecto final | No, cada quien elige dataset | Proyecto publicado y presentación |

## Cómo funcionan las variantes

1. **Asignación.** Cada alumno recibe un número del 1 al 10 el primer día. Anótalo en tu hoja de seguimiento.
2. **Celda de variante.** Al inicio de los notebooks de las sesiones 4, 5, 6, 7 y 9 va una celda con `MI_VARIANTE = ...`, el diccionario `VARIANTES` y la función `codigo_entrega`. El texto exacto lo imprime `python3 scripts/variantes.py snippet`.
3. **Solución del alumno.** Usa `p = VARIANTES[MI_VARIANTE]` y sus parámetros dentro de la consulta o del pipeline.
4. **Código de entrega.** Al terminar, el alumno ejecuta `codigo_entrega("S04", n=..., ticket=...)`, que imprime una línea como `S04|V3|n=1086|ticket=43.25`.
5. **Recolección.** El alumno pega esa línea en un formulario de Google Forms con tres campos: nombre, sesión y código. También comparte el enlace a su proyecto con permiso de lectura.
6. **Calificación.** Exportas las respuestas a un CSV con las columnas `alumno,codigo` y corres:
   `python3 scripts/variantes.py calificar --entregas entregas/entregas.csv`
   El script compara cada código contra la clave y marca `ok`, `mal` o `falta`.

### Preparar la clave (una sola vez)

La clave se calcula con el dataset real, en una máquina con los archivos en `datos/` (los mismos que descargan los notebooks):

```bash
mkdir -p datos
curl -L -o datos/viajes_2024_01.parquet https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet
curl -L -o datos/zonas.csv https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
pip install polars
python3 scripts/variantes.py clave --datos datos --salida clave/clave_variantes.csv
```

- Las carpetas `clave/` y `entregas/` están en `.gitignore`. Si compartes el repo con los alumnos, no se suben las respuestas.
- Antes del curso, comprueba una variante en la nube: resuelve la tarea de la sesión 4 con la variante 1 en un notebook y compara con `clave_variantes.csv`.

## Tabla de variantes

| Variante | Borough | Tipo de pago | Distancia mínima (millas) | Pasajeros mínimos | Distancia máxima (millas) |
|---|---|---|---|---|---|
| 1 | Manhattan | 1 (tarjeta) | 2 | 1 | 10 |
| 2 | Queens | 1 | 3 | 2 | 12 |
| 3 | Brooklyn | 1 | 1 | 1 | 15 |
| 4 | Manhattan | 2 (efectivo) | 2 | 2 | 18 |
| 5 | Bronx | 1 | 1 | 1 | 20 |
| 6 | Queens | 2 | 5 | 1 | 25 |
| 7 | Brooklyn | 2 | 1 | 2 | 30 |
| 8 | Manhattan | 1 | 5 | 3 | 35 |
| 9 | Bronx | 2 | 2 | 1 | 40 |
| 10 | Queens | 1 | 1 | 3 | 50 |

Si tienes menos de 10 alumnos, usa las variantes que necesites. Si algún día tienes más, agrega filas a `VARIANTES` en `scripts/variantes.py`.

## Tareas con variante, enunciado y solución

En todas, el alumno empieza con `p = VARIANTES[MI_VARIANTE]`. Las soluciones de abajo están verificadas contra la clave con datos de prueba. Los números reales salen de la clave.

### Sesión 4: SQL, join y agregación

- **Enunciado:** ¿cuántos viajes salieron de tu `borough` pagados con tu `tipo_pago`, y cuál fue el ticket promedio (`total_amount`, a 2 decimales)?
- **Solución:**

```python
import duckdb

p = VARIANTES[MI_VARIANTE]
n, ticket = duckdb.sql(f"""
    SELECT COUNT(*) AS n, ROUND(AVG(v.total_amount), 2) AS ticket
    FROM viajes v
    JOIN zonas z ON v.PULocationID = z.LocationID
    WHERE z.Borough = '{p["borough"]}' AND v.payment_type = {p["tipo_pago"]}
""").fetchone()

codigo_entrega("S04", n=n, ticket=ticket)
```

- **Explica (3 a 5 líneas):** ¿por qué usaste `JOIN` y qué pasaría con los viajes cuya zona es "Unknown"?

### Sesión 5: CTE y window function

- **Enunciado:** ¿cuál es la zona (`Zone`) de tu `borough` que más ingresos (`SUM(total_amount)`) generó como origen, y cuánto fue (2 decimales)? Usa una CTE y `RANK()`.
- **Solución:**

```python
zona, ingreso = duckdb.sql(f"""
    WITH ingresos AS (
        SELECT z.Zone AS zona, SUM(v.total_amount) AS ingreso
        FROM viajes v JOIN zonas z ON v.PULocationID = z.LocationID
        WHERE z.Borough = '{p["borough"]}'
        GROUP BY z.Zone
    ),
    ranking AS (
        SELECT zona, ingreso, RANK() OVER (ORDER BY ingreso DESC) AS pos
        FROM ingresos
    )
    SELECT zona, ROUND(ingreso, 2) AS ingreso FROM ranking WHERE pos = 1
""").fetchone()

codigo_entrega("S05", zona=zona, ingreso=ingreso)
```

- **Además entrega:** el diagrama del star schema de los taxis (hecho y dimensiones).
- **Explica:** ¿en qué se diferencia una tabla de hechos de una dimensión? Usa un ejemplo del dataset.

### Sesión 6: Pipeline lazy

- **Enunciado:** con `scan_parquet`, ¿cuántos viajes tienen `trip_distance` mayor que tu `distancia_min` y `passenger_count` mayor o igual que tu `pasajeros_min`, y cuál es su duración promedio en minutos (usa `dt.total_minutes()`, 2 decimales)?
- **Solución:**

```python
resultado = (
    pl.scan_parquet("datos/viajes_2024_01.parquet")
    .filter((pl.col("trip_distance") > p["distancia_min"])
            & (pl.col("passenger_count") >= p["pasajeros_min"]))
    .with_columns(
        (pl.col("tpep_dropoff_datetime") - pl.col("tpep_pickup_datetime"))
        .dt.total_minutes().alias("duracion_min")
    )
    .select(
        pl.len().alias("n"),
        pl.col("duracion_min").mean().round(2).alias("duracion"),
    )
    .collect()
)

n, duracion = resultado.row(0)
codigo_entrega("S06", n=n, duracion=duracion)
```

- **Explica:** pega el resultado de `.explain()` de tu pipeline y di en una frase qué hizo el motor antes de leer el archivo.

### Sesión 7: Análisis por hora

- **Enunciado:** en tu `borough`, ¿a qué hora del día (0 a 23, por `tpep_pickup_datetime`) hay más viajes y cuántos son? Si hay empate, gana la hora más temprana. Haz una gráfica de viajes por hora.
- **Solución:**

```python
por_hora = (
    viajes.join(zonas, left_on="PULocationID", right_on="LocationID")
    .filter(pl.col("Borough") == p["borough"])
    .with_columns(pl.col("tpep_pickup_datetime").dt.hour().alias("hora"))
    .group_by("hora")
    .agg(pl.len().alias("n"))
    .sort("hora")
)

pico = por_hora.sort(["n", "hora"], descending=[True, False]).row(0)
codigo_entrega("S07", hora=pico[0], n=pico[1])
```

- **Explica:** ¿qué tipo de join usaste y por qué?

### Sesión 9: Regla propia de validación

- **Enunciado:** agrega a tu pipeline una regla: un viaje es inválido si `trip_distance` es mayor que tu `distancia_max`. ¿Cuántos registros van a cuarentena por esa regla?
- **Solución:**

```python
invalidos_regla = viajes.filter(pl.col("trip_distance") > p["distancia_max"])
codigo_entrega("S09", n=invalidos_regla.height)
```

- **Explica:** ¿por qué se guardan los registros inválidos en cuarentena en lugar de borrarlos?

## Preguntas de explicación para las demás sesiones

- **Sesión 1:** con tus palabras, ¿qué pasa entre que un taxi termina un viaje y que ese viaje aparece en un reporte?
- **Sesión 2:** elige el error más difícil de los 3 que arreglaste y explica qué decía el traceback y cómo lo resolviste.
- **Sesión 3:** ¿cuándo elegirías CSV y cuándo Parquet? Usa tus propios números de tamaño y tiempo.
- **Sesión 8:** ¿qué ventaja tiene una tabla Delta sobre un archivo Parquet suelto?
- **Sesión 10:** ¿qué le dirías a alguien que va a heredar tu proyecto?

## Ejercicios "arregla esto"

Una celda rota por tarea es difícil de copiar y mide si saben depurar. Ideas, una para cada sesión indicada:

- **Sesión 2:** una función que no devuelve nada (`print` en lugar de `return`), un `for` con el `:` faltante y un `KeyError` en un diccionario.
- **Sesión 4:** un `GROUP BY` al que le falta una columna y un `JOIN` que duplica filas por usar la llave equivocada.
- **Sesión 6:** un pipeline al que se le olvidó `.collect()` y un filtro con una lambda en lugar de una expresión.
- **Sesión 9:** una validación que rechaza todo porque el tipo de dato no coincide con el esquema.

## Rúbrica de una tarea semanal (10 puntos)

| Criterio | Puntos | Qué se revisa |
|---|---|---|
| Resultado | 5 | El código de entrega coincide con la clave. Si el campo está mal pero el código es razonable, 2 puntos |
| Explicación | 3 | Es clara, está en sus palabras y demuestra que entiende. Una explicación copiada de la guía vale 1 |
| Reproducibilidad | 2 | Run all corre sin errores y sin celdas fuera de orden. Las celdas están en el orden en que se ejecutan |

La nota semanal promedia las tareas de las sesiones 1 a 9 y pesa el 45% de la calificación final (ver `docs/EVALUACION.md`).

## Detectar copia sin acusar a nadie

- Las variantes impiden copiar un número, pero un alumno puede pasarle su código a otro que solo cambia `MI_VARIANTE`. Por eso la explicación escrita y la pregunta oral pesan.
- Al inicio de cada sesión, pregunta en voz alta a 2 o 3 alumnos: "¿por qué elegiste ese tipo de join en tu tarea?". Con 10 alumnos rotas fácil.
- Si la explicación no coincide con el código, habla con la persona. Puede ser que se apoyó en un compañero, y eso se corrige acompañando, no castigando.
- Pide siempre el enlace al proyecto con permiso de lectura: así puedes ver el historial de versiones y el orden de ejecución.

## Operación para el instructor

- [ ] Antes del curso: calcular la clave (arriba) y comprobar una variante en la nube.
- [ ] Día 1: asignar variantes y anotarlas.
- [ ] Crear un Google Forms con nombre, sesión y código. Una sola vez para todo el curso.
- [ ] Cada semana: exportar respuestas a `entregas/entregas.csv`, correr `calificar`, pasar notas a la hoja de seguimiento.
- [ ] Revisar las explicaciones escritas y asignar los puntos de explicación y reproducibilidad.
- [ ] Devolver retroalimentación breve en la siguiente sesión.

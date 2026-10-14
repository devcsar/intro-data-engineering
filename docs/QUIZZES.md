# Quizzes del curso

Preguntas por sesión, listas para pasarse a Google Forms. Se genera con `scripts/compilar_docs.py` a partir de las guías, no se edita a mano.

## Sesión 1: Introducción a la ingeniería de datos y Deepnote como entorno de trabajo

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué hace principalmente un ingeniero de datos? | A) Predice ventas con modelos. B) Construye y mantiene los sistemas que mueven y preparan los datos. C) Diseña los logos de los reportes. D) Solo escribe consultas SQL. | B | Su trabajo es el pipeline, que los datos lleguen confiables. |
| 2 | ¿Cuál es el orden correcto de un pipeline? | A) Consumo, ingesta, fuente. B) Fuente, ingesta, transformación, almacenamiento, consumo. C) Transformación, fuente, consumo. D) Almacenamiento, fuente, ingesta. | B | Los datos nacen en la fuente y terminan siendo consumidos. |
| 3 | ¿Qué pasa con las variables cuando la máquina de Deepnote se apaga por inactividad? | A) Se guardan solas. B) Se pierden, pero el código y los archivos guardados se conservan. C) Se borra todo el proyecto. D) Se pasan a otra máquina. | B | La memoria se pierde, el disco de trabajo no. |
| 4 | ¿Para qué sirve "Run all"? | A) Para borrar el notebook. B) Para ejecutar todas las celdas de arriba hacia abajo y volver a un estado limpio y repetible. C) Para subir archivos. D) Para compartir el proyecto. | B | Garantiza orden y reproducibilidad. |
| 5 | ¿Qué es un DataFrame? | A) Un tipo de gráfica. B) Una tabla de datos en memoria con filas y columnas con nombre. C) Una cuenta de Deepnote. D) Un archivo de texto. | B | Es la estructura central para trabajar datos. |

## Sesión 2: Python esencial para datos

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué tipo de dato es `3.4`? | A) `int`. B) `float`. C) `str`. D) `bool`. | B | Tiene punto decimal, es un `float`. |
| 2 | Si `zonas = ["A", "B", "C"]`, ¿qué da `zonas[-1]`? | A) `"A"`. B) `"B"`. C) `"C"`. D) Un `IndexError`. | C | El índice `-1` es el último elemento. |
| 3 | ¿Qué hace `tipos_pago.get(9, "Otro")` si la llave 9 no existe? | A) Lanza `KeyError`. B) Devuelve `None`. C) Devuelve `"Otro"`. D) Agrega la llave 9. | C | `.get()` devuelve el valor por defecto sin fallar. |
| 4 | ¿Cuál es la diferencia entre `print` y `return` en una función? | A) Ninguna. B) `print` muestra el valor, `return` lo entrega a quien llamó la función. C) `return` solo sirve con números. D) `print` termina la función. | B | Solo lo que se devuelve con `return` se puede guardar en una variable. |
| 5 | Un traceback termina con `KeyError: 4`. ¿Qué pasó? | A) Un texto se sumó con un número. B) Falta un `:` en el código. C) Se pidió la llave 4 a un diccionario que no la tiene. D) Se dividió entre cero. | C | `KeyError` significa que la llave no existe en el diccionario. |

## Sesión 3: Fundamentos de datos y formatos (CSV, JSON, NDJSON, Parquet)

### Quiz de repaso de Python (minuto 0 a 10, sobre la sesión 2)

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué imprime `print(len(["JFK", "LGA", "EWR"]))`? | A) `2`. B) `3`. C) `"JFK"`. D) Un error. | B | `len` cuenta los elementos de la lista, que son tres. |
| 2 | ¿Qué tipo de dato es `"3"` (con comillas)? | A) `int`. B) `float`. C) `str`. D) `bool`. | C | Todo lo que va entre comillas es texto. |
| 3 | Una función no tiene `return`. ¿Qué devuelve al llamarla? | A) `0`. B) Un texto vacío. C) `None`. D) Un error. | C | Sin `return`, Python devuelve `None`. |
| 4 | ¿Qué imprime `for i in range(3): print(i)`? | A) `1 2 3`. B) `0 1 2`. C) `0 1 2 3`. D) `3`. | B | `range(3)` genera 0, 1 y 2, el final no se incluye. |
| 5 | Con `pagos = {1: "Tarjeta", 2: "Efectivo"}`, ¿qué da `pagos.get(7, "Otro")`? | A) `KeyError`. B) `None`. C) `"Otro"`. D) `7`. | C | `.get` devuelve el valor por defecto cuando la llave no existe. |

### Quiz de la sesión (cierre, pasar a Google Forms)

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Cuál de estos es un dato semiestructurado? | A) Una tabla de viajes con columnas fijas. B) Una foto. C) Un JSON donde cada evento puede traer campos distintos. D) Un audio. | C | El JSON tiene estructura, pero flexible. |
| 2 | Lees un CSV y obtienes una sola columna llamada `zona;ciudad;total`. ¿Qué falta? | A) Cambiar el encoding. B) Indicar `separator=";"`. C) Convertirlo a Parquet. D) Instalar una librería. | B | El delimitador real es punto y coma, no coma. |
| 3 | ¿Cuál es la diferencia entre JSON y NDJSON? | A) NDJSON es binario. B) JSON usa un objeto por línea. C) NDJSON tiene un objeto JSON por línea y se puede leer línea por línea. D) No hay diferencia. | C | NDJSON es JSON por líneas, ideal para logs y eventos. |
| 4 | ¿Por qué Parquet suele pesar menos que un CSV? | A) Borra los datos repetidos. B) Guarda por columnas, comprime y usa tipos en lugar de texto. C) Solo guarda las primeras filas. D) Usa más memoria RAM. | B | Las columnas se parecen entre sí y se comprimen mejor, y los números no se guardan como texto. |
| 5 | ¿Qué es el column pruning? | A) Borrar columnas del archivo original. B) Leer solo las columnas que se necesitan. C) Cambiar el tipo de una columna. D) Unir dos tablas. | B | Parquet guarda columnas por separado, así que las demás no se leen del disco. |

## Sesión 4: SQL I, consultas, joins y agregaciones

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué columna de `viajes` es una llave foránea hacia `zonas`? | A) `total_amount`. B) `PULocationID`. C) `trip_distance`. D) `payment_type`. | B | `PULocationID` guarda un `LocationID` de `zonas`. |
| 2 | ¿Cómo se pregunta correctamente por pasajeros nulos? | A) `WHERE passenger_count = NULL`. B) `WHERE passenger_count == NULL`. C) `WHERE passenger_count IS NULL`. D) `WHERE passenger_count = 0`. | C | Comparar con `NULL` usando `=` nunca da verdadero, se usa `IS NULL`. |
| 3 | Un viaje cuya zona no existe en `zonas`, ¿qué le pasa en un `INNER JOIN`? | A) Se queda con campos nulos. B) Desaparece del resultado. C) Se repite. D) Da error. | B | El `INNER JOIN` solo deja las filas con pareja. |
| 4 | ¿Para qué sirve `HAVING`? | A) Para filtrar filas antes de agrupar. B) Para ordenar. C) Para filtrar grupos después de agrupar. D) Para unir tablas. | C | `HAVING` filtra con agregaciones, `WHERE` filtra filas antes. |
| 5 | ¿Qué hace diferente `COUNT(passenger_count)` de `COUNT(*)`? | A) Nada. B) Cuenta solo las filas donde `passenger_count` no es nulo. C) Cuenta valores distintos. D) Suma los pasajeros. | B | `COUNT(columna)` ignora los nulos, `COUNT(*)` cuenta todas las filas. |

## Sesión 5: SQL II y Data Warehousing

Para pasar a Google Forms. Son dos cuestionarios: el repaso de SQL I del minuto 0 a 10, y el quiz de la sesión.

### Quiz de repaso de SQL I (minuto 0 a 10)

Se aplica al inicio de la sesión, no es parte del quiz de cierre.

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Cuál es la diferencia entre `WHERE` y `HAVING`? | A) Son iguales. B) `WHERE` filtra filas antes de agrupar, `HAVING` filtra grupos después de agregar. C) `HAVING` filtra filas y `WHERE` filtra grupos. D) `WHERE` solo funciona con texto. | B | `HAVING` puede usar funciones de agregación, `WHERE` no. |
| 2 | ¿Qué hace un `LEFT JOIN` entre `viajes` y `zonas`? | A) Solo deja los viajes que tienen zona. B) Deja todos los viajes, y pone `NULL` donde no hay zona. C) Borra viajes duplicados. D) Une las tablas por posición. | B | `LEFT JOIN` conserva todas las filas de la tabla izquierda. |
| 3 | ¿Qué falla en `SELECT Borough, COUNT(*) FROM zonas`? | A) Nada, funciona. B) Falta `GROUP BY Borough`. C) Falta `LIMIT`. D) `COUNT` no existe. | B | Si mezclas una columna normal con un agregado, la columna va en `GROUP BY`. |
| 4 | ¿Cuál es la diferencia entre `COUNT(*)` y `COUNT(passenger_count)`? | A) Ninguna. B) `COUNT(*)` cuenta filas, `COUNT(columna)` no cuenta los nulos de esa columna. C) `COUNT(*)` ignora los nulos. D) `COUNT(columna)` suma los valores. | B | Cuenta solo valores que no son nulos. |
| 5 | ¿Cómo se obtienen los 5 viajes más caros? | A) `ORDER BY total_amount ASC LIMIT 5`. B) `ORDER BY total_amount DESC LIMIT 5`. C) `LIMIT 5 ORDER BY total_amount`. D) `WHERE total_amount = 5`. | B | Se ordena de mayor a menor y se limita a 5. |

### Quiz de la sesión

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué ventaja principal tiene una CTE sobre subconsultas anidadas? | A) Es más rápida siempre. B) Le pone nombre a cada paso y la consulta se lee de arriba hacia abajo. C) Guarda los datos en disco. D) Reemplaza a los índices. | B | Es sobre todo legibilidad y reutilización dentro de una consulta. |
| 2 | Dos zonas empatan en el lugar 2 de viajes. ¿Qué diferencia hay entre `RANK()` y `ROW_NUMBER()`? | A) Ninguna. B) `RANK` les da el mismo número a las dos y salta el siguiente, `ROW_NUMBER` les da números distintos. C) `ROW_NUMBER` repite el número y `RANK` no. D) `RANK` elimina una de las filas. | B | Con empates, `RANK` da 1, 2, 2, 4, y `ROW_NUMBER` da 1, 2, 3, 4. |
| 3 | ¿Cuál es la granularidad de `fact_viajes`? | A) Una fila por zona. B) Una fila por día. C) Una fila por viaje. D) Una fila por método de pago. | C | El grano es lo que representa una fila, aquí un viaje. |
| 4 | ¿Qué describe mejor a un sistema OLAP? | A) Muchas escrituras pequeñas y rápidas. B) Consultas grandes de lectura que agregan datos históricos. C) Un sistema que solo guarda imágenes. D) Una base de datos sin tablas. | B | OLTP es la operación diaria, OLAP es el análisis. |
| 5 | En la arquitectura medallion, ¿en qué capa se guarda el dato crudo tal como llegó? | A) Gold. B) Silver. C) Bronze. D) Platinum. | C | Bronze conserva el original, silver limpia, gold agrega. |

## Sesión 6: Polars I, DataFrames y evaluación lazy

Para pasar a Google Forms.

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué diferencia hay entre `pl.read_parquet` y `pl.scan_parquet`? | A) Ninguna. B) `read_` lee todo a memoria y devuelve un DataFrame, `scan_` solo registra la lectura y devuelve un LazyFrame. C) `scan_` solo sirve para CSV. D) `read_` es lazy y `scan_` es eager. | B | `scan_` construye el plan, no lee hasta `collect()`. |
| 2 | ¿Qué es una expresión como `pl.col("total_amount") * 1.1`? | A) Una tabla con el resultado. B) La descripción de un cálculo que necesita un contexto para ejecutarse. C) Un error de sintaxis. D) Una columna nueva ya guardada. | B | La expresión es la receta, el contexto (`select`, `with_columns`) la ejecuta. |
| 3 | Quiero agregar una columna sin perder las demás, ¿qué contexto uso? | A) `select`. B) `filter`. C) `with_columns`. D) `head`. | C | `with_columns` conserva las columnas existentes y agrega o reemplaza. |
| 4 | ¿Qué hace el predicate pushdown? | A) Ordena las columnas. B) Aplica el filtro al leer el archivo, en vez de cargar todo y filtrar después. C) Elimina duplicados. D) Convierte el archivo a CSV. | B | El filtro viaja hasta el escaneo y se leen menos filas. |
| 5 | ¿Por qué en Deepnote Basic (5 GB) conviene usar lazy? | A) Porque es más bonito. B) Porque con varios meses el DataFrame completo no cabe en memoria, y lazy lee solo las columnas y filas necesarias. C) Porque Polars no tiene modo eager. D) Porque lazy no necesita `collect()`. | B | Lazy evita cargar todo y las copias intermedias. |

## Sesión 7: Polars II, transformaciones y agregaciones a escala

Para pasar a Google Forms.

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué hace un `left` join entre `viajes` y `zonas`? | A) Solo conserva los viajes que tienen zona. B) Conserva todos los viajes y pone `null` en las columnas de zona cuando no hay pareja. C) Elimina viajes duplicados. D) Une las tablas por posición. | B | `left` conserva todas las filas de la tabla izquierda. |
| 2 | ¿Para qué sirve un `anti` join? | A) Para unir tablas con llaves que se llaman distinto. B) Para devolver las filas de la tabla izquierda que NO tienen pareja en la derecha. C) Para sumar columnas. D) Para borrar nulos. | B | Sirve para encontrar huérfanos, como zonas sin viajes. |
| 3 | ¿Cuál es la diferencia entre `group_by` y `.over()`? | A) Ninguna. B) `group_by` reduce a una fila por grupo y `.over()` conserva todas las filas. C) `.over()` reduce filas y `group_by` no. D) `.over()` solo sirve con fechas. | B | `.over()` es la versión de Polars de una window function. |
| 4 | ¿Cómo se activa el motor streaming? | A) `scan_parquet(..., streaming=True)`. B) `collect(engine="streaming")`. C) `import streaming`. D) Se activa solo. | B | Se pide en el `collect()` del plan lazy. |
| 5 | ¿Qué hace el patrón `datos/viajes_2024_*.parquet` en `scan_parquet`? | A) Lee solo el primer archivo. B) Lee todos los archivos de `datos/` que empiezan con `viajes_2024_` y terminan en `.parquet` como una sola tabla lazy. C) Crea archivos nuevos. D) Da error si hay más de uno. | B | El `*` es un comodín para cualquier texto. |

## Sesión 8: Introducción a Databricks, lakehouse y notebooks

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué es un lakehouse? | A) Un lago de agua para guardar servidores. B) Una arquitectura que une la flexibilidad y bajo costo de un data lake con las tablas confiables y el SQL de un data warehouse. C) Un tipo de gráfica. D) Un lenguaje de programación. | B | Es una forma de organizar la arquitectura que combina lo mejor de ambos mundos. |
| 2 | ¿Qué significa la A de ACID? | A) Análisis. B) Atomicidad: el cambio se aplica completo o no se aplica. C) Almacenamiento. D) Acceso. | B | Si un cambio falla a la mitad, la tabla queda como estaba. |
| 3 | ¿Por qué en Free Edition no se pueden crear clusters? | A) Porque está roto. B) Porque solo ofrece compute serverless y no permite configuraciones personalizadas. C) Porque solo funciona en computadoras locales. D) Porque solo es para Windows. | B | La documentación dice que solo hay acceso a compute serverless. |
| 4 | ¿Qué pasa con los archivos si ejecutas `DROP TABLE` en una tabla gestionada? | A) Se quedan intactos. B) Se borran junto con la tabla. C) Se mueven a un volumen. D) Se convierten en CSV. | B | Databricks administra los archivos de una tabla gestionada, así que los borra. |
| 5 | ¿Para qué sirve `VERSION AS OF` en Delta? | A) Para cambiar la versión de Python. B) Para consultar la tabla como estaba en una versión anterior. C) Para cambiar de usuario. D) Para exportar a Excel. | B | Es la sintaxis de time travel, y el número de versión sale de `DESCRIBE HISTORY`. |

## Sesión 9: Pipeline ETL/ELT y calidad de datos

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué diferencia hay entre ETL y ELT? | A) Ninguna. B) En ETL se transforma antes de cargar al destino y en ELT se carga el crudo y se transforma en el destino. C) ETL es streaming y ELT es batch. D) ELT no transforma. | B | La diferencia está en dónde y cuándo ocurre la transformación. |
| 2 | ¿Qué significa que un pipeline sea idempotente? | A) Que corre muy rápido. B) Que ejecutarlo varias veces con los mismos datos deja el mismo resultado, sin duplicar. C) Que nunca falla. D) Que solo corre una vez. | B | Permite reintentar sin miedo a duplicar datos. |
| 3 | ¿Qué capa debe guardar el dato tal como llegó de la fuente? | A) Gold. B) Silver. C) Bronze. D) Ninguna. | C | Bronze conserva el original para poder repetir o investigar. |
| 4 | Un viaje fechado en diciembre dentro del archivo de enero, ¿qué dimensión de calidad rompe? | A) Unicidad. B) Oportunidad. C) Completitud. D) Ninguna. | B | La fecha no corresponde al periodo esperado. |
| 5 | ¿Para qué sirve la cuarentena (quarantine)? | A) Para borrar datos malos sin dejar rastro. B) Para guardar aparte los registros inválidos con su motivo y poder revisarlos. C) Para acelerar el pipeline. D) Para comprimir el archivo. | B | Los inválidos se conservan para investigar la causa. |

## Sesión 10: Proyecto final documentado en Deepnote

| # | Pregunta | Opciones | Correcta | Justificación |
|---|---|---|---|---|
| 1 | ¿Qué nivel de acceso de Deepnote permite que alguien lea y comente tu proyecto pero no lo edite ni lo ejecute? | A) View. B) Comment. C) Edit. D) Full access. | B | Comment permite ver y comentar sin editar ni ejecutar. |
| 2 | ¿Qué es el estado oculto? | A) Un archivo escondido. B) Variables que siguen en memoria aunque la celda que las creó ya no exista o haya cambiado. C) Un tipo de gráfica. D) Una función de Polars. | B | Hace que algo funcione hoy y falle al reiniciar. |
| 3 | ¿Cuál es la mejor prueba rápida de que un notebook es reproducible? | A) Que se vea bonito. B) Reiniciar la máquina y ejecutar Run all sin errores. C) Que tenga muchas celdas. D) Que tenga muchas gráficas. | B | Un Run all limpio demuestra que el orden y las dependencias están completos. |
| 4 | ¿Qué debe incluir una buena retroalimentación entre pares? | A) Solo críticas. B) Algo que funciona, algo que falta y una sugerencia concreta. C) Solo elogios. D) Una calificación sin explicación. | B | La retroalimentación útil es específica, equilibrada y accionable. |
| 5 | ¿Qué pasa con un bloque oculto en una app publicada de Deepnote? | A) Nadie lo puede ver. B) Sigue siendo accesible para quien tenga acceso a la app. C) Se borra. D) Se convierte en imagen. | B | Ocultar no es proteger, para esconder el código hay un interruptor aparte. |

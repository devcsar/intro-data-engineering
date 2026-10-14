# Glosario del curso

Todas las definiciones del curso, por sesión. Se genera con `scripts/compilar_docs.py` a partir de las guías, no se edita a mano.

## Sesión 1: Introducción a la ingeniería de datos y Deepnote como entorno de trabajo

- **Dato**: un hecho registrado, por ejemplo "el viaje 14 costó 18.50 dólares". Por sí solo no dice mucho. *Ejemplo:* una fila de la tabla de viajes. *Error común:* creer que dato e información son lo mismo.
- **Información**: datos puestos en contexto que ayudan a decidir. *Ejemplo:* "los viajes de los viernes por la noche dejan más propina". *Error común:* pensar que tener muchos datos ya es tener información.
- **Ingeniería de datos**: la disciplina que construye y mantiene los sistemas que mueven, limpian y guardan datos para que otras personas puedan usarlos. *Analogía:* las tuberías y el tratamiento del agua de una ciudad, nadie las ve pero sin ellas no hay agua limpia en la llave. *Error común:* creer que es lo mismo que hacer análisis.
- **Ingeniero de datos**: la persona que diseña, construye y cuida los pipelines. Su trabajo es que los datos lleguen completos, a tiempo y confiables.
- **Analista de datos**: responde preguntas del negocio con datos ya preparados, usando consultas, tableros y reportes.
- **Científico de datos**: construye modelos estadísticos o de aprendizaje automático para predecir o clasificar. *Resumen de los tres roles:* el ingeniero prepara el terreno, el analista responde preguntas, el científico predice.
- **Fuente de datos**: el lugar de donde salen los datos originales, por ejemplo una base de datos, una API, un archivo, un sensor. *Ejemplo del curso:* la página de la NYC Taxi and Limousine Commission.
- **Pipeline de datos**: una cadena automatizada de pasos que lleva datos de una fuente a un destino, transformándolos en el camino. *Analogía:* una línea de producción. *Error común:* pensar que un pipeline es un solo script.
- **Ingesta**: el paso de traer los datos desde la fuente al sistema donde se van a trabajar. *Ejemplo:* descargar el parquet con una URL.
- **Transformación**: limpiar, corregir, combinar o calcular datos para dejarlos listos para usar. *Ejemplo:* quitar viajes con distancia cero.
- **Almacenamiento**: guardar los datos en un formato y un lugar donde se puedan consultar después. *Ejemplo:* guardar el resultado en un archivo Parquet.
- **Consumo**: el uso final de los datos, por ejemplo un tablero, un reporte o un modelo.
- **Notebook**: un documento que mezcla código que se ejecuta, texto explicativo y los resultados, todo en la misma página. *Analogía:* un cuaderno de laboratorio. *Error común:* creer que el notebook es solo un editor de código.
- **Celda**: cada bloque de un notebook. Puede ser de código o de texto (Markdown). Se ejecuta con Shift + Enter.
- **Kernel o máquina**: el programa (y la computadora en la nube) que ejecuta tu código y recuerda las variables mientras está encendido. En Deepnote es la "máquina" del proyecto.
- **Workspace**: el espacio de trabajo de una cuenta o equipo en Deepnote, donde viven los proyectos.
- **Proyecto**: un contenedor dentro del workspace que agrupa notebooks, archivos y configuración. *Error común:* confundir proyecto con notebook, un proyecto puede tener varios notebooks.
- **Run all**: ejecutar todas las celdas del notebook de arriba hacia abajo. Es el ritual del curso al empezar cada sesión.
- **Orden de ejecución**: el orden en que se ejecutaron las celdas, que puede no ser el orden en que aparecen en la página. *Error común:* ejecutar celdas fuera de orden y obtener resultados que no se pueden repetir.
- **Estado oculto**: variables que siguen vivas en la memoria aunque ya borraste o cambiaste la celda que las creó. Causa resultados que "funcionan en mi máquina" y no se repiten.
- **Reproducibilidad**: que otra persona (o tú mañana) pueda ejecutar el notebook desde cero y obtener el mismo resultado. Run all es la prueba más simple.
- **Apagado por inactividad**: la máquina de Deepnote Free se apaga tras 15 minutos sin actividad. Las variables se pierden, el código y los archivos guardados en la carpeta de trabajo se conservan.
- **Archivo Parquet**: formato de archivo para datos en columnas, comprimido y con el esquema guardado dentro. Se ve a fondo en la sesión 3, hoy solo lo leemos.
- **DataFrame**: una tabla de datos en memoria, con filas y columnas con nombre. En el curso se usa el de Polars.
- **Esquema (schema)**: la lista de columnas de una tabla con su tipo de dato. *Ejemplo:* `passenger_count` es número, `tpep_pickup_datetime` es fecha y hora.
- **URL de descarga**: la dirección web de un archivo. Descargar por URL evita subir archivos pesados a mano.

## Sesión 2: Python esencial para datos

- **Variable**: un nombre que apunta a un valor guardado en memoria. Se crea con `=`. *Analogía:* una etiqueta pegada a una caja, la caja tiene el valor y la etiqueta es el nombre. *Error común:* creer que `=` significa "es igual a" como en matemáticas, en Python significa "guarda este valor con este nombre".
- **Tipo de dato**: la clase de valor que guarda una variable, de ella depende lo que se puede hacer con el valor. *Ejemplo:* un número se puede sumar, un texto se puede poner en mayúsculas. *Error común:* intentar sumar un texto con un número.
- **`int` (entero)**: número sin decimales, por ejemplo `3` pasajeros. *Error común:* pensar que `3.0` es un entero, es un `float`.
- **`float` (decimal)**: número con decimales, por ejemplo `3.4` millas. *Ejemplo:* `trip_distance` y `fare_amount` son decimales. *Error común:* esperar que `0.1 + 0.2` dé exactamente `0.3`, los decimales en computadora tienen pequeños errores de redondeo.
- **`str` (cadena de texto)**: texto entre comillas, por ejemplo `"Midtown Center"`. *Error común:* olvidar las comillas y que Python crea que es un nombre de variable.
- **`bool` (booleano)**: solo puede ser `True` o `False`. Se escribe con mayúscula inicial. *Ejemplo:* `pago_con_tarjeta = True`. *Error común:* escribir `true` en minúscula, Python marca `NameError`.
- **`None`**: el valor que representa "no hay nada aquí". *Ejemplo:* una función sin `return` devuelve `None`. *Error común:* confundirlo con `0` o con un texto vacío.
- **`type()`**: función que dice de qué tipo es un valor. *Ejemplo:* `type(3.4)` da `float`. Sirve mucho para depurar.
- **Conversión de tipos (casting)**: cambiar un valor de un tipo a otro con `int()`, `float()`, `str()`. *Ejemplo:* `int("5")` da `5`. *Error común:* `int("3.5")` falla con `ValueError`, primero hay que hacer `float("3.5")`.
- **f-string**: un texto con una `f` antes de las comillas que permite meter variables entre llaves. *Ejemplo:* `f"Viaje de {distancia} millas"`. *Error común:* olvidar la `f` y que se imprima la llave tal cual.
- **Comentario**: texto después de `#` que Python ignora, sirve para explicar el código a quien lo lea. *Error común:* comentar lo obvio y no comentar el porqué.
- **Operador aritmético**: símbolos para calcular: `+`, `-`, `*`, `/`, `//` (división entera), `%` (residuo) y `**` (potencia). *Ejemplo:* `7 // 2` da `3` y `7 % 2` da `1`. *Error común:* creer que `/` devuelve un entero, siempre devuelve `float`.
- **Operador de comparación**: compara dos valores y da un `bool`: `==`, `!=`, `<`, `<=`, `>`, `>=`. *Error común:* usar `=` en lugar de `==` dentro de un `if`.
- **Operador lógico**: combina condiciones: `and`, `or`, `not`. *Ejemplo:* `distancia > 0 and total > 0`. *Error común:* escribir `x > 1 and < 5` en lugar de `x > 1 and x < 5`.
- **Operador `in`**: pregunta si un valor está dentro de una lista, un texto o las llaves de un diccionario. *Ejemplo:* `"Airport" in "JFK Airport"` da `True`.
- **Lista (`list`)**: una colección ordenada de valores entre corchetes. *Ejemplo:* `zonas = ["JFK Airport", "Midtown Center"]`. *Error común:* creer que una lista solo puede tener un tipo de valor, puede mezclar, pero en datos conviene que sean del mismo tipo.
- **Índice**: la posición de un elemento en una lista, empieza en `0`. El `-1` es el último. *Error común:* pedir el índice igual a la longitud de la lista, da `IndexError`.
- **Rebanada (slicing)**: tomar un pedazo de una lista con `lista[inicio:fin]`, el fin no se incluye. *Ejemplo:* `zonas[0:2]` da los dos primeros. *Error común:* esperar que incluya el elemento del final.
- **Mutable**: un objeto que se puede cambiar después de crearlo. Las listas y diccionarios lo son, los textos y números no. *Error común:* asignar una lista a otra variable (`b = a`) y creer que es una copia, las dos apuntan a la misma lista.
- **Métodos de lista**: funciones que pertenecen a la lista, como `append` (agregar al final), `remove` (quitar) y `sort` (ordenar). Se llaman con punto. *Error común:* hacer `lista = lista.append(x)`, `append` devuelve `None` y la lista se pierde.
- **`len()`**: devuelve cuántos elementos tiene una lista, un texto o un diccionario.
- **Diccionario (`dict`)**: una colección de pares llave y valor entre llaves. *Analogía:* un directorio telefónico, buscas por nombre y te da el número. *Ejemplo:* `tipos_pago = {1: "Tarjeta de crédito", 2: "Efectivo"}`. *Error común:* pedir una llave que no existe con corchetes y recibir `KeyError`.
- **Llave y valor (key y value)**: la llave es lo que se busca (única en el diccionario), el valor es lo que se obtiene. *Ejemplo:* el código `2` es la llave y `"Efectivo"` es el valor.
- **`.get()`**: forma segura de leer un diccionario, si la llave no existe devuelve un valor por defecto en lugar de fallar. *Ejemplo:* `tipos_pago.get(9, "Otro")`.
- **`.items()`, `.keys()`, `.values()`**: métodos para recorrer las parejas, las llaves o los valores de un diccionario.
- **Condicional (`if`, `elif`, `else`)**: bloque de código que solo se ejecuta si se cumple una condición. *Ejemplo:* si la distancia es menor a 1 milla, el viaje es "corto". *Error común:* olvidar los dos puntos al final de la línea.
- **Indentación**: los espacios al inicio de una línea que le dicen a Python qué código pertenece a un bloque. Se usan 4 espacios. *Error común:* mezclar niveles y recibir `IndentationError`.
- **Bloque de código**: las líneas indentadas debajo de un `if`, `for` o `def`.
- **Ciclo `for`**: repite un bloque por cada elemento de algo que se pueda recorrer. *Analogía:* revisar una pila de tickets uno por uno. *Error común:* modificar una lista mientras se recorre.
- **Iterable**: cualquier cosa que un `for` puede recorrer: listas, textos, diccionarios, `range`.
- **`range()`**: genera una secuencia de números. `range(3)` da `0, 1, 2`. *Error común:* esperar que incluya el número final.
- **`enumerate()`**: recorre una lista dando el índice y el elemento a la vez.
- **Acumulador**: una variable que se va actualizando dentro de un ciclo para sumar, contar o juntar resultados. *Ejemplo:* `total = 0` y luego `total += d` en cada vuelta. *Error común:* inicializarlo dentro del ciclo y que se reinicie en cada vuelta.
- **Comprensión de listas (list comprehension)**: forma corta de crear una lista a partir de otra. *Ejemplo:* `[d * 1.6 for d in distancias]`. Se menciona como atajo, no es obligatoria.
- **Función**: un bloque de código con nombre que se puede reutilizar. Se crea con `def`. *Analogía:* una receta que puedes usar cuando quieras. *Error común:* definir la función y nunca llamarla.
- **Parámetro y argumento**: el parámetro es el nombre que aparece en la definición (`def f(distancia)`), el argumento es el valor que se pasa al llamarla (`f(3.4)`).
- **Valor por defecto**: valor que toma un parámetro si no se le pasa nada. *Ejemplo:* `def f(distancia, umbral=5)`.
- **`return`**: lo que la función devuelve a quien la llamó. *Error común:* usar `print` en lugar de `return`, la función muestra el valor pero no lo entrega y no se puede guardar en una variable.
- **Alcance (scope)**: dónde existe una variable. Una variable creada dentro de una función no existe fuera de ella. *Error común:* querer usar fuera de la función una variable que se creó adentro.
- **Módulo**: un archivo de Python con funciones listas para usar. Se trae con `import`. *Ejemplo:* `import math`, `from pathlib import Path`. *Error común:* usar el módulo sin importarlo y recibir `NameError`.
- **Librería o paquete**: un conjunto de módulos que alguien más escribió. *Ejemplo:* Polars. *Error común:* confundir el nombre del paquete que se instala con el nombre que se importa.
- **Alias de importación**: un apodo corto, como `import polars as pl`.
- **Excepción**: el aviso que Python lanza cuando algo sale mal y el programa se detiene. *Error común:* verla como algo malo, es información útil.
- **Traceback**: el reporte que Python imprime cuando hay una excepción, con la ruta de llamadas que llevó al error. Se lee de abajo hacia arriba: la última línea dice qué pasó, las de arriba dicen dónde. *Error común:* asustarse con el bloque rojo y no leer la última línea.
- **Tipos de error frecuentes**:
  - `SyntaxError`: el código está mal escrito (falta un `:` o un paréntesis).
  - `IndentationError`: la indentación está mal.
  - `NameError`: usas un nombre que no existe (typo o no se ejecutó la celda que lo crea).
  - `TypeError`: operación entre tipos que no se llevan, por ejemplo texto más número.
  - `ValueError`: el tipo es correcto pero el valor no sirve, por ejemplo `int("hola")`.
  - `KeyError`: la llave no está en el diccionario.
  - `IndexError`: el índice se sale de la lista.
  - `ZeroDivisionError`: dividir entre cero.
  - `ModuleNotFoundError`: el módulo no está instalado o está mal escrito.
- **Depurar (debug)**: encontrar y corregir la causa de un error. *Método del curso:* leer la última línea del traceback, ubicar la línea, imprimir los valores con `print` y `type`.

## Sesión 3: Fundamentos de datos y formatos (CSV, JSON, NDJSON, Parquet)

- **Dato estructurado**: dato organizado en filas y columnas fijas, con tipos definidos. *Ejemplo:* la tabla de viajes de taxi o la tabla de zonas. *Error común:* creer que "estructurado" significa que está en una base de datos, un CSV bien hecho también es estructurado.
- **Dato semiestructurado**: dato que tiene una estructura, pero flexible: cada registro puede traer campos distintos o anidados. *Ejemplo:* un JSON de una app donde unos eventos traen `ubicacion` y otros no. *Error común:* creer que no tiene esquema, lo tiene, pero no es rígido.
- **Dato no estructurado**: dato sin forma de tabla ni campos definidos. *Ejemplo:* un PDF, una foto, un audio, el texto libre de una reseña. *Error común:* pensar que no se puede analizar, solo hay que extraer estructura primero.
- **Esquema (schema)**: la descripción de una tabla, con el nombre y el tipo de cada columna. *Analogía:* los encabezados y las reglas de un formulario. *Ejemplo:* `passenger_count` es número, `tpep_pickup_datetime` es fecha y hora.
- **Tipo de dato (tipado)**: la clase de valor de cada columna (entero, decimal, texto, fecha y hora, booleano). *Error común:* creer que "123" y 123 son lo mismo, uno es texto y el otro número.
- **Inferencia de esquema**: cuando la herramienta adivina los tipos mirando los valores, como hace `read_csv`. *Error común:* confiar ciegamente, si las primeras filas son enteros y una fila más abajo trae texto, la inferencia falla o se equivoca.
- **Esquema declarado (explícito)**: cuando tú dices el tipo de cada columna. Es más seguro y más repetible. *Ejemplo:* `schema_overrides={"id": pl.String}`.
- **Metadatos**: datos sobre los datos: nombres de columnas, tipos, cantidad de filas, fecha de creación, compresión. *Analogía:* la ficha técnica de un producto. *Error común:* creer que un CSV trae metadatos, solo trae texto.
- **Formato de archivo**: la forma acordada de escribir datos en un archivo para que otro programa pueda leerlo. *Ejemplo:* CSV, JSON, Parquet.
- **Formato de texto y formato binario**: un archivo de texto se puede abrir con un editor y leer a simple vista (CSV, JSON), uno binario no (Parquet). *Error común:* intentar abrir un Parquet en Excel o en un bloc de notas.
- **CSV (valores separados por comas)**: archivo de texto donde cada línea es una fila y las columnas se separan con un carácter. *Ejemplo:* `taxi_zone_lookup.csv`. *Error común:* creer que el CSV tiene tipos, todo es texto y la herramienta adivina.
- **Delimitador (separador)**: el carácter que separa las columnas: coma, punto y coma, tabulador, barra vertical. *Ejemplo:* en muchos países de habla hispana Excel guarda con punto y coma, porque la coma se usa para los decimales. *Error común:* leer con coma un archivo con punto y coma y obtener una sola columna.
- **Encabezado (header)**: la primera fila con los nombres de las columnas. *Error común:* no avisar que no hay encabezado y perder la primera fila de datos como nombre de columna.
- **Comillas y escape**: las comillas protegen un texto que contiene el delimitador. *Ejemplo:* `"Calle Reforma, 10"` es una sola celda aunque tenga una coma.
- **Valor nulo (null)**: la ausencia de un dato. En CSV suele ser una celda vacía. *Error común:* confundir nulo con cero o con texto vacío.
- **Encoding (codificación de caracteres)**: la tabla que convierte bytes en letras. UTF-8 es el estándar actual, Latin-1 (ISO-8859-1) es común en archivos viejos. *Ejemplo:* si se lee un archivo Latin-1 como UTF-8, "Coyoacán" sale mal o falla. *Error común:* ignorar el encoding hasta que aparecen símbolos raros.
- **Separador decimal**: en México se usa el punto (`12.50`), en otros países la coma (`12,50`). *Error común:* leer `12,50` y obtener texto en lugar de número.
- **JSON**: formato de texto para datos con llaves y valores, que permite anidar objetos y listas. *Ejemplo:* `{"id": 1, "zona": "JFK", "tags": ["aeropuerto"]}`. *Error común:* creer que un archivo JSON grande se puede leer por partes, un arreglo JSON completo se tiene que leer entero.
- **Anidamiento**: un campo que contiene otros campos o listas. *Ejemplo:* un viaje con un campo `pago` que trae `tipo` e `importe`.
- **NDJSON (JSON por líneas, JSON Lines)**: un archivo con un objeto JSON por línea, sin corchetes ni comas entre líneas. *Analogía:* un CSV donde cada línea es un JSON. *Error común:* confundirlo con JSON, un NDJSON completo no es un JSON válido y viceversa. Se usa mucho para logs y flujos de eventos porque se puede leer línea por línea.
- **Serialización**: convertir datos en memoria a texto o bytes que se puedan guardar o enviar. *Ejemplo:* `write_csv` y `write_ndjson`.
- **Almacenamiento por filas**: los valores de una fila se guardan juntos. Bueno para leer o escribir un registro completo (por ejemplo, una app que guarda un viaje). *Ejemplo:* CSV.
- **Almacenamiento columnar**: los valores de una columna se guardan juntos. Bueno para análisis, que casi siempre usa pocas columnas de muchas filas. *Analogía:* en lugar de una pila de fichas con todos los datos de cada persona, una lista con solo las edades y otra con solo los nombres. *Ejemplo:* Parquet.
- **Parquet (Apache Parquet)**: formato binario columnar, comprimido, con el esquema guardado en el archivo. *Error común:* creerlo "mejor" en todos los casos, para intercambiar con personas en Excel el CSV sigue siendo útil.
- **Row group (grupo de filas)**: un bloque de filas dentro de un archivo Parquet, con las columnas guardadas por separado y estadísticas propias. Permite leer solo los bloques que importan.
- **Compresión**: reducir el tamaño de los datos guardándolos de forma más compacta, sin perder información. *Ejemplo:* los valores repetidos, como `payment_type`, se comprimen muy bien en una columna. *Error común:* creer que comprimir siempre hace más lenta la lectura, muchas veces es más rápido porque se leen menos bytes del disco.
- **Códec de compresión**: el algoritmo concreto: `snappy` (rápido), `zstd` (buen balance, es el que usa Polars por defecto), `gzip` (más lento, común). *Error común:* creer que hay un códec perfecto, depende de velocidad contra tamaño.
- **Codificación por diccionario**: forma de comprimir una columna con pocos valores distintos, guardando una lista de valores únicos y referencias a ella.
- **Esquema embebido**: el esquema va dentro del archivo Parquet, así que al leerlo los tipos son los correctos sin adivinar. *Ejemplo:* las fechas siguen siendo fechas. *Error común:* creer que el CSV también los conserva, un CSV de vuelta llega con fechas como texto.
- **Column pruning (poda de columnas)**: leer solo las columnas que necesitas. Como Parquet guarda columnas por separado, las demás ni se leen del disco. *Ejemplo:* `columns=["PULocationID", "total_amount"]`. *Error común:* leer las 19 columnas y luego descartar 17.
- **Predicate pushdown (empuje de filtros)**: aplicar el filtro lo más cerca posible de la lectura, usando las estadísticas mínimo y máximo de cada row group para saltarse bloques completos. *Ejemplo:* si un bloque tiene `total_amount` máximo de 50 y filtras por mayores a 100, ese bloque ni se lee. *Error común:* creer que el filtro se hace siempre después de leer todo.
- **Apache Arrow**: formato de datos en memoria, columnar, que comparten muchas herramientas (Polars, DuckDB, pandas) para intercambiar datos sin copiarlos ni convertirlos. *Analogía:* un idioma común entre herramientas. *Error común:* confundirlo con Parquet, Arrow es en memoria, Parquet es en disco.
- **Delta Lake**: un formato de tabla que se apoya en archivos Parquet y agrega un registro de transacciones. Da cambios seguros (ACID), historial y viaje en el tiempo. Se ve a fondo en la sesión 8.
- **Apache Iceberg**: otro formato de tabla abierto, con la misma idea que Delta (archivos Parquet más metadatos de tabla). *Error común:* creer que Delta e Iceberg son formatos de archivo nuevos, son una capa de gestión sobre archivos Parquet.
- **ACID**: conjunto de garantías para que una escritura se complete entera o no se haga, sin dejar tablas a medias. Solo se menciona hoy.
- **Benchmark (comparación medida)**: medir tiempos y tamaños de forma repetible para comparar opciones. *Error común:* medir una sola vez, la primera lectura puede ser más lenta por la memoria caché del sistema, por eso se repite.
- **Megabyte (MB)**: unidad de tamaño. En la sesión se usa 1 MB igual a 1,048,576 bytes para medir los archivos.

## Sesión 4: SQL I, consultas, joins y agregaciones

- **Base de datos relacional**: un conjunto de tablas relacionadas entre sí por llaves. *Analogía:* varias hojas de Excel donde una columna de una hoja apunta a otra hoja. *Error común:* creer que una base de datos es un solo archivo grande, son varias tablas conectadas.
- **Tabla**: un conjunto de datos con filas y columnas. *Ejemplo:* `viajes` y `zonas`. En el curso, cada DataFrame se puede tratar como una tabla.
- **Fila (registro)**: un elemento de la tabla. *Ejemplo:* un viaje de taxi.
- **Columna (campo, atributo)**: una propiedad de cada fila, con nombre y tipo. *Ejemplo:* `total_amount`.
- **Llave primaria (primary key)**: la columna (o columnas) que identifica de forma única cada fila. No se repite y no es nula. *Ejemplo:* `LocationID` en `zonas`. *Error común:* creer que `viajes` tiene llave primaria, la tabla de viajes no trae un identificador de viaje, hay que tener cuidado al contar duplicados.
- **Llave foránea (foreign key)**: una columna que apunta a la llave primaria de otra tabla. *Ejemplo:* `PULocationID` y `DOLocationID` en `viajes` apuntan a `LocationID` en `zonas`. *Error común:* creer que la base de datos siempre verifica que la llave exista, en archivos y DataFrames nadie lo revisa, por eso aparecen filas huérfanas.
- **Tabla de hechos y tabla de dimensión**: el hecho guarda eventos que ocurren (viajes), la dimensión guarda descripciones (zonas). Se ve a fondo en la sesión 5, hoy solo se usa la idea.
- **Relación uno a muchos**: una fila de la dimensión se relaciona con muchas filas del hecho. *Ejemplo:* una zona tiene miles de viajes.
- **SQL**: lenguaje para consultar y manipular datos en tablas. Se escribe describiendo qué quieres, no cómo calcularlo. *Analogía:* pedir un platillo al mesero sin entrar a la cocina. *Error común:* creer que SQL es solo para bases de datos grandes, también funciona sobre DataFrames y archivos.
- **Consulta (query)**: una instrucción SQL que pide datos. Casi siempre empieza con `SELECT`.
- **DuckDB**: motor de bases de datos analítico que corre dentro de Python, sin servidor. Puede consultar archivos (Parquet, CSV) y DataFrames directamente. *Error común:* confundirlo con una base de datos que hay que instalar y administrar.
- **Bloque SQL de Deepnote**: un tipo de celda que ejecuta SQL. Con la integración de DataFrames (`deepnote-dataframe-sql`) puedes escribir `FROM viajes` y Deepnote entiende que `viajes` es la variable DataFrame del notebook. El resultado se guarda en una variable de salida. *Error común:* creer que hay que conectar una base de datos, la integración de DataFrames no necesita configuración.
- **Variable de salida**: el nombre de la variable donde un bloque SQL de Deepnote guarda su resultado (por ejemplo `df_top`). Se puede usar luego en celdas de código.
- **`duckdb.sql()`**: la forma de correr la misma consulta desde una celda de Python. DuckDB busca variables DataFrame con el nombre de la tabla. *Error común:* poner el nombre de la variable con comillas dentro de `FROM`.
- **`SELECT`**: la parte de la consulta que dice qué columnas o expresiones quieres ver. *Error común:* usar `SELECT *` en tablas grandes y por costumbre, trae todas las columnas.
- **`FROM`**: dice de qué tabla vienen los datos.
- **Alias (`AS`)**: un nombre nuevo para una columna, un cálculo o una tabla. *Ejemplo:* `trip_distance * 1.60934 AS kilometros`, o `viajes AS v`. *Error común:* usar el alias de una columna dentro del `WHERE` de la misma consulta, no existe todavía en ese momento.
- **Expresión**: un cálculo dentro de la consulta. *Ejemplo:* `total_amount - tip_amount`.
- **`WHERE`**: filtra filas antes de agrupar. *Ejemplo:* `WHERE trip_distance > 0`.
- **Operadores de comparación y lógicos**: `=` (igual, un solo signo), `<>` o `!=` (distinto), `<`, `<=`, `>`, `>=`, `AND`, `OR`, `NOT`, `BETWEEN a AND b` (incluye los extremos), `IN (1, 2)`, `LIKE '%Airport%'` (el `%` es cualquier cantidad de caracteres). *Error común:* usar `==` como en Python, en SQL es `=`.
- **`ORDER BY`**: ordena el resultado. `ASC` de menor a mayor (por defecto), `DESC` de mayor a menor. *Error común:* esperar un orden sin escribir `ORDER BY`, sin él el orden no está garantizado.
- **`LIMIT`**: limita cuántas filas se devuelven. *Error común:* usar `LIMIT` sin `ORDER BY` y creer que son "los primeros" o "los mejores".
- **`DISTINCT`**: quita filas repetidas del resultado. *Ejemplo:* los valores distintos de `payment_type`.
- **`NULL` (nulo)**: ausencia de un valor. No es cero ni texto vacío. *Error común:* escribir `= NULL`, nunca da verdadero, se usa `IS NULL`.
- **`IS NULL` e `IS NOT NULL`**: la forma correcta de preguntar si un valor falta.
- **Lógica de tres valores**: en SQL una comparación puede dar verdadero, falso o desconocido (cuando hay un nulo). `WHERE` solo deja pasar las verdaderas. *Ejemplo:* `NULL > 2` no es verdadero ni falso, es desconocido, y esa fila no aparece.
- **`COALESCE(a, b)`**: devuelve el primer valor que no sea nulo. *Ejemplo:* `COALESCE(passenger_count, 1)`. *Error común:* rellenar nulos sin pensar, se inventa información.
- **`JOIN`**: unir filas de dos tablas usando una condición. *Analogía:* buscar en el directorio el nombre que corresponde a cada código.
- **`ON`**: la condición de la unión. *Ejemplo:* `ON v.PULocationID = z.LocationID`.
- **`INNER JOIN`**: devuelve solo las filas que tienen pareja en las dos tablas. *Error común:* usarlo sin darse cuenta de que descarta filas sin pareja.
- **`LEFT JOIN`**: devuelve todas las filas de la tabla izquierda, y los datos de la derecha si hay pareja (si no, nulos). *Error común:* creer que `LEFT JOIN` da el mismo resultado que `INNER JOIN`, solo coinciden si todas las filas tienen pareja.
- **Fila huérfana**: una fila del hecho cuya llave foránea no existe en la dimensión. *Ejemplo:* un viaje cuyo `PULocationID` no aparece en `zonas`. Se detecta con `LEFT JOIN ... WHERE dimension.llave IS NULL`.
- **Zona "Unknown"**: en `zonas`, `LocationID` 264 y 265 son zonas desconocidas. Los viajes sí tienen pareja, pero la zona no dice nada útil. Es un caso de calidad de datos distinto al de la fila huérfana.
- **Multiplicación de filas (fan-out)**: cuando la tabla de la derecha tiene la llave repetida, cada fila de la izquierda se repite varias veces y los totales salen inflados. *Error común:* no comparar el conteo antes y después del join.
- **Función de agregación**: calcula un solo valor a partir de muchas filas. *Ejemplos:* `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- **`COUNT(*)`, `COUNT(columna)` y `COUNT(DISTINCT columna)`**: el primero cuenta filas, el segundo cuenta valores no nulos de esa columna, el tercero cuenta valores distintos no nulos. *Error común:* creer que `COUNT(columna)` cuenta filas, ignora los nulos.
- **`SUM`, `AVG`, `MIN`, `MAX`**: suma, promedio, mínimo y máximo. Ignoran los nulos. *Error común:* esperar que un promedio cuente los nulos como cero.
- **`GROUP BY`**: agrupa filas con el mismo valor en una o más columnas, y las funciones de agregación se calculan por grupo. *Analogía:* separar los tickets en pilas por tipo de pago y contar cada pila. *Error común:* poner en el `SELECT` una columna que no está en `GROUP BY` ni dentro de una agregación, da error.
- **`HAVING`**: filtra grupos después de agrupar, usando agregaciones. *Error común:* usar `WHERE COUNT(*) > 10`, no se puede, es `HAVING COUNT(*) > 10`.
- **Orden lógico de ejecución**: aunque se escribe `SELECT` primero, el motor evalúa en este orden: `FROM`, `JOIN`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`, `LIMIT`. Explica por qué `WHERE` no ve los alias del `SELECT` y por qué `HAVING` sí ve las agregaciones.
- **Comentario SQL**: texto después de `--` en una línea, el motor lo ignora.
- **Cadena de texto en SQL**: se escribe con comillas simples (`'Airport'`). Las comillas dobles son para nombres de columnas.
- **`ROUND(x, n)`**: redondea a `n` decimales.
- **`UNION ALL`**: junta los resultados de dos consultas con las mismas columnas, una debajo de otra. Se usa hoy una vez para comparar conteos.

## Sesión 5: SQL II y Data Warehousing

### SQL avanzado (5.1 a 5.4)

- **Subconsulta (5.1)**: una consulta `SELECT` escrita dentro de otra, entre paréntesis. Puede ir en `WHERE` (para comparar contra un valor calculado), en `FROM` (como si fuera una tabla temporal) o en `SELECT`. *Ejemplo:* los viajes con `total_amount` mayor al promedio, donde el promedio sale de otra consulta. *Error común:* anidar cuatro subconsultas y no poder leerlas después, para eso existen las CTEs.
- **Subconsulta en `FROM`**: la subconsulta se usa como tabla y necesita un alias. *Ejemplo:* calcular viajes por zona y luego promediar esos conteos. *Error común:* olvidar el alias.
- **Subconsulta con `IN`**: devuelve una lista de valores contra la que se compara. *Ejemplo:* los viajes cuyo `PULocationID` está en las zonas de Manhattan. *Error común:* usar `=` cuando la subconsulta devuelve varias filas.
- **CTE (5.2)**: Common Table Expression, un resultado con nombre que defines con `WITH nombre AS (...)` antes de la consulta principal. Se lee de arriba hacia abajo, como una receta. *Analogía:* preparar ingredientes por separado antes de cocinar el platillo. *Error común:* creer que la CTE se guarda en la base de datos, solo existe durante esa consulta.
- **Varias CTEs encadenadas**: se separan con coma y cada una puede usar las anteriores. Un solo `WITH`, no uno por CTE. *Error común:* repetir la palabra `WITH` o dejar una coma sobrante antes del `SELECT` final.
- **`CASE WHEN` (5.3)**: la forma de poner condiciones "si pasa esto, entonces aquello" dentro de una consulta, para crear categorías. Termina con `END`. *Ejemplo:* clasificar viajes en corto, medio o largo según la distancia. *Error común:* olvidar `ELSE`, las filas que no cumplen ninguna condición quedan en `NULL`.
- **Window function (5.4)**: una función que calcula sobre un grupo de filas relacionadas, pero sin juntarlas en una sola fila como hace `GROUP BY`. Cada fila conserva su detalle y recibe un valor extra. *Analogía:* en una lista de clase, ponerle a cada alumno su lugar dentro del grupo sin quitar a nadie de la lista. *Error común:* creer que reemplaza a `GROUP BY`, hacen cosas distintas.
- **`OVER`**: la cláusula que convierte una función en window function y define la "ventana". Dentro llevan `PARTITION BY` y `ORDER BY`.
- **`PARTITION BY`**: divide las filas en grupos independientes para la ventana. *Ejemplo:* un ranking que reinicia en cada `Borough`. *Error común:* confundirlo con `GROUP BY`, `PARTITION BY` no colapsa filas.
- **`ROW_NUMBER`**: numera las filas 1, 2, 3, sin repetir nunca el número, aunque haya empates. *Error común:* usarlo cuando se quiere que los empates compartan lugar.
- **`RANK`**: numera por orden, y los empates comparten número y dejan huecos después (1, 2, 2, 4). *Error común:* esperar que no haya huecos.
- **`SUM OVER` (suma acumulada)**: una suma que se va acumulando fila a fila según el orden de la ventana. *Ejemplo:* ingreso acumulado día a día. *Error común:* olvidar el `ORDER BY` dentro de `OVER`, entonces suma todo el grupo en cada fila.
- **`QUALIFY`**: un filtro especial de DuckDB que se aplica después de calcular las window functions. Es un atajo, en otras bases de datos hay que usar una CTE. *Error común:* intentar poner una window function en `WHERE`, no se puede.

### Data warehousing (5.5 a 5.12)

- **OLTP (5.5)**: Online Transaction Processing, bases de datos que atienden la operación diaria con muchas escrituras pequeñas y rápidas. *Ejemplo:* el sistema que registra cada viaje de taxi cuando termina. *Error común:* hacer reportes pesados directamente sobre la base operativa y volverla lenta.
- **OLAP (5.5)**: Online Analytical Processing, sistemas hechos para leer y agregar muchos datos y responder preguntas. *Ejemplo:* "¿cuánto se ganó por zona cada hora del mes?". *Error común:* creer que son dos productos distintos, son dos usos, y a veces un mismo motor hace ambos.
- **Data warehouse (almacén de datos)**: una base de datos organizada para análisis, que junta datos de varias fuentes con un modelo pensado para consultarse rápido. *Analogía:* la bodega central de una cadena de tiendas, donde todo está ordenado para surtir.
- **Normalización (5.6)**: separar los datos en tablas pequeñas para no repetir información. *Ejemplo:* guardar el nombre de la zona una sola vez en `zonas` y en `viajes` solo su `LocationID`. *Error común:* sobre-normalizar un almacén de datos, se llenan las consultas de joins.
- **Desnormalización (5.6)**: juntar tablas y repetir datos a propósito para que las consultas sean más simples y rápidas. *Ejemplo:* una tabla de viajes que ya trae `Borough` y `Zone` escritos en cada fila. *Error común:* creer que repetir datos siempre es malo, en análisis es una decisión de diseño.
- **Llave primaria y llave foránea**: la primaria identifica una fila de forma única (`LocationID` en `zonas`), la foránea es la columna de otra tabla que apunta a ella (`PULocationID` en `viajes`). *Error común:* pensar que la llave foránea debe ser única.
- **Tabla de hechos (5.7)**: la tabla central que guarda los eventos que se miden, con números (medidas) y llaves hacia las dimensiones. *Ejemplo:* `fact_viajes`, una fila por viaje. *Error común:* meter ahí descripciones largas, eso va en las dimensiones.
- **Medida**: el número que se suma, promedia o cuenta en una tabla de hechos. *Ejemplo:* `total_amount`, `trip_distance`, `tip_amount`.
- **Granularidad o grano (5.7)**: lo que representa exactamente una fila de la tabla de hechos. Se decide primero, antes que todo lo demás. *Ejemplo:* "una fila por viaje". *Error común:* mezclar granos en la misma tabla (viajes y totales por día juntos), los números dejan de cuadrar.
- **Tabla de dimensión (5.8)**: una tabla de descripción que da contexto a los hechos: quién, dónde, cuándo, cómo. *Ejemplo:* `dim_zona`, `dim_tiempo`, `dim_pago`. *Error común:* confundirla con un hecho, la dimensión describe, el hecho mide.
- **Dimensión de rol**: la misma dimensión usada en dos papeles dentro de un hecho. *Ejemplo:* `dim_zona` sirve como zona de origen y como zona de destino, se une dos veces con alias distintos.
- **Llave sustituta (surrogate key)**: un identificador inventado por nosotros que reemplaza a la llave del sistema de origen. *Error común:* en este curso usamos `LocationID` como llave, para no complicar, pero en un almacén real se suele crear una propia.
- **Star schema o esquema estrella (5.9)**: un modelo con una tabla de hechos al centro y dimensiones directas alrededor, como una estrella. Las dimensiones están desnormalizadas. *Error común:* creer que el hecho depende de las demás en cadena, solo se conecta con cada dimensión.
- **Snowflake schema o copo de nieve (5.9)**: como la estrella, pero con las dimensiones normalizadas en sub-tablas. *Ejemplo:* `dim_zona` apunta a `dim_borough`. Ahorra repetición, pero agrega joins. *Error común:* elegirlo por defecto, para empezar casi siempre conviene la estrella.
- **Data lake**: almacenamiento barato de archivos en su forma original (CSV, JSON, Parquet), sin un modelo impuesto. *Error común:* creer que un lago es un almacén, un lago sin orden se vuelve un "pantano de datos".
- **Lakehouse (5.10)**: una arquitectura que junta lo bueno del lago (archivos baratos y abiertos) con lo bueno del almacén (tablas, transacciones, consultas rápidas). En la sesión 8 lo vemos en Databricks con Delta Lake. *Error común:* pensar que es un producto de una sola marca.
- **Arquitectura medallion (5.11)**: organizar los datos en tres capas de calidad creciente. **Bronze** guarda el dato crudo tal como llegó, **silver** lo limpia y le da forma, **gold** lo agrega para el consumo. *Ejemplo en el curso:* bronze es el parquet original, silver quita viajes con distancia cero, gold es el ingreso por día. *Error común:* limpiar en bronze, se pierde el dato original y no se puede auditar.
- **ETL (5.12)**: Extract, Transform, Load. Se extrae de la fuente, se transforma en un paso intermedio y se carga ya limpio al destino. *Error común:* creer que ETL y ELT son lo mismo con otro orden de letras, cambia dónde se hace el trabajo pesado.
- **ELT (5.12)**: Extract, Load, Transform. Se carga el dato crudo al destino y se transforma ahí, usando el poder del almacén o del motor SQL. *Ejemplo:* cargar el parquet tal cual (bronze) y hacer las capas silver y gold con SQL. *Error común:* creer que ELT elimina la transformación, solo cambia el lugar.

## Sesión 6: Polars I, DataFrames y evaluación lazy

### Por qué Polars (6.1, 6.2)

- **Polars (6.1)**: una librería de Python (escrita en Rust) para trabajar tablas de datos de forma rápida. Tiene un motor de consultas que optimiza lo que le pides antes de ejecutarlo. *Analogía:* un cocinero que lee toda la receta antes de empezar y organiza el trabajo. *Error común:* creer que es solo "pandas más rápido", tiene otra forma de pensar (expresiones y lazy).
- **pandas (6.1)**: la librería más conocida para tablas en Python. Ejecuta cada paso al momento, guarda un índice en cada tabla y suele necesitar bastante memoria. *Error común:* pensar que Polars es una versión nueva de pandas con los mismos métodos. Se parecen en el nombre de algunas cosas, pero no funciona igual.
- **Apache Arrow (6.2)**: un formato de datos en memoria organizado por columnas. Polars lo usa por dentro. Como todos los valores de una columna están juntos, se leen y se operan rápido, y se comparte con otras herramientas sin copiar. *Error común:* confundir Arrow (formato en memoria) con Parquet (formato en disco). Se parecen, y se llevan bien, pero no son lo mismo.
- **Ejecución paralela (6.2)**: Polars reparte el trabajo entre los núcleos del procesador a la vez. *Ejemplo:* calcular varias columnas al mismo tiempo. *Error común:* esperar que sea igual de rápido en cualquier máquina, en la máquina Basic de Deepnote hay 2 vCPU.
- **Columnar**: guardar los datos columna por columna y no fila por fila. Si solo necesitas 4 columnas de 19, solo lees esas 4. Es la base de las optimizaciones de hoy.

### DataFrame, Series y tipos (6.3 a 6.5)

- **Serie, `Series` (6.3)**: una columna de datos con nombre y un solo tipo. *Ejemplo:* `viajes["trip_distance"]`. *Error común:* creer que puede mezclar números y texto, no puede.
- **`DataFrame` (6.3)**: una tabla de datos en memoria, formada por Series del mismo largo. *Analogía:* una hoja de cálculo donde cada columna tiene un tipo fijo. *Error común:* pensar que modificarlo lo cambia en el lugar. Casi todos los métodos devuelven un DataFrame nuevo.
- **Tipo de dato (`dtype`) (6.4)**: la clase de valores que acepta una columna: `Int64` (enteros), `Float64` (decimales), `String` (texto), `Boolean`, `Date`, `Datetime`. *Error común:* creer que un número guardado como texto se puede sumar.
- **Esquema (`schema`) (6.4)**: la lista de nombres de columnas con su tipo. En Polars sale con `viajes.schema`. *Ejemplo:* `trip_distance` es `Float64`, `tpep_pickup_datetime` es `Datetime`.
- **Nulo (`null`)**: un valor que falta. En Polars se escribe `null`, y es distinto de `NaN` (un número "no válido", que solo existe en columnas decimales). *Error común:* contar `NaN` y `null` como lo mismo.
- **Ausencia de índice (6.5)**: un DataFrame de Polars no tiene índice de filas. Las filas se identifican solo por su posición, y no hay `.loc` ni `.iloc`. *Analogía:* una tabla impresa sin numerar las filas. *Error común:* buscar `reset_index()` o `df.index`, que no existen en Polars. Si necesitas un número de fila se agrega una columna con `with_row_index()`.

### Expresiones y contextos (6.6 a 6.9)

- **Expresión (6.6)**: una descripción de un cálculo sobre columnas, que todavía no se ejecuta. Se arma con `pl.col("nombre")` y funciones encadenadas. *Ejemplo:* `pl.col("total_amount") * 1.1`. *Analogía:* una receta escrita, no el platillo. *Error común:* creer que una expresión por sí sola devuelve datos, necesita un contexto.
- **`pl.col`**: la forma de nombrar una columna dentro de una expresión. `pl.col("a", "b")` elige varias columnas, y `pl.all()` elige todas.
- **`alias`**: ponerle nombre al resultado de una expresión. *Error común:* olvidarlo y obtener un `DuplicateError` cuando dos expresiones producen el mismo nombre de salida.
- **Contexto (6.7 a 6.9)**: el método donde se evalúan las expresiones y que decide qué se hace con ellas. Los tres básicos son `select`, `filter` y `with_columns`.
- **Contexto `select` (6.7)**: elige o calcula columnas, y el resultado trae solo esas columnas. *Equivale a:* el `SELECT` de SQL. *Error común:* usar `select` esperando conservar el resto de columnas.
- **Contexto `filter` (6.8)**: deja solo las filas que cumplen una condición. *Equivale a:* `WHERE`. Para combinar condiciones se usa `&` (y), `|` (o) y paréntesis, no `and` ni `or`. *Error común:* usar `and` de Python y recibir un error de "truth value of an Expr is ambiguous".
- **Contexto `with_columns` (6.9)**: agrega columnas nuevas o reemplaza existentes, y conserva todas las demás. *Equivale a:* `SELECT *, nueva_columna`. *Error común:* intentar `df["nueva"] = ...` como en pandas, Polars no lo permite.
- **Encadenamiento**: unir varios métodos uno tras otro, cada uno sobre el resultado del anterior, entre paréntesis y un método por línea. *Analogía:* una línea de producción. *Error común:* olvidar los paréntesis externos o el punto al inicio de cada línea.
- **`when`, `then`, `otherwise`**: el equivalente en Polars de `CASE WHEN`. *Ejemplo:* `pl.when(pl.col("fare_amount") > 0).then(...).otherwise(None)`.
- **`pl.len()`**: la expresión que cuenta filas. *Equivale a:* `COUNT(*)`.
- **Expresiones nativas contra lambdas**: las funciones de Polars (`pl.col("x") * 2`) corren en el motor optimizado y en paralelo. Una lambda de Python (`map_elements`) corre fila por fila y es mucho más lenta. *Error común:* usar `lambda` por costumbre.

### Evaluación lazy (6.10 a 6.13)

- **Ejecución eager**: el cálculo se hace al momento en que escribes cada instrucción, y cada paso crea un resultado completo en memoria. *Ejemplo:* `viajes.filter(...)` ya devuelve una tabla nueva.
- **Ejecución lazy (perezosa)**: las instrucciones solo se anotan, el cálculo se hace hasta que pides el resultado. Eso le permite al motor ver todo el plan y optimizarlo. *Analogía:* dar la lista completa de compras en lugar de ir tienda por tienda.
- **`read_` (6.10)**: funciones como `pl.read_parquet` o `pl.read_csv` que leen el archivo completo a memoria y devuelven un `DataFrame`. *Error común:* usarlas con archivos grandes en una máquina chica.
- **`scan_` (6.10)**: funciones como `pl.scan_parquet` que no leen todavía, solo registran de dónde van a leer y devuelven un `LazyFrame`. *Error común:* esperar ver datos al ejecutar un `scan_`, solo ves el plan.
- **`LazyFrame` y plan de consulta (6.11)**: el `LazyFrame` es la tabla "pendiente de calcular". Guarda el plan de consulta, la lista de pasos que se van a ejecutar. *Error común:* intentar usar `.height` o `viajes[0]` en un LazyFrame, esos atributos no existen hasta que se ejecuta.
- **`collect()` (6.12)**: ejecuta el plan y devuelve un `DataFrame` normal. *Error común:* olvidarlo y confundirse porque aparece un plan en lugar de una tabla.
- **`explain()` (6.12)**: muestra el plan de consulta ya optimizado como texto, sin ejecutarlo. *Ejemplo:* ver cuántas columnas se van a leer.
- **Optimizador de consultas**: la parte de Polars que reescribe el plan para hacerlo más barato sin cambiar el resultado.
- **Projection pushdown (6.13)**: el optimizador detecta qué columnas realmente se usan y solo lee esas del archivo. *Ejemplo:* si la consulta usa 5 de las 19 columnas, solo se leen 5. En el plan se ve como `PROJECT n/N COLUMNS`. *Error común:* pensar que lee todo y luego descarta, el descarte ocurre desde la lectura.
- **Predicate pushdown (6.13)**: el filtro se aplica al leer el archivo, y no después de cargar todo. En el plan aparece como `SELECTION`. *Ejemplo:* `trip_distance > 0` se evalúa durante el escaneo. *Error común:* creer que el orden en que escribes el `filter` cambia el resultado, el optimizador lo acomoda.
- **Memoria (RAM)**: el espacio de trabajo de la máquina, 5 GB en Deepnote Basic. El dataset de taxis cabe en memoria (alrededor de 390 MB), varios meses combinados no. Por eso lazy no es un lujo: es la forma de crecer sin reventar la máquina.

## Sesión 7: Polars II, transformaciones y agregaciones a escala

### Tipos, fechas, texto, nulos y duplicados (7.1 a 7.4)

- **Casteo de tipos, `cast` (7.1)**: convertir una columna de un tipo a otro, por ejemplo de entero a decimal o de texto a número. *Ejemplo:* `pl.col("passenger_count").cast(pl.Int8)`. *Error común:* convertir texto con letras a número y recibir un error, con `strict=False` esos valores quedan en `null` en vez de fallar.
- **Tipo más chico**: usar `Int8` en lugar de `Int64` para valores pequeños ahorra memoria. *Error común:* usar un tipo demasiado chico y que el valor no quepa.
- **Namespace**: un grupo de funciones que cuelga de una expresión según el tipo de dato. Para fechas es `.dt`, para texto es `.str`. *Analogía:* los cajones de una cómoda, uno para fechas y otro para texto.
- **Namespace `.dt` (7.2)**: funciones para columnas de fecha y hora, como `dt.hour()`, `dt.weekday()`, `dt.date()`, `dt.month()`, `dt.truncate("1h")`, `dt.total_minutes()`. *Ejemplo:* sacar la hora de `tpep_pickup_datetime`. *Error común:* usar `.dt` sobre una columna que es texto, hay que convertirla a fecha primero.
- **`dt.weekday()`**: el día de la semana como número, donde 1 es lunes y 7 es domingo. *Error común:* esperar que el domingo sea 0.
- **Namespace `.str` (7.3)**: funciones para columnas de texto, como `str.to_uppercase()`, `str.contains()`, `str.replace()`, `str.starts_with()`, `str.len_chars()`. *Ejemplo:* encontrar las zonas cuyo nombre contiene "Airport". *Error común:* `str.contains` entiende expresiones regulares, un punto o un paréntesis pueden comportarse distinto a lo esperado.
- **Nulo (7.4)**: un valor que falta. Se detecta con `is_null()`, se cuenta con `null_count()`, se descarta con `drop_nulls()` y se reemplaza con `fill_null()`. *Error común:* rellenar nulos sin pensar, `fill_null(0)` en una columna de pasajeros inventa información.
- **Duplicado (7.4)**: una fila repetida. Se detecta con `is_duplicated()` y se elimina con `unique()`. Con `subset=[...]` se decide por qué columnas se compara. *Error común:* creer que `unique()` conserva el orden original, hay que usar `maintain_order=True` si importa.

### Agregaciones y orden (7.5, 7.6)

- **`group_by` + `agg` (7.5)**: agrupar filas por una o más columnas y calcular algo por cada grupo. *Equivale a:* `GROUP BY`. El resultado tiene una fila por grupo. *Ejemplo:* ticket promedio por método de pago. *Error común:* olvidar que el orden de los grupos no está garantizado.
- **Métrica**: el cálculo que se hace por grupo, como contar, sumar, promediar, máximo, mediana. Se escribe como expresión: `pl.col("x").mean()`.
- **Múltiples métricas y alias (7.6)**: dentro de `agg` se pueden poner varias expresiones separadas por coma, cada una con `alias` para dar nombre a la columna de salida. *Error común:* olvidar el `alias` y obtener nombres repetidos o poco claros.
- **`sort`**: ordena el resultado. `descending=True` va de mayor a menor. Se puede ordenar por varias columnas, útil para desempatar. *Error común:* esperar que `group_by` devuelva los grupos en un orden estable, sin `sort` el orden puede cambiar entre ejecuciones.
- **`maintain_order`**: un parámetro de `group_by` que conserva el orden de aparición de los grupos. Es más lento, se usa solo cuando hace falta.

### Joins y window functions (7.7 a 7.9)

- **Join (7.7)**: unir dos tablas con una columna en común. *Equivale a:* `JOIN` de SQL. *Error común:* unir sin revisar el tipo y el contenido de la llave.
- **Join `inner`**: conserva solo las filas que tienen pareja en ambas tablas. *Error común:* perder filas sin darse cuenta si falta alguna llave.
- **Join `left`**: conserva todas las filas de la tabla izquierda, y pone `null` donde no hay pareja. *Ejemplo:* todos los viajes, con la zona cuando existe.
- **Join `anti`**: devuelve las filas de la tabla izquierda que NO tienen pareja en la derecha. *Ejemplo:* las zonas que nunca fueron origen de un viaje. Sirve para encontrar filas huérfanas.
- **`left_on` y `right_on` (7.8)**: se usan cuando la llave se llama distinto en cada tabla. *Ejemplo:* `left_on="PULocationID", right_on="LocationID"`. Si se llama igual, basta `on=`. *Error común:* esperar que la columna `LocationID` siga en el resultado: en un join `left` o `inner` la columna de la derecha se descarta por defecto, queda solo `PULocationID`.
- **Sufijo (`suffix`)**: cuando las dos tablas tienen una columna con el mismo nombre, la de la derecha recibe un sufijo (`_right` por defecto). *Ejemplo:* al unir `zonas` dos veces, una para origen y otra para destino, se pone `suffix="_destino"`. *Error común:* hacer dos joins sin sufijo y no saber cuál `Zone` es cuál.
- **Window function con `.over()` (7.9)**: calcular algo por grupo pero sin colapsar las filas, igual que `OVER (PARTITION BY ...)` de SQL. *Ejemplo:* `pl.col("n_viajes").sum().over("Borough")` pone en cada fila el total de su Borough. *Error común:* confundirla con `group_by`, que sí reduce el número de filas.

### Streaming, archivos múltiples y gráficas (7.10, 7.11)

- **Motor streaming (7.10)**: una forma de ejecutar el plan lazy procesando el archivo en pedazos, en lugar de cargarlo completo. Se activa con `collect(engine="streaming")`. Permite trabajar con datos más grandes que la memoria. *Analogía:* contar una pila enorme de billetes por montones, en lugar de ponerlos todos en la mesa. *Error común:* creer que es automático, hay que pedirlo, y que todas las operaciones están soportadas igual.
- **Glob (7.11)**: un patrón con comodines para elegir varios archivos a la vez. `*` significa "cualquier texto". *Ejemplo:* `datos/viajes_2024_*.parquet` elige todos los archivos que empiezan con `viajes_2024_` y terminan en `.parquet`. *Error común:* un patrón demasiado amplio (`datos/*`) que incluye archivos que no son datos.
- **Lectura de múltiples archivos (7.11)**: `pl.scan_parquet` acepta un glob y trata todos los archivos como una sola tabla lazy. Con `include_file_paths="archivo"` agrega una columna con el nombre del archivo de origen. *Error común:* asumir que todos los meses tienen el mismo esquema (ver schema drift).
- **Schema drift**: cuando el esquema de los archivos cambia entre un mes y otro, por ejemplo una columna que pasa de entero a decimal, o una columna nueva. Al leer varios archivos juntos aparece un `SchemaError` o un `ColumnNotFoundError`. Es la razón por la que en clase se usa un solo mes.
- **Plotly**: una librería de gráficas interactivas. Con `plotly.express` (`px`) se arma una gráfica en una línea a partir de un DataFrame. *Error común:* graficar la tabla completa de 3 millones de filas, se grafica el resultado ya agregado.

## Sesión 8: Introducción a Databricks, lakehouse y notebooks

- **Databricks**: una plataforma en la nube para trabajar con datos y con inteligencia artificial en un solo lugar. Reúne notebooks, SQL, procesamiento distribuido con Spark, tablas con control de acceso y herramientas para pipelines. *Analogía:* un edificio de oficinas completo, mientras Deepnote es tu escritorio. *Error común:* creer que Databricks es solo un notebook más grande.
- **Free Edition**: la versión gratuita de Databricks para estudiantes, docentes y gente que quiere aprender. Según la documentación (consultada el 14 de octubre de 2026) funciona solo con compute serverless y con cuotas, y reemplazó a Community Edition, que se retiró en 2025. Es para uso no comercial y no tiene soporte ni garantía de servicio. *Error común:* pensar que es una prueba de 14 días, no tiene fecha de vencimiento, pero las cuentas inactivas pueden eliminarse.
- **Cuota (uso justo)**: el límite de cómputo que puedes gastar. La documentación dice que si te pasas, el compute de tu workspace se apaga por el resto del día y, en casos extremos, por el resto del mes. Tus datos y configuración no se borran. *Número exacto de la cuota:* no está publicado en esa página, verificar en tu cuenta. *Error común:* ejecutar cosas pesadas "por probar" y quedarse sin compute a media clase.
- **Cluster**: un grupo de máquinas que Databricks enciende para correr tu código. En Free Edition no se crean ni se configuran clusters, por eso no encontrarás ese botón. *Ejemplo:* en una cuenta de empresa eliges tamaño y tipo de máquinas, aquí no. *Error común:* pasar 10 minutos buscando "Create cluster".
- **Compute serverless**: compute que Databricks administra por ti, sin que elijas ni enciendas máquinas. Tú ejecutas la celda y la plataforma pone los recursos. En Free Edition el compute de notebooks tiene tamaño y uso limitados. *Analogía:* tomar un taxi en lugar de comprar y mantener un coche. *Error común:* creer que "serverless" significa que no hay servidores, hay, pero no los administras.
- **Data lake**: un almacén barato de archivos de todo tipo (Parquet, CSV, imágenes) sin estructura impuesta. Guarda mucho, pero no garantiza orden ni consistencia. *Analogía:* una bodega grande. *Error común:* creer que guardar archivos ya es "tener datos listos".
- **Data warehouse**: una base de datos pensada para análisis, con tablas bien definidas, SQL rápido y reglas. Es ordenado, pero tradicionalmente más caro y menos flexible con datos sin estructura. *Analogía:* una biblioteca catalogada.
- **Lakehouse**: una arquitectura que junta lo mejor de los dos: archivos baratos del lake con tablas confiables, transacciones y SQL del warehouse. En Databricks se logra con Delta Lake encima del almacenamiento de archivos. *Error común:* pensar que es un producto, es una forma de organizar la arquitectura.
- **Workspace de Databricks**: tu espacio de trabajo en el navegador, donde viven notebooks, carpetas, consultas y tablas. Free Edition da un workspace y un metastore por cuenta.
- **Delta Lake**: un formato de tabla de código abierto que se guarda como archivos Parquet más un registro de transacciones. Ese registro es lo que da ACID, historial y time travel. *Ejemplo:* una tabla Delta se ve como carpeta con archivos `.parquet` y una carpeta `_delta_log`. *Error común:* creer que Delta reemplaza a Parquet, lo usa por debajo.
- **Registro de transacciones (`_delta_log`)**: el diario donde Delta anota cada cambio hecho a la tabla. Quien lee la tabla consulta ese diario para saber qué archivos forman la versión actual.
- **ACID**: cuatro garantías de una transacción. *Atomicidad:* o se aplica todo el cambio o nada. *Consistencia:* la tabla nunca queda en un estado que rompa sus reglas. *Aislamiento:* quien lee mientras otro escribe ve una versión completa, no a medias. *Durabilidad:* un cambio confirmado no se pierde. *Ejemplo:* si un `DELETE` falla a la mitad, la tabla queda como estaba. *Error común:* creer que un data lake de archivos sueltos ya las tiene.
- **Tabla gestionada (managed)**: una tabla cuyos archivos y metadatos administra Databricks. Si borras la tabla (`DROP`), se borran también los datos. *Ejemplo:* la tabla `yellow_taxi` que creamos hoy con `saveAsTable`. *Error común:* creer que `DROP TABLE` solo quita el nombre.
- **Tabla externa (external)**: una tabla cuyos datos viven en una ubicación que tú controlas. Si la borras, el nombre desaparece, los archivos se quedan. *Nota:* en Free Edition no se pueden configurar ubicaciones de almacenamiento personalizadas, por eso hoy solo se revisa el concepto y no se crea una (verificar si tu cuenta permite alguna ubicación externa). *Error común:* usar externas "porque suenan más profesionales" sin necesitar la razón (que otro sistema también lea esos archivos).
- **Time travel**: consultar la tabla como estaba en una versión o fecha anterior. Se escribe `VERSION AS OF n` o `TIMESTAMP AS OF 'fecha'`. *Ejemplo:* ver cuántas filas había antes de un `DELETE`. *Error común:* creer que guarda historia para siempre. Según la documentación el historial se conserva 30 días por defecto y los archivos eliminados 7 días, y se recomienda confiar solo en los últimos 7 días salvo que cambies esas configuraciones.
- **`DESCRIBE HISTORY`**: comando que lista las operaciones hechas a una tabla Delta (versión, fecha, operación, usuario). Sirve para auditar y para encontrar el número de versión al que quieres regresar.
- **`RESTORE`**: comando que regresa una tabla a una versión anterior (`RESTORE TABLE t TO VERSION AS OF n`). Es otra operación más del historial, no borra el historial. *Error común:* ejecutarlo sin revisar primero a qué versión va.
- **Unity Catalog**: el sistema de Databricks para organizar y gobernar datos: quién puede ver qué, y dónde vive cada objeto. Organiza todo en tres niveles. *Analogía:* el directorio del edificio con las llaves de cada oficina.
- **Catálogo, esquema y tabla (espacio de nombres de tres niveles)**: la dirección completa de una tabla es `catálogo.esquema.tabla`. *Ejemplo:* `workspace.curso_de.yellow_taxi`. *Error común:* escribir solo `yellow_taxi` y consultar sin saber en qué catálogo y esquema se está parado.
- **Volumen (volume)**: un lugar dentro de Unity Catalog para guardar archivos (no tablas), como nuestro parquet o un CSV. Su ruta empieza con `/Volumes/`. Subir un archivo por la interfaz a un volumen tiene un límite de 5 GB según la documentación.
- **Metastore**: el registro central de Unity Catalog con la lista de catálogos, esquemas, tablas y permisos. Free Edition incluye uno por cuenta.
- **Notebook de Databricks**: un notebook donde cada celda puede ser Python, SQL o Markdown. Una celda cambia de lenguaje con una línea mágica como `%sql` o `%md`. *Error común:* creer que todas las celdas deben ser del mismo lenguaje.
- **SQL editor**: la pantalla para escribir consultas SQL sin notebook, guardarlas y hacer gráficas. Corre sobre un SQL warehouse.
- **SQL warehouse**: el compute dedicado a ejecutar SQL (consultas, dashboards). En Free Edition hay uno solo, de tamaño `2X-Small` según la documentación. *Error común:* esperar que responda al instante la primera vez, puede tardar en arrancar.
- **Apache Spark**: el motor de procesamiento distribuido detrás de Databricks. Reparte el trabajo entre varias máquinas. *Error común:* usar Spark para datos que caben cómodos en Polars, para este dataset sería excesivo, lo usamos hoy para aprender la plataforma.
- **PySpark**: la API de Spark para Python. *Ejemplo:* `spark.table("...").groupBy("payment_type").count()`. Free Edition no soporta R ni Scala, solo SQL y Python en la práctica.
- **DataFrame de Spark**: una tabla distribuida con filas y columnas con nombre, parecida al DataFrame de Polars pero con otra sintaxis. *Error común:* creer que sus métodos se llaman igual que en Polars (`groupBy` con B mayúscula, `orderBy`, `agg`).
- **Transformación y acción (evaluación perezosa en Spark)**: las transformaciones (`filter`, `groupBy`, `select`) solo arman un plan, las acciones (`display`, `show`, `count`, `write`) lo ejecutan. Es la misma idea de `scan_parquet` y `collect` en Polars. *Error común:* creer que no pasó nada porque la celda de la transformación terminó rápido.
- **`display()`**: función de Databricks que muestra un DataFrame como tabla interactiva y permite agregar visualizaciones. *Error común:* usar `print(df)`, que no muestra los datos.
- **Genie**: el asistente de Databricks que responde preguntas sobre tus datos en lenguaje natural y genera la consulta SQL. La documentación de Free Edition lo lista entre lo que incluye. Hoy es solo panorama. *Error común:* confiar en la respuesta sin leer el SQL que generó, hay que revisarlo como cualquier consulta.
- **Criterios de elección de plataforma**: las preguntas para decidir dónde correr un trabajo: tamaño de los datos, quién colabora, cuánto cuesta, necesidad de gobierno y permisos, y si el trabajo tiene que correr de forma programada. Se resumen en la tabla del bloque de 130 a 145.

## Sesión 9: Pipeline ETL/ELT y calidad de datos

- **ETL**: Extract, Transform, Load. Se extraen los datos de la fuente, se transforman en un paso intermedio y se cargan ya limpios al destino. *Ejemplo:* limpiar el parquet con Polars y guardar solo el resultado limpio. *Error común:* creer que ETL es siempre mejor porque "ya llega limpio".
- **ELT**: Extract, Load, Transform. Primero se carga el dato crudo al destino (lakehouse o warehouse) y la transformación se hace allá, normalmente con SQL. *Ejemplo:* subir el parquet tal cual a una tabla y limpiar con consultas, como hicimos en Databricks. *Error común:* pensar que ELT significa no transformar.
- **Batch (por lotes)**: procesar los datos en grupos, cada cierto tiempo (cada hora, cada noche). *Ejemplo:* el archivo mensual de taxis. *Error común:* creer que batch es "lento", solo es por lotes.
- **Streaming (flujo continuo)**: procesar cada dato casi en cuanto llega. *Ejemplo:* un tablero que se actualiza con cada viaje nuevo. Hoy solo es panorama. *Error común:* usar streaming cuando una carga diaria bastaba, cuesta más y complica.
- **Capas medallion (bronze, silver, gold)**: una forma de ordenar el pipeline en capas que se limpian poco a poco.
- **Bronze**: el dato crudo, copiado fiel de la fuente, sin corregir. Sirve para poder repetir todo desde el origen. *Ejemplo:* `datos/bronze/viajes_2024_01.parquet`. *Error común:* limpiar en bronze y perder el original.
- **Silver**: el dato limpio, con tipos correctos y reglas aplicadas, a nivel de registro. *Ejemplo:* viajes válidos con distancia mayor a cero. *Error común:* mezclar aquí las agregaciones del negocio.
- **Gold**: tablas listas para consumo, agregadas y pensadas para una pregunta. *Ejemplo:* ingreso por borough. *Error común:* hacer una gold para cada capricho en lugar de partir de silver.
- **Idempotencia**: ejecutar un proceso una o varias veces con los mismos datos de entrada deja exactamente el mismo resultado. *Analogía:* el botón de un elevador, apretarlo cinco veces no llama cinco elevadores. *Error común:* escribir con "agregar al final" (append) y duplicar filas al reintentar.
- **Carga completa (full load)**: cada corrida reprocesa todo. Es simple y segura, pero cara cuando crece el volumen.
- **Carga incremental**: cada corrida procesa solo lo nuevo. Se apoya en una marca de agua (por ejemplo, la fecha más reciente ya cargada) o en una llave para saber qué ya existe. *Error común:* confiar en la marca de agua sin validar fechas, un dato con fecha rara la desplaza.
- **Marca de agua (watermark)**: el valor que recuerda hasta dónde ya se cargó. *Ejemplo:* la fecha de recogida más reciente en silver.
- **Calidad de datos**: qué tan confiables y útiles son los datos para el uso que se les quiere dar. Se mide con dimensiones.
- **Completitud**: ¿vienen todos los datos que deberían venir? *Ejemplo:* un viaje sin zona de origen. *Error común:* confundir nulo con cero.
- **Validez**: ¿el valor tiene un formato o rango permitido? *Ejemplo:* distancia mayor a cero, importe no negativo.
- **Unicidad**: ¿no hay registros repetidos? *Ejemplo:* el mismo viaje dos veces.
- **Consistencia**: ¿los datos concuerdan entre sí y con otras fuentes? *Ejemplo:* el `PULocationID` debe existir en la tabla de zonas.
- **Oportunidad (actualidad)**: ¿los datos están al día y en el periodo esperado? *Ejemplo:* un viaje fechado en diciembre dentro del archivo de enero.
- **Regla de validación**: una condición que cada registro debe cumplir. En Polars se escribe como expresión booleana. En el curso cada regla vale `True` cuando el registro **falla**.
- **Valores nulos y reglas**: una comparación con un nulo da nulo, no falso. *Ejemplo:* `trip_distance <= 0` es nulo cuando la distancia es nula, y un filtro lo tira o lo deja pasar sin avisar. *Error común:* validar sin manejar nulos antes, es la fricción más frecuente de la sesión.
- **Pandera**: biblioteca para describir un esquema (columnas, tipos y reglas) y validar un DataFrame contra él. Se usa `pandera.polars`, el backend para Polars.
- **Esquema (`DataFrameSchema`)**: la descripción de cómo debe verse una tabla. *Ejemplo:* `trip_distance` es decimal y mayor a cero. *Error común:* hacerlo tan estricto que todo falla.
- **Validación perezosa (`lazy=True`)**: pide a Pandera recopilar todos los fallos antes de lanzar el error, en lugar de detenerse en el primero. El error `SchemaErrors` trae una tabla `failure_cases`.
- **Quarantine (cuarentena)**: una zona aparte donde se guardan los registros que no pasaron las reglas, con el motivo. No se tiran, se revisan. *Analogía:* la mesa de objetos que revisa el inspector de aduana. *Error común:* borrar los registros inválidos sin dejar rastro.
- **Conciliación**: comprobar que las cuentas cuadran entre capas. *Ejemplo:* el número de filas en silver debe ser igual a la suma de viajes en gold.
- **Logging**: registrar lo que hace el programa con mensajes y niveles, en lugar de usar `print`. Niveles de menor a mayor: DEBUG, INFO, WARNING, ERROR, CRITICAL. *Error común:* usar print y no tener hora, nivel ni forma de filtrar.
- **Métricas de ejecución**: números que describen una corrida: filas leídas, filas en silver, filas en cuarentena, duración. *Ejemplo:* guardarlas en un JSON. Permiten notar cuando algo cambia.
- **Orquestador**: herramienta que programa, ejecuta y vigila pipelines en el orden correcto, con reintentos y alertas. *Panorama:* Apache Airflow (flujos como DAGs en Python), Dagster (orientado a activos de datos) y Prefect (flujos y tareas en Python). Hoy solo se nombran. *Error común:* creer que un orquestador es lo que procesa los datos, solo coordina.
- **DAG**: grafo acíclico dirigido, la forma de describir qué tarea va antes de cuál sin ciclos.
- **Script `.py`**: un archivo de código que se ejecuta de principio a fin desde la terminal, sin notebook. *Ejemplo:* `python pipeline.py`. *Error común:* creer que un script es "menos" que un notebook, es lo que corre en producción.
- **`if __name__ == "__main__"`**: el bloque que corre solo cuando ejecutas el archivo directamente, no cuando lo importas.
- **Código de salida**: el número con el que un programa avisa cómo terminó. 0 significa éxito, distinto de 0 significa fallo. Los orquestadores lo usan para decidir si reintentan.
- **Dependencia**: un paquete externo que tu código necesita (Polars, DuckDB, Pandera).
- **Archivo de dependencias (`pyproject.toml`)**: el archivo donde se anotan el proyecto y sus dependencias. *Error común:* instalar paquetes a mano sin anotarlos y que otra persona no pueda repetir el entorno.
- **Archivo de bloqueo (`uv.lock`)**: guarda las versiones exactas instaladas. Lo crea uv.
- **Entorno virtual (`.venv`)**: una carpeta con su propio Python y paquetes, separada de otros proyectos.
- **uv**: herramienta para gestionar proyectos de Python, dependencias y entornos de forma rápida. `uv init --no-package` crea un proyecto simple de scripts, `uv add` agrega dependencias y `uv run` ejecuta dentro del entorno del proyecto. *Error común:* creer que uv reemplaza a Python, lo administra.
- **Schema drift**: cambio no anunciado en tipos o columnas de la fuente. Seleccionar solo las columnas que usas y fijar los tipos en silver protege el pipeline.

## Sesión 10: Proyecto final documentado en Deepnote

- **Proyecto integrador (proyecto final)**: un trabajo donde se usa todo lo aprendido: ingesta, capas, calidad, JOIN, agregaciones, visualizaciones y documentación. *Ejemplo:* el pipeline de taxis de la sesión 9, ahora con gráficas y texto. *Error común:* querer hacerlo gigante, un proyecto pequeño bien terminado vale más.
- **Integración del pipeline completo**: juntar en un solo notebook todas las piezas en orden lógico, de modo que "Run all" lo ejecute de principio a fin sin errores. *Error común:* dejar celdas de prueba que dependen de otras fuera de orden.
- **Documentación**: texto que explica qué hace el trabajo, por qué se tomaron las decisiones y cómo repetirlo. *Analogía:* las instrucciones de una receta. *Error común:* escribir qué hace el código línea por línea en lugar de explicar la razón.
- **Narrativa en Markdown**: usar celdas de texto con títulos, listas y énfasis para contar una historia: pregunta, método, resultados, conclusión. *Ejemplo:* un `## Calidad de datos` seguido de dos párrafos y una tabla de reglas. *Error común:* un notebook de 40 celdas de código sin una sola línea de texto.
- **Resumen (README) del notebook**: la primera sección del notebook con la pregunta, el dataset, el hallazgo principal y cómo reproducirlo. Quien lo abra debe entender de qué trata en 30 segundos.
- **Reproducibilidad**: que otra persona, o tú en seis meses, pueda ejecutar el notebook desde cero y obtener el mismo resultado. *Prueba simple:* Run all en una máquina recién encendida.
- **Orden de ejecución**: la secuencia en que se corrieron las celdas, que puede ser distinta del orden en que se leen. *Error común:* confiar en que "ya corrí esa celda ayer".
- **Estado oculto**: variables que viven en la memoria de la máquina aunque la celda que las creó ya no exista o se haya cambiado. *Ejemplo:* una celda usa `umbral` pero la celda donde se definió se borró; funciona hoy y falla con Run all. *Error común:* entregar el proyecto sin probar un Run all limpio.
- **Run all**: ejecutar todo de arriba hacia abajo. Para estar seguro de la reproducibilidad, hazlo con la máquina recién reiniciada.
- **Comentario (en Deepnote)**: una nota que se deja sobre un bloque, con el botón de comentario arriba a la derecha del bloque. Sirve para revisar sin editar el código del otro. Los hilos se pueden resolver y reabrir.
- **Mención (@)**: escribir `@` en un comentario y elegir a una persona. Deepnote le manda un correo.
- **Revisión entre pares**: que una persona revise el trabajo de otra con criterios claros y dé retroalimentación útil. *Ejemplo:* usar la lista de verificación de la rúbrica. *Error común:* decir "está bien" o "no me gustó" sin detalles.
- **Retroalimentación útil**: específica, amable y accionable. Una fórmula: qué funciona, qué falta, una sugerencia concreta.
- **Historial de versiones**: el registro de cambios del proyecto. En Deepnote se abre desde el menú de tres puntos arriba a la derecha del proyecto o desde el ícono de Versions, y requiere permiso de edición o mayor. Restaurar crea primero una copia del estado actual, así que es seguro. En el plan Free la documentación de precios (consultada el 14 de octubre de 2026) indica 7 días de historial, verificar el que corresponde a tu plan.
- **Restaurar una versión**: regresar el proyecto a un punto anterior del historial. Afecta a todos los notebooks del proyecto a la vez.
- **Permisos y compartición**: Deepnote permite compartir con personas por correo o con un enlace, y elegir el nivel de acceso: View (solo ver), Comment (ver y comentar), Execute (además ejecutar), Edit (además editar) y Full access (además administrar). *Ejemplo:* para revisión entre pares se usa Comment, para la entrega final View. Algunos permisos finos solo existen en planes Team y Enterprise. *Error común:* compartir con nivel Edit "por si acaso" y que alguien cambie el trabajo.
- **Enlace compartido**: una URL que da acceso según el nivel que elijas. Según la documentación, quien abre el enlace en modo View no necesita cuenta, pero sí necesita registrarse para ejecutar bloques.
- **App publicada**: una vista del notebook sin editar, creada con **Create app** y los bloques que elijas. Cada proyecto puede tener una app. Su visibilidad se elige entre "Workspace & collaborators", "Anyone with a link" y "Public". *Error común:* creer que ocultar un bloque lo hace privado, los bloques ocultos siguen siendo accesibles para quien tenga acceso a la app, y hay una opción para esconder todo el código.
- **Publicación de resultados**: dejar el trabajo en un lugar donde otra persona lo pueda ver sin tu ayuda. En este curso, el proyecto compartido por enlace o la app publicada. Qué opciones están disponibles en tu plan: verificar. *Error común:* publicar datos personales o sensibles.
- **Visualización clara**: una gráfica con título, ejes con nombre y unidades, y un mensaje. *Ejemplo:* "Ingreso total por borough de origen" con eje en dólares. *Error común:* gráficas sin título o con demasiados colores.
- **Hallazgo (insight)**: una conclusión que sale de los datos y sirve para decidir. *Ejemplo:* "La hora pico de viajes es a las 18:00". *Error común:* describir la gráfica en lugar de decir qué significa.
- **Presentación de resultados**: contar el proyecto en 3 a 5 minutos con orden: pregunta, datos, método, resultado y límites. *Error común:* explicar cada línea de código.
- **Rúbrica**: la tabla de criterios y puntos con la que se evalúa. Está en `proyecto_final/RUBRICA.md` y vale 100 puntos.
- **Ruta de aprendizaje posterior**: los temas que siguen después del curso. Se listan en el bloque de cierre: Python intermedio y Git, entornos locales (uv, Docker), orquestación (Airflow, Dagster, Prefect), dbt, modelado dimensional, nube y almacenamiento de objetos, Spark y PySpark.

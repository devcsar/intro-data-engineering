# Rúbrica del proyecto final (100 puntos)

El proyecto final vale 40% de la evaluación del curso. Esta rúbrica la usan el instructor para calificar y los compañeros para la revisión entre pares.

| Criterio | Puntos |
|---|---|
| Ingesta y lectura correcta de datos | 15 |
| Transformaciones (joins, agregaciones, medallion) | 25 |
| Calidad de datos (validaciones) | 20 |
| Documentación y claridad narrativa | 20 |
| Visualizaciones e insights | 15 |
| Presentación | 5 |
| **Total** | **100** |

## Descriptores por nivel

Dentro de cada nivel, el instructor elige el puntaje según qué tan completo está lo descrito.

### 1. Ingesta y lectura correcta de datos (15 puntos)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 13 a 15 | Lee Parquet o CSV con rutas o URL claras y fáciles de cambiar. Muestra el esquema, el número de filas y revisa los tipos. Bronze conserva el dato crudo sin cambios y registra su origen. El notebook obtiene sus datos por sí mismo, desde cero. |
| Bueno | 10 a 12 | Lee bien y muestra el esquema. Bronze existe, pero hay rutas fijas difíciles de cambiar, o falta registrar el origen o revisar los tipos. |
| Suficiente | 6 a 9 | Lee los datos, pero con problemas de tipos sin atender, sin capa bronze separada, o depende de archivos que otra persona no puede obtener. |
| Insuficiente | 0 a 5 | No logra leer los datos, o el notebook falla en la ingesta. |

### 2. Transformaciones: joins, agregaciones y medallion (25 puntos)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 22 a 25 | Silver tiene tipos correctos y los datos limpios. Hay al menos un JOIN entre hechos y dimensión, con la clave y el tipo de JOIN justificados (y se revisa qué pasa con las filas sin pareja). Hay al menos tres agregaciones que responden preguntas distintas. Gold está escrita en su carpeta. El pipeline es idempotente y se demuestra. |
| Bueno | 17 a 21 | Las tres capas existen. El JOIN y las tres agregaciones están y son correctos, pero falta justificar decisiones, revisar las filas sin pareja o demostrar la idempotencia. |
| Suficiente | 11 a 16 | Falta alguna pieza: una capa, el JOIN o una agregación, o hay errores que cambian los resultados (por ejemplo, filas duplicadas). |
| Insuficiente | 0 a 10 | Faltan varias piezas o las transformaciones no funcionan. |

### 3. Calidad de datos: validaciones (20 puntos)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 18 a 20 | Al menos tres validaciones, de dimensiones distintas (por ejemplo completitud, validez, consistencia), con la razón de cada una. Los registros inválidos van a cuarentena con el motivo. Se informa cuántos cayeron por regla. Se usa un esquema de Pandera como contrato. Se manejan los nulos antes de validar. |
| Bueno | 14 a 17 | Tres validaciones y cuarentena con motivo, pero faltan razones escritas, el conteo por regla o el contrato de Pandera. |
| Suficiente | 8 a 13 | Hay validaciones, pero son menos de tres, o no hay cuarentena (se tiran los registros sin dejar rastro), o son demasiado estrictas o flojas sin análisis. |
| Insuficiente | 0 a 7 | No hay validaciones, o no funcionan. |

### 4. Documentación y claridad narrativa (20 puntos)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 18 a 20 | El notebook empieza con un resumen (pregunta, dataset, hallazgo, cómo reproducirlo). Cada sección tiene texto en Markdown que explica el porqué de las decisiones. Hay una sección de límites y siguientes pasos. Corre de arriba hacia abajo sin errores y sin estado oculto. Está publicado y abre sin pedir permisos. |
| Bueno | 14 a 17 | Hay resumen y secciones explicadas. Faltan algunos porqués, o la sección de límites, o hay un detalle menor de orden o publicación. |
| Suficiente | 8 a 13 | Hay algo de texto, pero se limita a decir qué hace el código. O el notebook falla con Run all. O el enlace no abre. |
| Insuficiente | 0 a 7 | Casi no hay texto, es solo código, o no se puede abrir. |

### 5. Visualizaciones e insights (15 puntos)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 13 a 15 | Al menos dos gráficas claras con título, ejes con nombre y unidades, tipo de gráfica adecuado. Cada una tiene una frase de lectura. Las conclusiones usan números tomados de los datos y responden la pregunta del proyecto. |
| Bueno | 10 a 12 | Dos gráficas correctas, pero a alguna le faltan títulos, unidades o la frase de lectura. Las conclusiones son correctas pero generales. |
| Suficiente | 6 a 9 | Hay dos gráficas, pero poco legibles o con tipo inadecuado, o las conclusiones no se apoyan en los datos. |
| Insuficiente | 0 a 5 | Hay menos de dos gráficas o no se entienden. |

### 6. Presentación (5 puntos)

| Nivel | Puntos | Descriptor |
|---|---|---|
| Excelente | 5 | Presenta en el tiempo asignado, con orden (pregunta, datos, método, hallazgo, límite), sin leer el código línea por línea, y responde preguntas. |
| Bueno | 4 | Orden claro, pero se pasa o se queda corto de tiempo, o responde parcialmente. |
| Suficiente | 2 a 3 | Presenta, pero sin estructura clara o centrada en el código. |
| Insuficiente | 0 a 1 | No presenta o no se puede seguir. |

## Sugerencias de calificación

Estas son sugerencias, la decisión final es del instructor.

- Si el notebook no corre con Run all, revisar cuánto falla. Un fallo menor se descuenta en documentación. Un fallo en la ingesta afecta casi todos los criterios.
- Si el alumno no entregó el avance de la sesión 9, no se penaliza aparte, pero se refleja en lo que logró terminar.
- Valorar el esfuerzo de usar un dataset propio (opción 3) si cumple todos los requisitos.
- Los puntos de presentación se dan el mismo día de la sesión 10.

## Lista de verificación para la revisión entre pares

Revisa el proyecto de tu pareja con esta lista. Haz Run all antes de contestar. Deja al menos tres comentarios en Deepnote: uno sobre algo que funciona, uno sobre algo que falta y una sugerencia concreta.

**Acceso y orden**
- [ ] El enlace abre sin pedir permisos.
- [ ] Run all termina sin errores.
- [ ] Las secciones siguen la plantilla (resumen, ingesta, calidad, gold, visualizaciones, hallazgos, límites).
- [ ] No hay celdas de prueba sueltas ni variables que dependan de celdas borradas.

**Ingesta**
- [ ] Se lee un Parquet o un CSV y se muestra el esquema y el número de filas.
- [ ] Existe la capa bronze con el dato crudo.

**Transformaciones**
- [ ] Existe la capa silver con tipos correctos.
- [ ] Hay al menos un JOIN de hechos con una dimensión.
- [ ] Hay al menos tres agregaciones.
- [ ] Existe la capa gold escrita en su carpeta.
- [ ] Correr el pipeline dos veces no duplica datos.

**Calidad de datos**
- [ ] Hay al menos tres validaciones y cada una dice por qué existe.
- [ ] Los registros inválidos van a cuarentena con el motivo.
- [ ] Se dice cuántos registros cayeron en cada regla.

**Documentación**
- [ ] Empieza con un resumen (pregunta, dataset, hallazgo, cómo reproducirlo).
- [ ] Cada sección tiene texto que explica el porqué, no solo el qué.
- [ ] Hay una sección de límites y siguientes pasos.

**Visualizaciones**
- [ ] Hay al menos dos gráficas con título y ejes con nombre.
- [ ] Cada una tiene una frase que dice qué se ve.
- [ ] Las conclusiones citan números de los datos.

**Tu retroalimentación**
- [ ] Escribí un comentario sobre algo que funciona.
- [ ] Escribí un comentario sobre algo que falta.
- [ ] Escribí una sugerencia concreta que se pueda aplicar hoy.

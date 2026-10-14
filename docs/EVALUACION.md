# Evaluación

## Pesos

| Componente | Peso |
|---|---|
| Participación y asistencia | 15% |
| Ejercicios y entregables semanales (sesiones 1 a 9) | 45% |
| Proyecto final | 40% |

Hay evaluación formativa continua: un quiz breve al inicio de las sesiones 3 y 5, y retroalimentación en vivo durante la práctica.

## Entregables por sesión

| Sesión | Entregable |
|---|---|
| 1 | Notebook propio ejecutado con el dataset cargado |
| 2 | Cuaderno de ejercicios resuelto |
| 3 | Tabla comparativa CSV vs. Parquet con explicación propia |
| 4 | 5 consultas SQL resueltas |
| 5 | Diagrama de star schema y 3 consultas con CTE o window |
| 6 | Pipeline lazy con explicación de qué optimizó el motor |
| 7 | Notebook con 3 análisis agregados y 1 join |
| 8 | Captura de la tabla creada y de una consulta ejecutada en Databricks |
| 9 | Pipeline con tres capas y al menos 3 validaciones |
| 10 | Proyecto final publicado y presentación |

## Tareas, variantes y calificación

El detalle de cada tarea, las variantes por alumno, la rúbrica semanal de 10 puntos y el proceso de calificación están en `docs/TAREAS.md`.

## Cómo recolectar el trabajo

Deepnote no califica automáticamente ni se integra con plataformas de cursos. Se usa esto:

- **Verificación inmediata:** cada notebook termina con `verificar_sesion_0N()`, que le dice al alumno qué le falta. Es retroalimentación, no calificación.
- **Código de entrega:** las tareas con variante imprimen una línea (por ejemplo `S04|V3|n=1086|ticket=43.25`) que el alumno pega en Google Forms. `scripts/variantes.py calificar` la compara con la clave.
- **Entrega:** el alumno comparte con el instructor el enlace de su proyecto con permiso de lectura y envía el enlace (formulario o chat). Para la sesión 8, una captura de pantalla.
- **Quizzes:** las preguntas de `docs/QUIZZES.md` se pasan a Google Forms. Forms califica automáticamente y entrega una hoja de cálculo.
- **Proyecto final:** rúbrica manual en `proyecto_final/RUBRICA.md`, 100 puntos.

## Proyecto final

Los requisitos, opciones de dataset, calendario y formato de entrega están en `proyecto_final/README.md`. La rúbrica con descriptores por nivel está en `proyecto_final/RUBRICA.md`.

| Criterio | Puntos |
|---|---|
| Ingesta y lectura correcta de datos | 15 |
| Transformaciones (joins, agregaciones, medallion) | 25 |
| Calidad de datos (validaciones) | 20 |
| Documentación y claridad narrativa | 20 |
| Visualizaciones e insights | 15 |
| Presentación | 5 |

## Registro de seguimiento sugerido

Una hoja de cálculo con una fila por alumno y una columna por sesión (asistencia, entregable, quiz), más la nota del proyecto final. Ahí se calcula el 15, 45 y 40 por ciento.

# Plantilla de guía de sesión

Cada archivo `docs/guia/S0X.md` (y `S10.md`) usa exactamente estas secciones, en este orden. `S01.md` es el ejemplo completo de referencia en tono, profundidad y formato.

## Reglas de estilo (obligatorias)

- Español de México, frases directas, vocabulario común y sencillo. Nada de lenguaje rebuscado.
- Usa comas para encadenar ideas. No uses guiones largos (el carácter de raya) como puntuación, ni en el texto ni en el código comentado. Usa comas, dos puntos o paréntesis.
- Usa bullets cuando ayuden. Las tablas solo para tiempos, quizzes y comparaciones.
- Todo el código va en bloques con lenguaje (` ```python `, ` ```sql `, ` ```bash `).
- No inventes cifras. Si un resultado numérico depende de los datos y no lo puedes verificar, escribe "verificar en la nube" en lugar de un número. Solo estas cifras están confirmadas: yellow_tripdata_2024-01.parquet tiene 2,964,624 filas y 19 columnas, taxi_zone_lookup.csv tiene 265 zonas.
- Dataset hilo conductor en todo el curso: NYC TLC Yellow Taxi enero 2024 más la tabla de zonas. URLs en `docs/DATASETS.md`.
- Versiones fijas: Python 3.12 o 3.13, Polars 1.43.2, DuckDB y Pandera la última estable, Plotly para gráficas.
- Todo corre en Deepnote (máquina Basic, 5 GB de RAM, apagado a los 15 minutos de inactividad). Excepción: la sesión 8 usa Databricks Free Edition (solo serverless).
- Los alumnos pueden llevarse todo el contenido, así que las soluciones sí van completas en la guía.

## Secciones

1. `# Sesión N: Título` y una ficha en tabla: semana, duración (150 min), notebook (`notebooks/S0N.deepnote`), datasets, cuentas necesarias, prerrequisitos.
2. `## Objetivos`: 3 a 4 bullets, formato "Al terminar, el alumno puede...".
3. `## Antes de la sesión`: checklist del instructor (qué abrir, qué probar, qué imprimir o compartir, qué avisar a los alumnos).
4. `## Conceptos y definiciones`: TODAS las definiciones de la sesión, una por término, en este formato:
   - **Término**: definición clara en 1 a 3 frases. *Ejemplo o analogía:* una línea. *Error común:* una línea.
   Cubre cada tema del temario de la sesión (los numerados como 4.1, 4.2, etc. en `docs/referencia/CONTEXTO_BASE_agosto.md`).
5. `## Guion minuto a minuto`: tabla de tiempos del temario y, debajo, una subsección por bloque con:
   - **Qué decir**: los puntos clave, redactados como los diría el instructor.
   - **Qué hacer en pantalla**: pasos concretos en Deepnote o en el notebook.
   - **Pregunta de comprobación**: una pregunta para verificar que entendieron, con la respuesta esperada.
6. `## Código del live coding`: el código completo, comentado, en el orden exacto en que se escribe en clase. Cada bloque dice a qué parte del guion corresponde.
7. `## Ejercicios`: cada uno con enunciado, pista, solución completa y qué debe ver el alumno al ejecutarla.
8. `## Quiz`: 5 preguntas de opción múltiple (4 opciones), con respuesta correcta y una línea de justificación. Pensadas para pasarse a Google Forms.
9. `## Errores comunes`: tabla con síntoma, causa y cómo resolverlo en clase.
10. `## Cierre y tarea`: qué se resume al final, la tarea con soluciones y cómo se entrega.
11. `## Especificación del notebook`: lista ordenada de los bloques del `.deepnote` para que Claude Code lo construya: tipo de bloque, contenido o referencia al código de la guía, y la celda final `verificar_sesion_0N()` con los asserts exactos. Sigue el patrón de `notebooks/S01.deepnote` (H1, callout de "Run all", secciones H2, ejercicio con `...`, verificación).
12. `## Para profundizar`: 3 a 5 enlaces o recursos (documentación oficial).

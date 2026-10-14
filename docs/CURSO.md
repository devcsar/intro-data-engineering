# Curso: Introducción a la Ingeniería de Datos (Impact Click)

Este es el documento de entrada del repo. Explica qué es el curso, cómo está armado y dónde vive cada cosa.

## Ficha

| Campo | Valor |
|---|---|
| Nombre de trabajo | Ingeniería de Datos desde Cero: del CSV al Lakehouse |
| Organiza | Fundación Impact Click |
| Duración | 10 sesiones de 150 minutos, 25 horas en total |
| Cadencia | 2 sesiones por semana, 5 semanas |
| Público | Personas que empiezan en tecnología, sin experiencia previa |
| Grupo previsto | 10 alumnos |
| Idioma | Español |
| Entorno | Deepnote en el navegador para todo el curso. La sesión 8 usa también Databricks Free Edition |
| Dataset | NYC TLC Yellow Taxi, enero 2024, más la tabla de zonas |
| Dinámica | El instructor programa en vivo y los alumnos ejecutan el mismo notebook al mismo tiempo |

## Cómo está armado

- **Una guía por sesión** en `docs/guia/`. Cada guía trae objetivos, definiciones, guion minuto a minuto, código del live coding, ejercicios con solución, quiz, errores comunes, tarea y la especificación del notebook.
- **Un notebook por sesión** en `notebooks/` (formato `.deepnote`). Es lo que los alumnos ejecutan.
- **Dos proyectos en Deepnote** para los alumnos, generados con `scripts/build_curso.py`:
  - "Curso Data Engineering - Impact Click": las sesiones 1 a 9, un notebook por sesión.
  - "Proyecto final - Impact Click": la sesión 10 y la plantilla del proyecto final.
- Se usan solo 2 proyectos porque la cuenta Free de Deepnote permite 5 por workspace.

## Mapa de sesiones

| Sem. | Ses. | Tema | Herramientas | Guía | Notebook |
|---|---|---|---|---|---|
| 1 | 1 | Introducción a la ingeniería de datos y Deepnote | Deepnote, Polars (lectura) | [S01](guia/S01.md) | `S01.deepnote` |
| 1 | 2 | Python esencial para datos | Python | [S02](guia/S02.md) | `S02.deepnote` |
| 2 | 3 | Fundamentos de datos y formatos | Polars, PyArrow | [S03](guia/S03.md) | `S03.deepnote` |
| 2 | 4 | SQL I: consultas, joins y agregaciones | DuckDB, bloques SQL | [S04](guia/S04.md) | `S04.deepnote` |
| 3 | 5 | SQL II y Data Warehousing | DuckDB | [S05](guia/S05.md) | `S05.deepnote` |
| 3 | 6 | Polars I: DataFrames y evaluación lazy | Polars | [S06](guia/S06.md) | `S06.deepnote` |
| 4 | 7 | Polars II: transformaciones y agregaciones a escala | Polars, Plotly | [S07](guia/S07.md) | `S07.deepnote` |
| 4 | 8 | Introducción a Databricks y lakehouse | Databricks Free Edition | [S08](guia/S08.md) | `S08.deepnote` y `databricks/S08_notebook.py` |
| 5 | 9 | Pipeline ETL/ELT, calidad de datos y reproducibilidad | Polars, Pandera, uv | [S09](guia/S09.md) | `S09.deepnote` y `proyecto_uv/` |
| 5 | 10 | Proyecto final documentado en Deepnote | Todo el stack | [S10](guia/S10.md) | `S10.deepnote` y `proyecto_final/` |

## Mapa del repo

- `docs/guia/`: guías del instructor, una por sesión.
- `docs/GUIA_DEL_INSTRUCTOR.md`: cómo dar el curso, antes, durante y después de cada sesión.
- `docs/GLOSARIO.md`: todas las definiciones del curso, por sesión.
- `docs/QUIZZES.md`: todas las preguntas, listas para Google Forms.
- `docs/EVALUACION.md`: pesos, entregables y cómo recolectar el trabajo.
- `docs/TAREAS.md`: tareas con variantes por alumno, rúbrica semanal y calificación.
- `docs/DATASETS.md`: datasets, URLs y puntos de enseñanza.
- `docs/LIMITACIONES.md`: límites de Deepnote Free y riesgos con 10 alumnos.
- `docs/PRUEBA_DE_CLASE.md`: ensayo completo antes de la primera clase.
- `docs/FLUJO_DE_TRABAJO.md`: cómo crear, validar, publicar y mantener el contenido.
- `docs/referencia/CONTEXTO_BASE_agosto.md`: el documento de contexto original (agosto 2026), con el temario detallado.
- `notebooks/`: los notebooks `.deepnote` y `requirements.txt`.
- `databricks/`: notebook para importar en Databricks (sesión 8).
- `proyecto_uv/`: pipeline como script y proyecto de uv (sesión 9).
- `proyecto_final/`: instrucciones y rúbrica del proyecto final.
- `scripts/`: `dn` (validar y subir), `nb.py` (ayudante para armar notebooks), `build_curso.py` (arma los dos proyectos), `compilar_docs.py` (regenera glosario y quizzes), `variantes.py` (variantes, clave y calificación).
- `dist/`: los archivos `.deepnote` que se suben a Deepnote, generados por `build_curso.py`.

## Qué cambió respecto al documento de agosto

El documento `docs/referencia/CONTEXTO_BASE_agosto.md` sigue siendo la referencia del temario, pero estas decisiones lo reemplazan:

- **Cuentas de los alumnos:** se parte de que usan cuenta Free de Deepnote. El plan de Educación se solicita a help@deepnote.com pero no se da por hecho.
- **Reparto:** los alumnos entran como Viewers y duplican el proyecto a su workspace. Se reparten 2 proyectos, no uno por módulo.
- **Dependencias:** van en `requirements.txt` como archivo del proyecto, no en la configuración del entorno, porque esa no se copia al duplicar. La lista actual es `polars==1.43.2`, `duckdb`, `pandera`, `plotly` y `pyarrow`.
- **Polars:** se fija la versión 1.43.2 aunque ya existe Polars 2.0. Hay que revisar antes de cada cohorte.
- **Bloques SQL:** los bloques SQL nativos de Deepnote solo corren en la nube. En local se usa `duckdb.sql()`.
- **Contenido abierto:** los alumnos pueden llevarse todo el material, incluidas las soluciones.

## Pendientes

- Confirmar en la nube los valores marcados como "verificar en la nube" en las guías y registrarlos en `docs/REGISTRO_VERIFICACION.md`.
- Ensayar `databricks/S08_notebook.py` en una cuenta Free de Databricks.
- Decidir cómo se reparten las presentaciones de la sesión 10 con 10 alumnos (ver `docs/GUIA_DEL_INSTRUCTOR.md`).
- Solicitar el plan de Educación de Deepnote.
- Definir fechas, sede y horario.

# Contexto del proyecto, Curso "Ingeniería de Datos desde Cero"

> Documento de contexto técnico y fuente de verdad del proyecto. Contiene decisiones de diseño, temario detallado, stack por sesión, requisitos y riesgos.

| Campo | Valor |
|---|---|
| Nombre | Ingeniería de Datos desde Cero: del CSV al Lakehouse |
| Modalidad | Curso en vivo (presencial o remoto) |
| Duración | 10 sesiones × 150 min = **25 horas** |
| Cadencia | 2 sesiones por semana, 5 semanas |
| Público | Principiantes absolutos en tecnología |
| Entorno base | **Deepnote** (navegador, sin instalación local) |
| Ubicación | Ciudad de México |
| Versión del temario | v2, Deepnote-first |
| Última actualización | Agosto 2026 |
| Estado | Temario cerrado, pendiente validación con organizadores |

---

## 1. Historial de decisiones

### v1 → v2: migración a Deepnote como entorno base

**Solicitud del cliente:** que todo el trabajo técnico ocurra en Deepnote, para lidiar lo menos posible con distintos entornos y sistemas operativos. Deepnote debía pasar del final del curso al inicio, como herramienta y entorno de trabajo.

**Evaluación:** aprobado. Es una mejora clara para este público.

**Hallazgo que reforzó la decisión:** Deepnote ofrece un **plan de Educación 100% gratuito** para estudiantes, docentes e investigadores, que incluye la mayoría de las funciones del plan Team salvo máquinas avanzadas, scheduling y Deepnote AI. Es extensible a MOOCs y ONGs aunque no exista correo institucional. Esto elimina el techo de 3 editores / 5 proyectos del plan Free, que era la principal objeción estructural.

**Refinamiento aplicado:** Deepnote no se movió íntegro a la sesión 1. Se dividió en dos bloques:
- **Deepnote como entorno** (~45 min, sesión 1): crear proyecto, ejecutar celdas, subir archivos.
- **Deepnote como herramienta de colaboración y publicación** (~25 min, sesión 10): comentarios, versiones, permisos, narrativa, reproducibilidad, publicación.

Enseñar historial de versiones el día uno es peso muerto: no hay nada sobre qué colaborar todavía.

**Efecto secundario:** la división liberó una sesión completa, que se asignó a **fundamentos de Python**, el riesgo #1 del diseño v1, que carecía de sesión de Python pese a que Polars y los pipelines lo asumen. El pre-work asíncrono pasa de obligatorio a opcional, lo que reduce la barrera de inscripción.

**Costo asumido conscientemente:** uv pasa de sesión completa a bloque de 20 min en la sesión 9.

### Decisiones vigentes de v1

| Decisión | Razón |
|---|---|
| **Es Data Engineering, no ingeniería de software** | El brief original decía "ingeniería de software", pero los segmentos son de ingeniería de datos. Se ajustó el nombre para no crear expectativas equivocadas. |
| **DuckDB como motor SQL** | Cero configuración, lee Parquet/CSV directo desde SQL, corre in-process. Superior a SQLite para analítica; evita levantar PostgreSQL. |
| **Polars sobre pandas** | Sin índice (fuente enorme de confusión para principiantes), API de expresiones consistente, separación clara eager/lazy. |
| **Databricks como tour, no taller** | Free Edition es serverless-only: no se pueden crear ni configurar clusters. |
| **Un solo dataset hilo conductor** | Reduce carga cognitiva: no reaprenden el dominio en cada sesión, solo la herramienta nueva. |
| **~35% teoría / 55% práctica / 10% descansos** | Basado en evidencia de carga cognitiva en novatos: worked examples, live coding, ejercicios progresivos. |

---

## 2. Stack y versiones verificadas (agosto 2026)

| Herramienta | Versión | Rol | Notas |
|---|---|---|---|
| **Deepnote** | Plan Educación | Entorno base de todo el curso | Solicitar en Settings → Upgrade → Education plan |
| Python | 3.11+ | Lenguaje base | Provisto por Deepnote |
| **Polars** | 1.43.2 | Procesamiento de DataFrames | Evitar versiones "yanked" en PyPI: 1.43.0, 1.41.0, 1.39.2, 1.38.0, 1.36.0 (regresión en `unpivot`), 1.35.0 |
| **DuckDB** | última estable | Motor SQL analítico | También disponible vía bloques SQL nativos de Deepnote |
| **Pandera** | última estable | Validación de calidad | Usar backend `pandera.polars` |
| **Databricks** | Free Edition | Plataforma lakehouse | Sesión 8 únicamente |
| uv | 0.12+ | Gestión local de proyectos | Solo bloque demostrativo en sesión 9. Desde 0.12.0 `uv init` crea layout `src/`; usar `--no-package` para principiantes |
| PyArrow | implícito | Formato columnar en memoria | Viene con Polars |
| Plotly / Matplotlib | última | Visualización | Sesión 7 en adelante |

**Verificar antes de cada cohorte:** `pl.__version__` y los límites vigentes de Deepnote y Databricks. El ecosistema se mueve rápido.

---

## 3. Deepnote: configuración del aula

### Plan de Educación

- 100% gratuito para estudiantes, docentes e investigadores con correo institucional.
- Extensible a MOOCs y ONGs sin correo institucional (verificar caso con soporte).
- Incluye la mayoría de funciones del plan Team **excepto**: máquinas avanzadas, scheduling y Deepnote AI.
- Cada miembro obtiene horas ilimitadas de máquina Basic (5 GB RAM, 2 vCPU).
- Ruta alterna: GitHub Student Developer Pack, que habilita colaboración con número ilimitado de docentes y estudiantes.

### Límites del plan Free (si no se obtiene el de Educación)

- 3 editores y 5 proyectos por workspace
- Máquina Basic: 5 GB RAM, 2 vCPU
- Historial de revisiones: 7 días
- Apagado tras 15 min de inactividad y tras 8 h de ejecución continua
- Team: $39/editor/mes anual, $49 mensual

### Montaje operativo

1. Solicitar el plan de Educación **antes** de comprometerse con el diseño.
2. Un workspace del curso con proyectos plantilla que los alumnos **dupliquen** a su espacio.
3. Agrupar por módulo, no por sesión: un proyecto por bloque temático (Python, SQL, Polars, Pipeline, Proyecto final).
4. Invitar a los alumnos como Viewers al notebook de demostración del instructor.
5. **Ritual de cada sesión: "Run all" al empezar.** Resuelve el apagado por inactividad y enseña reproducibilidad.
6. Ensayar el plan B en Google Colab antes de que arranque el curso.

### Consideración de memoria

El dataset de taxis ocupa ~390 MB en memoria (2.96M filas × 19 columnas), lo que cabe holgadamente en los 5 GB de la máquina Basic. Varios meses combinados no caben. **Esto es una ventaja pedagógica:** obliga a usar `scan_parquet` y evaluación lazy desde el inicio, que es el hábito correcto.

---

## 4. Datasets

### 4.1 Hilo conductor: NYC TLC Yellow Taxi

| Archivo | Contenido | Tamaño |
|---|---|---|
| `yellow_tripdata_2024-01.parquet` | 2,964,624 filas × 19 columnas | ~50 MB |
| `taxi_zone_lookup.csv` | 265 zonas (LocationID, Borough, Zone, service_zone) | ~12 KB |

- Base: `https://d37ci6vzurychx.cloudfront.net/trip-data/`
- Zonas: `https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv`

**Por qué:** ya viene en Parquet (justifica el formato sin trabajo previo), tiene hecho + dimensión natural para joins, es lo bastante grande para justificar lazy y lo bastante chico para la máquina Basic de Deepnote.

**Puntos de enseñanza que regala:**
- `LocationID` 264 y 265 son "Unknown" → ilustra por qué un `INNER JOIN` pierde filas.
- **Schema drift entre meses:** `passenger_count`, `RatecodeID` y `congestion_surcharge` aparecen como `DOUBLE` o `INT64` según el archivo; `airport_fee` a veces va capitalizado. Los archivos 2025+ agregan `cbd_congestion_fee` (20 columnas vs 19). Excelente material para la sesión de calidad de datos, pero causa errores al combinar meses sin cuidado.

### 4.2 Alternativa local (CDMX): Ecobici

- Portal: `datos.cdmx.gob.mx`
- Uso: gancho de motivación y opción de proyecto final.
- **Verificar disponibilidad antes de cada cohorte.** Los datos históricos tenían actualizaciones con fechas 2023-2024. El feed en tiempo real usa GBFS (`gbfs.mex.lyftbikes.com`) y no entrega histórico.

### 4.3 Otras fuentes para proyecto final
`inegi.org.mx/datosabiertos` · `datos.gob.mx`

---

## 5. Temario detallado

### SEMANA 1

#### Sesión 1, Introducción a Data Engineering + Deepnote como entorno de trabajo

**Objetivos:** explicar qué hace un ingeniero de datos · operar Deepnote a nivel básico · ejecutar su primer notebook con datos reales.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-15 | 15 | Bienvenida, encuadre y demo del proyecto final |
| 15-45 | 30 | Teoría: qué hace un ingeniero de datos · anatomía de un pipeline · DE vs. analista vs. científico · panorama laboral |
| 45-75 | 30 | Deepnote en vivo: alta de cuenta, plan de Educación, workspace, proyecto, notebook, celdas |
| 75-85 | 10 | Descanso |
| 85-115 | 30 | Live coding: orden de ejecución, ritual "Run all", apagado por inactividad, subir archivos, primer `read_csv` |
| 115-140 | 25 | Práctica: duplicar notebook plantilla y explorar el dataset |
| 140-150 | 10 | Cierre, presentación del dataset y tarea |

**Contenido:** 1.1 Qué hace un ingeniero de datos · 1.2 Anatomía de un pipeline · 1.3 DE vs. analista vs. científico de datos · 1.4 Notebooks en la nube · 1.5 Workspaces, proyectos y notebooks · 1.6 Celdas de código y Markdown · 1.7 Orden de ejecución y reproducibilidad · 1.8 Carga de archivos y primera lectura.

**Entregable:** notebook propio ejecutado con el dataset cargado.
**Tarea:** 10 ejercicios cortos de Python.
**Fricción esperada:** verificación del plan de Educación; confusión con el orden de ejecución de celdas.

---

#### Sesión 2, Python esencial para datos

**Objetivos:** usar variables, listas, diccionarios, ciclos y funciones · leer e interpretar un traceback.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Dudas de Deepnote y revisión de tarea |
| 10-35 | 25 | Variables, tipos y operadores |
| 35-60 | 25 | Listas y diccionarios: crear, indexar, recorrer |
| 60-70 | 10 | Descanso |
| 70-95 | 25 | Control de flujo: `if/else` y `for` |
| 95-120 | 25 | Funciones y módulos |
| 120-140 | 20 | Taller de errores: reparar 5 celdas rotas a propósito |
| 140-150 | 10 | Cierre y tarea |

**Contenido:** 2.1 Variables y tipos (int, float, str, bool) · 2.2 Operadores · 2.3 Listas · 2.4 Diccionarios · 2.5 Condicionales · 2.6 Ciclos `for` · 2.7 Funciones, parámetros y retorno · 2.8 Importar módulos · 2.9 Lectura de tracebacks.

**Entregable:** cuaderno de ejercicios resuelto.
**Nota didáctica:** el taller de errores es deliberado. Enseñar a leer tracebacks en la sesión 2 ahorra decenas de horas de soporte en las sesiones 6-9.

---

### SEMANA 2

#### Sesión 3, Fundamentos de datos y formatos (CSV, JSON, Parquet)

**Objetivos:** distinguir almacenamiento por filas vs. columnas · explicar compresión, tipado y esquema · convertir formatos y medir la diferencia.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Quiz de Python y repaso |
| 10-40 | 30 | Teoría: datos estructurados/semi/no estructurados · esquema y tipado · CSV y JSON a fondo |
| 40-50 | 10 | Descanso |
| 50-80 | 30 | Teoría + demo: Parquet, columnar vs. filas, compresión, esquema embebido, column pruning. Mención de Arrow, Delta e Iceberg |
| 80-120 | 40 | Práctica: leer Parquet, inspeccionar esquema, convertir a CSV, comparar |
| 120-140 | 20 | Ejercicio: reporte comparativo con conclusión escrita |
| 140-150 | 10 | Cierre y tarea |

**Contenido:** 3.1 Datos estructurados, semiestructurados y no estructurados · 3.2 Esquema, tipado y metadatos · 3.3 CSV: delimitadores, encabezados, encoding · 3.4 JSON y NDJSON · 3.5 Parquet: columnar, compresión, esquema embebido · 3.6 Column pruning y predicate pushdown · 3.7 Apache Arrow · 3.8 Delta Lake e Iceberg (panorama).

**Entregable:** tabla comparativa CSV vs. Parquet con explicación propia.
**Fricción esperada:** intentar abrir Parquet en Excel; confundir JSON con NDJSON.

---

#### Sesión 4, SQL I: queries, joins y agregaciones

**Objetivos:** escribir SELECT/WHERE/ORDER BY · unir tablas con JOIN · agregar con GROUP BY.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Encuadre: por qué SQL sigue siendo la habilidad más solicitada |
| 10-35 | 25 | Modelo relacional · DuckDB y bloques SQL nativos de Deepnote |
| 35-65 | 30 | Live coding: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, nulos |
| 65-75 | 10 | Descanso |
| 75-110 | 35 | Joins `INNER` y `LEFT` · hecho + dimensión · filas huérfanas |
| 110-140 | 30 | Agregaciones y `GROUP BY` · `HAVING` · ejercicio top 10 |
| 140-150 | 10 | Cierre y tarea |

**Contenido:** 4.1 Tablas, filas, columnas y claves · 4.2 DuckDB y bloques SQL de Deepnote · 4.3 `SELECT`, `FROM`, alias · 4.4 `WHERE` y operadores · 4.5 `ORDER BY`, `LIMIT`, `DISTINCT` · 4.6 Manejo de nulos · 4.7 `INNER JOIN` y `LEFT JOIN` · 4.8 `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` · 4.9 `GROUP BY` y `HAVING`.

**Entregable:** 5 consultas resueltas.
**Fricción esperada:** olvidar `GROUP BY` con agregados; confundir INNER vs LEFT JOIN.

---

### SEMANA 3

#### Sesión 5, SQL II + Data Warehousing

**Objetivos:** usar CTEs y window functions · explicar OLTP vs. OLAP · describir modelado dimensional y medallion.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Quiz de repaso |
| 10-40 | 30 | Subconsultas · CTEs con `WITH` · `CASE WHEN` |
| 40-60 | 20 | Window functions: `ROW_NUMBER`, `RANK`, `SUM OVER` |
| 60-70 | 10 | Descanso |
| 70-90 | 20 | OLTP vs. OLAP · normalización vs. desnormalización |
| 90-115 | 25 | Modelado dimensional: hechos, dimensiones, granularidad, star vs. snowflake |
| 115-130 | 15 | Lakehouse y medallion (bronze/silver/gold) · ETL vs. ELT |
| 130-145 | 15 | Práctica: diagramar el star schema y crearlo con CTEs |
| 145-150 | 5 | Cierre y tarea |

**Contenido:** 5.1 Subconsultas · 5.2 CTEs · 5.3 `CASE WHEN` · 5.4 Window functions · 5.5 OLTP vs. OLAP · 5.6 Normalización vs. desnormalización · 5.7 Tabla de hechos y granularidad · 5.8 Tablas de dimensión · 5.9 Star y snowflake schema · 5.10 Lakehouse · 5.11 Arquitectura medallion · 5.12 ETL vs. ELT.

**Entregable:** diagrama de star schema + 3 consultas con CTE o window.
**Fricción esperada:** confundir dimensión con hecho; sobre-normalizar.

---

#### Sesión 6, Polars I: DataFrames y evaluación lazy

**Objetivos:** manipular DataFrames con expresiones y contextos · explicar eager vs. lazy · construir un pipeline con `scan_parquet` + `collect`.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Cuándo SQL y cuándo DataFrame · por qué Polars y no pandas |
| 10-40 | 30 | `DataFrame` y `Series` · tipos y esquema · ausencia de índice · `pl.col` |
| 40-50 | 10 | Descanso |
| 50-85 | 35 | Contextos `select`, `filter`, `with_columns` · encadenamiento (live coding) |
| 85-115 | 30 | Eager vs. lazy · `read_` vs. `scan_` · `collect()` y `explain()` · por qué con 5 GB lazy no es opcional |
| 115-140 | 25 | Práctica: pipeline lazy con filtro y columna de duración |
| 140-150 | 10 | Cierre y tarea |

**Contenido:** 6.1 Polars vs. pandas · 6.2 Arrow y ejecución paralela · 6.3 `Series` y `DataFrame` · 6.4 Tipos y esquema · 6.5 Ausencia de índice · 6.6 Expresiones (`pl.col`) · 6.7 Contexto `select` · 6.8 Contexto `filter` · 6.9 Contexto `with_columns` · 6.10 `read_` vs. `scan_` · 6.11 `LazyFrame` y plan de consulta · 6.12 `collect()` y `explain()` · 6.13 Projection y predicate pushdown.

**Entregable:** pipeline lazy con explicación de qué optimizó el motor.
**Fricción esperada:** olvidar `.collect()`; buscar el índice de pandas; usar lambdas en vez de expresiones nativas.

---

### SEMANA 4

#### Sesión 7, Polars II: transformaciones y agregaciones a escala

**Objetivos:** agregar con `group_by`/`agg` · hacer joins en Polars · procesar volúmenes con streaming.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Repaso de Polars I |
| 10-35 | 25 | `cast`, namespace `.dt`, namespace `.str`, nulos y duplicados |
| 35-65 | 30 | `group_by` + `agg` con múltiples métricas · alias · ordenamiento |
| 65-75 | 10 | Descanso |
| 75-100 | 25 | Joins (`inner`, `left`, `anti`) · window functions con `.over()` |
| 100-125 | 25 | Práctica: análisis por zona, hora del día y método de pago |
| 125-140 | 15 | Motor streaming y lectura con globs |
| 140-150 | 10 | Cierre y tarea |

**Contenido:** 7.1 Casteo de tipos · 7.2 Namespace `.dt` · 7.3 Namespace `.str` · 7.4 Nulos y duplicados · 7.5 `group_by` + `agg` · 7.6 Múltiples métricas y alias · 7.7 Joins en Polars · 7.8 `left_on` / `right_on` · 7.9 Window functions con `.over()` · 7.10 Motor streaming · 7.11 Lectura de múltiples archivos.

**Entregable:** notebook con 3 análisis agregados y 1 join.
**Fricción esperada:** nombres de columnas tras join; esperar orden sin `sort`.

---

#### Sesión 8, Introducción a Databricks: lakehouse y notebooks

**Objetivos:** navegar Databricks Free Edition · explicar lakehouse y Unity Catalog · ejecutar una consulta y un notebook serverless.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | De tu notebook personal a una plataforma empresarial |
| 10-35 | 25 | Qué es Databricks · Free Edition: qué incluye, qué no, por qué serverless-only · registro |
| 35-60 | 25 | Lakehouse: Delta Lake, ACID, tablas gestionadas, time travel · Unity Catalog |
| 60-70 | 10 | Descanso |
| 70-105 | 35 | Práctica: subir Parquet, crear tabla, consultar con SQL |
| 105-130 | 25 | Notebook serverless: PySpark básico, agregación, visualización · Genie |
| 130-145 | 15 | Comparativa: cuándo Deepnote, cuándo Databricks, cuándo máquina propia |
| 145-150 | 5 | Cierre + **asignación del proyecto final** |

**Contenido:** 8.1 Qué es Databricks · 8.2 Free Edition: alcances y límites · 8.3 Delta Lake y ACID · 8.4 Tablas gestionadas vs. externas · 8.5 Time travel · 8.6 Unity Catalog · 8.7 Compute serverless · 8.8 SQL editor y SQL warehouse · 8.9 PySpark básico · 8.10 Genie (panorama) · 8.11 Criterios de elección de plataforma.

**Entregable:** captura de la tabla creada y una consulta ejecutada.
**Nota:** sesión más ligera que en v1 porque ya dominan el concepto de notebook en la nube; el tiempo se invierte en conceptos de lakehouse, no en explicar la interfaz.
**Fricción esperada:** buscar cómo crear un cluster (no existe); exceder cuota y perder compute el resto del día.

---

### SEMANA 5

#### Sesión 9, Pipeline ETL/ELT + calidad de datos

**Objetivos:** construir un pipeline bronze→silver→gold · aplicar validaciones · entender por qué un pipeline productivo no vive en un notebook.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-10 | 10 | Encuadre y repaso de medallion |
| 10-35 | 25 | ETL vs. ELT · idempotencia · cargas completas vs. incrementales · orquestación (panorama) |
| 35-60 | 25 | Calidad de datos · validaciones con Polars · esquemas con Pandera · registros que fallan |
| 60-70 | 10 | Descanso |
| 70-110 | 40 | Práctica: pipeline bronze → silver → gold con 3 validaciones |
| 110-125 | 15 | Logging y métricas de ejecución |
| 125-145 | 20 | **Bloque uv:** escribir un `.py` desde la terminal de Deepnote, archivo de dependencias, equivalente local con uv |
| 145-150 | 5 | Cierre y avance del proyecto |

**Contenido:** 9.1 ETL vs. ELT · 9.2 Batch vs. streaming (panorama) · 9.3 Capas bronze/silver/gold · 9.4 Idempotencia · 9.5 Cargas incrementales · 9.6 Dimensiones de calidad de datos · 9.7 Validaciones con Polars · 9.8 Esquemas con Pandera · 9.9 Quarantine de registros inválidos · 9.10 Logging y métricas · 9.11 Orquestadores (panorama) · 9.12 Del notebook al script `.py` · 9.13 Gestión de dependencias y uv.

**Entregable:** pipeline con tres capas y al menos 3 validaciones.
**Fricción esperada:** no manejar nulos antes de validar; validaciones demasiado estrictas.

---

#### Sesión 10, Proyecto final documentado en Deepnote

**Objetivos:** documentar y publicar trabajo de forma profesional · integrar lo aprendido · presentar resultados.

| Tiempo | Dur. | Bloque |
|---|---|---|
| 0-15 | 15 | Repaso integrador |
| 15-40 | 25 | **Colaboración y publicación en Deepnote:** comentarios, historial de versiones, permisos, narrativa en Markdown, orden de ejecución, publicación |
| 40-50 | 10 | Descanso |
| 50-55 | 5 | Rúbrica y formato de entrega |
| 55-120 | 65 | Taller asistido con revisión entre pares |
| 120-145 | 25 | Presentaciones de 3-5 min |
| 145-150 | 5 | Cierre y ruta siguiente |

**Contenido:** 10.1 Comentarios y revisión entre pares · 10.2 Historial de versiones · 10.3 Permisos y compartición · 10.4 Narrativa en Markdown · 10.5 Orden de ejecución y estado oculto · 10.6 Publicación de resultados · 10.7 Integración del pipeline completo · 10.8 Presentación de resultados · 10.9 Ruta de aprendizaje posterior.

**Entregable:** proyecto final publicado en Deepnote + presentación.
**Nota:** el proyecto se asigna al cierre de la sesión 8 para que lleguen a la 10 con avance, no empezando de cero.

---

## 6. Tecnologías por sesión

| Sem. | Ses. | Tema | Stack | Entorno |
|---|---|---|---|---|
| 1 | 1 | Intro DE + Deepnote | **Deepnote**, Polars (lectura) | Navegador |
| 1 | 2 | Python esencial | **Python**, Deepnote | Navegador |
| 2 | 3 | Formatos | **Polars** (I/O), PyArrow | Navegador |
| 2 | 4 | SQL I | **DuckDB**, bloques SQL de Deepnote | Navegador |
| 3 | 5 | SQL II + DWH | **DuckDB**, diagramación | Navegador |
| 3 | 6 | Polars I | **Polars** (API completa) | Navegador |
| 4 | 7 | Polars II | **Polars** (streaming), Plotly | Navegador |
| 4 | 8 | Databricks | **Databricks Free Edition**, Spark SQL, PySpark, Delta, Unity Catalog | Navegador |
| 5 | 9 | ETL/ELT | Polars, DuckDB, **Pandera**, `logging`, terminal, uv (demo) | Navegador |
| 5 | 10 | Proyecto | Todo el stack | Navegador |

**Nota:** las 10 sesiones ocurren en el navegador. No hay instalación local obligatoria en ningún momento del curso.

### Cuentas necesarias

| Servicio | Crear antes de | Costo |
|---|---|---|
| Deepnote (plan Educación) | Sesión 1 | Gratis |
| Databricks Free Edition | Sesión 8 | Gratis |

---

## 7. Requisitos técnicos de los participantes

Al ser un curso 100% en navegador, los requisitos son mínimos:

| Componente | Requisito |
|---|---|
| Equipo | Cualquier laptop o desktop con navegador moderno (incluye Chromebook) |
| Navegador | Chrome o Edge actualizado (recomendados sobre Safari y Firefox) |
| RAM local | 4 GB suficientes |
| Internet | **25 Mbps estables**, es el requisito crítico |
| Sistema operativo | Indistinto |
| Permisos de administrador | **No requeridos** |
| Cuenta de correo | Para registro en Deepnote y Databricks |

**Nuevo cuello de botella:** el ancho de banda de la sede. Con 15 personas en notebooks en la nube simultáneamente, es la variable que puede arruinar una sesión. Medir antes de comprometer el lugar.

---

## 8. Distribución de horas

| Bloque temático | Sesiones | Horas |
|---|---|---|
| Fundamentos y entorno (DE + Deepnote + Python) | 1-2 | 5.0 |
| Datos y formatos | 3 | 2.5 |
| SQL y Data Warehousing | 4-5 | 5.0 |
| Polars | 6-7 | 5.0 |
| Plataformas (Databricks) | 8 | 2.5 |
| Pipelines y calidad de datos | 9 | 2.5 |
| Documentación y proyecto final | 10 | 2.5 |
| **Total** | **10** | **25.0** |

**Balance:** ~35% exposición, ~55% práctica y live coding, ~10% descansos y transiciones.
**Descansos:** uno de 10 min por sesión, entre los minutos 40 y 85 según carga del bloque.

---

## 9. Código clave de referencia

### Sesión 3, Formatos
```python
import polars as pl
df = pl.read_parquet("yellow_tripdata_2024-01.parquet")
print(df.schema)   # tipos por columna
print(df.shape)    # (2964624, 19)
df.write_csv("taxi.csv")   # comparar tamaño en disco
```

### Sesión 4, SQL con DuckDB
```python
import duckdb
con = duckdb.connect()
con.sql("""
  SELECT PULocationID, COUNT(*) AS viajes, AVG(trip_distance) AS dist_prom
  FROM 'yellow_tripdata_2024-01.parquet'
  GROUP BY PULocationID
  ORDER BY viajes DESC
  LIMIT 10
""").show()
```
```sql
SELECT z.Borough, COUNT(*) AS viajes
FROM 'yellow_tripdata_2024-01.parquet' t
JOIN 'taxi_zone_lookup.csv' z ON t.PULocationID = z.LocationID
GROUP BY z.Borough
ORDER BY viajes DESC;
```

### Sesión 5, CTE + window
```sql
WITH viajes_por_dia AS (
  SELECT CAST(tpep_pickup_datetime AS DATE) AS dia,
         COUNT(*) AS n_viajes,
         SUM(total_amount) AS ingreso
  FROM 'yellow_tripdata_2024-01.parquet'
  GROUP BY 1
)
SELECT dia, n_viajes, ingreso,
       RANK() OVER (ORDER BY ingreso DESC) AS ranking
FROM viajes_por_dia
ORDER BY ranking;
```

### Sesión 6, Polars lazy
```python
import polars as pl

lf = (
    pl.scan_parquet("yellow_tripdata_2024-01.parquet")
      .filter(pl.col("trip_distance") > 0)
      .with_columns(
          (pl.col("tpep_dropoff_datetime") - pl.col("tpep_pickup_datetime"))
          .dt.total_minutes().alias("duracion_min")
      )
      .select("PULocationID", "trip_distance", "total_amount", "duracion_min")
)
df = lf.collect()   # aquí se ejecuta
```

### Sesión 7, Agregaciones y streaming
```python
import polars as pl

zonas = pl.read_csv("taxi_zone_lookup.csv")

resultado = (
    pl.scan_parquet("yellow_tripdata_2024-01.parquet")
      .filter(pl.col("total_amount") > 0)
      .join(zonas.lazy(), left_on="PULocationID", right_on="LocationID", how="left")
      .group_by("Borough")
      .agg(
          pl.len().alias("n_viajes"),
          pl.col("total_amount").mean().alias("ticket_promedio"),
          pl.col("trip_distance").sum().alias("millas_totales"),
      )
      .sort("n_viajes", descending=True)
      .collect(engine="streaming")
)
```

### Sesión 8, Databricks
```sql
SELECT payment_type, COUNT(*) AS viajes, ROUND(AVG(total_amount),2) AS ticket
FROM yellow_taxi
GROUP BY payment_type
ORDER BY viajes DESC;
```
```python
df = spark.read.table("yellow_taxi")
df.groupBy("payment_type").count().orderBy("count", ascending=False).show()
```

### Sesión 9, Pipeline + calidad
```python
import polars as pl
import pandera.polars as pa

# BRONZE -> SILVER
silver = (
    pl.scan_parquet("yellow_tripdata_2024-01.parquet")
      .filter((pl.col("trip_distance") > 0) & (pl.col("total_amount") >= 0))
      .drop_nulls(subset=["PULocationID", "total_amount"])
      .collect()
)

# Validación de calidad
schema = pa.DataFrameSchema({
    "trip_distance": pa.Column(float, pa.Check.gt(0)),
    "total_amount":  pa.Column(float, pa.Check.ge(0)),
    "PULocationID":  pa.Column(int,   pa.Check.in_range(1, 265)),
})
schema.validate(silver)

# SILVER -> GOLD
gold = (silver.join(pl.read_csv("taxi_zone_lookup.csv"),
                    left_on="PULocationID", right_on="LocationID", how="left")
              .group_by("Borough")
              .agg(pl.len().alias("viajes"),
                   pl.col("total_amount").sum().alias("ingreso")))
gold.write_parquet("gold_ingresos_borough.parquet")
```

### Sesión 9, Bloque uv (demostrativo, terminal de Deepnote)
```bash
uv init --no-package mi-pipeline
cd mi-pipeline
uv add polars duckdb pandera
uv run python pipeline.py
```

---

## 10. Evaluación

| Componente | Peso |
|---|---|
| Participación y asistencia | 15% |
| Ejercicios y entregables semanales (sesiones 1-9) | 45% |
| Proyecto final | 40% |

Evaluación formativa continua: quiz breve de repaso al inicio de las sesiones 3 y 5, feedback en vivo durante la práctica.

### Proyecto final, requisitos
- Ingesta desde Parquet o CSV
- Al menos un JOIN (hecho + dimensión) y 3 agregaciones
- Implementación de las capas bronze/silver/gold
- Al menos 3 validaciones de calidad
- Documentación en Markdown explicando cada paso
- Al menos 2 visualizaciones
- Publicado en Deepnote

### Rúbrica (100 pts)

| Criterio | Puntos |
|---|---|
| Ingesta y lectura correcta de datos | 15 |
| Transformaciones (joins, agregaciones, medallion) | 25 |
| Calidad de datos (validaciones) | 20 |
| Documentación y claridad narrativa | 20 |
| Visualizaciones e insights | 15 |
| Presentación | 5 |

### Opciones de dataset
1. NYC TLC Yellow Taxi (hilo conductor): ingresos y patrones por zona/hora
2. Ecobici CDMX: patrones de viajes por estación/horario
3. Dataset libre del alumno, aprobado por el instructor

---

## 11. Riesgos y mitigaciones

| # | Riesgo | Impacto | Mitigación |
|---|---|---|---|
| 1 | **No se aprueba el plan de Educación de Deepnote** → aplican límites de 3 editores / 5 proyectos | Crítico | Solicitarlo antes de comprometer el diseño. Plan B: cada alumno usa su propio workspace personal Free (es el único editor), o migrar a Google Colab |
| 2 | **Dependencia total de internet y de un proveedor**, punto único de falla | Alto | Google Colab documentado **y ensayado** como respaldo; exportar notebooks como `.ipynb` al cierre de cada sesión; medir el ancho de banda de la sede antes de contratarla |
| 3 | **Apagado por inactividad de 15 min** durante bloques teóricos; los alumnos pierden variables | Medio | Ritual "Run all" desde la sesión 1; avisarlo explícitamente; mantener bloques teóricos cortos |
| 4 | **No aprenden a montar su propio entorno**, brecha real de empleabilidad | Medio | Bloque uv de 20 min en sesión 9 + guía asíncrona opcional; encuadrarlo explícitamente como tarea posterior al curso |
| 5 | **Techo de 5 GB de RAM** impide fuerza bruta | Bajo | Es ventaja pedagógica: obliga a usar lazy desde el inicio. Dimensionar datasets acorde |
| 6 | **Notebooks inducen malos hábitos** para pipelines productivos | Bajo | Sesión 9 escribe `.py` reales desde la terminal de Deepnote |
| 7 | **Databricks Free Edition** es serverless-only, sin clusters configurables | Bajo | Sesión 8 diseñada como recorrido conceptual |
| 8 | **Schema drift del dataset de taxis** entre meses | Bajo | Convertirlo en punto de enseñanza; fijar un solo mes para clase |
| 9 | **Drift de versiones** del ecosistema | Bajo | Fijar versiones; verificar antes de cada cohorte |

### Recortes disponibles si el tiempo se agota
Streaming engine · snowflake schema · orquestadores (ya es solo panorama) · Delta/Iceberg (ya es solo mención) · bloque uv · Genie.

---

## 12. Pendientes / decisiones abiertas

- [ ] **Solicitar y confirmar el plan de Educación de Deepnote** (bloqueante)
- [ ] Confirmar nombre final del curso con organizadores
- [ ] Medir el ancho de banda de la sede
- [ ] Definir tamaño de grupo (recomendado: 12-16 por instructor)
- [ ] Confirmar modalidad: presencial, remota o híbrida
- [ ] Verificar disponibilidad de los datasets de Ecobici CDMX
- [ ] Ensayar el plan B en Google Colab
- [ ] Preparar los proyectos plantilla en el workspace del curso
- [ ] Definir fechas exactas y horario

---

## 13. Recursos

### Documentación oficial
- Deepnote, `deepnote.com/docs` · plan de Educación: `deepnote.com/docs/edu-overview`
- Polars, `docs.pola.rs`
- DuckDB, `duckdb.org/docs`
- Databricks Free Edition, `docs.databricks.com/aws/en/getting-started/free-edition-limitations`
- Pandera, `pandera.readthedocs.io`
- uv, `docs.astral.sh/uv`

### Datos abiertos México
`datos.cdmx.gob.mx` · `inegi.org.mx/datosabiertos` · `datos.gob.mx`

### Ruta posterior al curso
Python intermedio y Git · gestión local de entornos (uv, Docker) · orquestación (Airflow, Dagster, Prefect) · dbt · modelado dimensional a profundidad (Kimball) · cloud y almacenamiento de objetos · Spark/PySpark.

---

## 14. Glosario

| Término | Definición |
|---|---|
| **Pipeline de datos** | Flujo automatizado que mueve y transforma datos de una fuente a un destino |
| **ETL / ELT** | Extract-Transform-Load / Extract-Load-Transform |
| **OLTP / OLAP** | Procesamiento transaccional / analítico |
| **Star schema** | Modelo con tabla de hechos central rodeada de dimensiones |
| **Hecho / Dimensión** | Métricas numéricas / contexto descriptivo |
| **Lakehouse** | Arquitectura que une data lake y data warehouse |
| **Medallion** | Capas bronze / silver / gold de refinamiento progresivo |
| **Columnar vs. row-based** | Almacenamiento por columnas (analítica) vs. por filas (transaccional) |
| **Lazy evaluation** | Diferir el cómputo hasta `collect()` para optimizar |
| **Idempotencia** | Ejecutar un proceso varias veces sin efectos duplicados |
| **DataFrame / LazyFrame** | Tabla en memoria / plan de consulta diferido en Polars |
| **Schema drift** | Cambio no anunciado en la estructura o tipos de los datos de origen |
| **Notebook** | Documento que combina código ejecutable, texto y resultados |

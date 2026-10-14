# Instrucciones para Claude Code: montar el repo, construir el curso y publicarlo en Deepnote

Este archivo es para ti, Claude Code. Léelo completo antes de ejecutar nada y sigue las partes en orden. Si una fase falla, detente y repórtalo, no improvises.

## Contexto

- Proyecto: curso introductorio de Ingeniería de Datos para la fundación Impact Click, 10 sesiones, en español, para principiantes, unos 10 alumnos. Todo el trabajo técnico corre en Deepnote. La sesión 8 usa además Databricks Free Edition.
- Esta carpeta se llama `intro-data-engineering`. Lee primero `docs/CURSO.md` (mapa del repo y decisiones vigentes) y `docs/FLUJO_DE_TRABAJO.md`.
- **El contenido ya está escrito.** Las 10 guías de `docs/guia/S01.md` a `S10.md` traen definiciones, guion, código, ejercicios con solución, quiz y, al final, la sección **"Especificación del notebook"** con los bloques que debe tener cada `.deepnote`. Tu trabajo es convertir esas guías en notebooks, probarlos en Deepnote real y publicarlos.
- Ya están configurados en esta máquina: Deepnote CLI (v0.10.x), el skill `deepnote` y el MCP de Deepnote (workspace **Impact Click**, acceso admin, OAuth). Usa el skill para cualquier duda del formato `.deepnote`.
- Idioma de lo que escribas para el usuario y en los notebooks: español de México, frases directas, comas en lugar de guiones largos (no uses la raya), bullets cuando ayuden.

## Reglas que no se rompen

- No imprimas, registres ni subas `DEEPNOTE_TOKEN`. Nunca uses `--token` en la línea de comandos, usa la variable de entorno o `.env`.
- No borres, renombres ni modifiques los proyectos que ya existen en el workspace ("Daily stock price dashboard" y "Welcome"). Solo crea cosas nuevas.
- No uses `--prune` ni `--on-conflict override` en `deepnote sync` sin preguntarme antes.
- Antes de cualquier comando que escriba en Deepnote (`open`, `sync`, herramientas de escritura del MCP, `create_run`), di en una línea qué va a hacer.
- Fuente de verdad: los archivos `notebooks/*.deepnote` en git. Lo que se edite en la nube se trae de vuelta al repo con sync.
- Si descubres que el código de una guía falla en la nube, corrige el notebook Y la guía, para que no se separen.
- No inventes resultados. Los textos "verificar en la nube" de las guías se reemplazan solo con valores que obtuviste ejecutando.
- Commits pequeños, uno por sesión como mínimo, con mensajes en español.

## Parte A: Infraestructura y prueba con la sesión 1

### Fase 0: Verificación previa

1. Confirma que estás en `intro-data-engineering` (`pwd`) y que existen `docs/guia/S01.md` a `S10.md`, `notebooks/S01.deepnote`, `scripts/` y `.env.example`.
2. `node -v` (20 o superior), `deepnote --version`, `git --version`, `gh auth status`, `python3 -c "import yaml"`. Si falta `yaml`: `pip install --user pyyaml` (o `uv pip install pyyaml`).
3. Comprueba `DEEPNOTE_TOKEN` sin mostrarlo: `[ -n "$DEEPNOTE_TOKEN" ] && echo definido || echo falta`. Si falta, busca en `.env`; si tampoco está, detente y pídeme que lo configure (ver `README.md`).
4. Con el MCP, ejecuta `get_me` y confirma que el workspace es **Impact Click**. Ejecuta `list_projects` y guarda la lista como línea base.
5. Si `gh auth status` falla, detente y pídeme `gh auth login`.

### Fase 1: Repo en GitHub

1. `git init -b main` si aún no es repo. Revisa que `.gitignore` excluya `.env`.
2. `git add .` y revisa con `git status` que NO aparezca `.env`.
3. Commit inicial: `Estructura inicial del curso: guias, scripts, documentacion y sesion 1`.
4. Crea el repo privado con el mismo nombre de la carpeta: `gh repo create intro-data-engineering --private --source=. --remote=origin --push`.
5. Crea la rama de trabajo: `git switch -c contenido-completo`. Trabaja en ella hasta el final y abre un pull request a `main` en la Fase 12.

### Fase 2: Validar lo que ya existe

1. `./scripts/dn todo` debe mostrar `ok`.
2. `./scripts/dn lint notebooks/S01.deepnote` y `./scripts/dn stats notebooks/S01.deepnote`. Reporta advertencias.
3. Lee la sección "Especificación del notebook" de `docs/guia/S01.md`. Aplica los 5 ajustes pendientes a `notebooks/S01.deepnote` (ejemplo de orden de ejecución, anatomía del pipeline, ejercicios 2 y 3, verificación ampliada). Valida otra vez y haz commit.

### Fase 3: Primer proyecto en la nube (con S01)

`deepnote sync` NO crea proyectos, solo sincroniza los que ya existen. Para crear uno se importa el archivo con `deepnote open`.

1. Ejecuta `python3 scripts/build_curso.py`. Genera `dist/curso.deepnote` con los notebooks que existan (hoy solo S01). Valida con `deepnote validate dist/curso.deepnote`.
2. Importa: `deepnote open dist/curso.deepnote`. Con el MCP (`list_projects`) confirma que aparece "Curso Data Engineering - Impact Click" en el workspace Impact Click, además de los 2 proyectos originales.
3. Si `deepnote open` intenta abrir un navegador y falla en WSL, usa el plan B con el MCP: `create_project`, `create_notebook` y `create_block` por cada bloque del YAML, respetando orden y tipos. Para bloques SQL conserva `sql_integration_id: deepnote-dataframe-sql`.
4. Sube `notebooks/requirements.txt` al proyecto como archivo `requirements.txt` (herramienta `write_file` del MCP). El campo `settings.requirements` no se aplica al importar.
5. Compara el ID del proyecto en la nube con `scripts/ids_proyectos.json` (clave `curso`). Si el CLI o la nube asignaron otro ID, actualiza el JSON, vuelve a correr el build y haz commit con el mensaje `Vincular proyecto curso con Deepnote`.
6. Con `create_run` ejecuta el notebook S01 y revisa con `get_run`. Es normal que la celda de verificación imprima "Pendiente" mientras los ejercicios sigan con `...`. Si falla `import polars` u otra librería, `requirements.txt` no se instaló solo: reporta el error exacto y propón la celda `%pip install -q -r requirements.txt` (ver `docs/LIMITACIONES.md`), sin agregarla todavía a todos los notebooks. Pregúntame.
7. Haz una corrida en seco de la sincronización (lee `deepnote sync --help` primero) y documenta en `docs/FLUJO_DE_TRABAJO.md` el comando exacto que funcionó, con directorio y flags.

**Punto de control 1:** muéstrame un resumen corto de la Parte A (URL del repo, URL del proyecto, resultado del run, comando de sync) y espera mi visto bueno antes de seguir.

## Parte B: Construir los notebooks de las sesiones 2 a 10

Para cada sesión N de 2 a 10, repite este ciclo. Ve por semanas: S02 y S03, luego S04 y S05, y así. Después de cada semana haz commit y reporta avance en 3 líneas.

### Ciclo por sesión

1. **Lee** `docs/guia/S0N.md` completo, sobre todo "Código del live coding", "Ejercicios" y "Especificación del notebook".
2. **Construye** `notebooks/S0N.deepnote` siguiendo la especificación y el patrón de `notebooks/S01.deepnote`: título (H1), callout de "Run all", objetivo, secciones H2 con explicación y código, ejercicios con `...`, y celda final `verificar_sesion_0N()`. Puedes usar el ayudante `scripts/nb.py` (clase `Notebook`) en un script temporal, o escribir el YAML siguiendo el skill. Las soluciones NO van en las celdas de ejercicio, van en la guía.
3. **Tareas y variantes** (ver `docs/TAREAS.md`):
   - En los notebooks de **S04, S05, S06, S07 y S09** agrega al inicio (después del callout de "Run all") una sección "Tu variante" con la celda que imprime `python3 scripts/variantes.py snippet` (deja `MI_VARIANTE = ...`), y al final, antes de la verificación, una sección "Tarea con variante" con el enunciado de `docs/TAREAS.md` y una celda con `...` para la solución y la llamada a `codigo_entrega`. La solución NO va en el notebook.
   - En **todos** los notebooks agrega una celda Markdown final "Explica con tus palabras" con la pregunta de esa sesión de `docs/TAREAS.md` (3 a 5 líneas).
   - Las celdas de verificación de las sesiones con variante deben avisar "Pendiente: falta definir MI_VARIANTE" si sigue en `...`, y nunca mostrar respuestas.
4. **Valida:** `./scripts/dn check notebooks/S0N.deepnote`, luego `lint` y `stats`.
5. **Sube y ejecuta en la nube:**
   - Reconstruye (`python3 scripts/build_curso.py`) y sincroniza `dist/curso.deepnote` con el proyecto (primero `--dry-run`). Si el sync no agrega notebooks nuevos a un proyecto existente, usa el MCP (`create_notebook` y `create_block`) y dímelo.
   - Con `create_run` ejecuta el notebook completo y revisa con `get_run`.
6. **Corrige** lo que falle, en el notebook y en la guía.
7. **Completa los "verificar en la nube":** busca esas frases en la guía (`grep -n "verificar en la nube" docs/guia/S0N.md`), obtén el valor real ejecutando y sustitúyelo. Anota en `docs/REGISTRO_VERIFICACION.md`: fecha, sesión, resultado del run, tiempo, errores y valores obtenidos.
8. **Commit:** `Sesion N: notebook construido y probado en Deepnote`.

### Casos especiales por sesión

- **S02:** el taller de errores trae 5 celdas rotas a propósito, y Run all se detiene en la primera celda con error. Colócalas al final del notebook, después de la verificación, o en una sección separada, y avisa en un callout que Run all se detendrá ahí. Confirma el comportamiento de Run all en la nube.
- **S03:** escribir y leer CSV y NDJSON de unos 3 millones de filas puede ser lento y consumir disco y RAM en la máquina Basic (5 GB). Mide tiempos y espacio. Si es demasiado, reduce con una muestra (por ejemplo las primeras 500 mil filas) y ajusta guía y notebook.
- **S04 y S05:** verifica que los bloques SQL con CTE, `QUALIFY` y `VALUES` corren con `deepnote-dataframe-sql`, y que `deepnote_return_variable_type: dataframe` entrega un objeto con `.columns` y `len()` (lo usa la verificación). Confirma que `pyarrow` está disponible (ya está en `requirements.txt`).
- **S05:** el diagrama del star schema está en Mermaid en la guía. Comprueba si Deepnote lo dibuja en una celda Markdown. Si no, agrega una imagen o el diagrama en texto, y dime cuál usaste.
- **S06:** confirma la salida real de `explain()` (se espera `PROJECT` con menos columnas y `SELECTION` empujados al scan) y actualiza la guía con lo que veas.
- **S07:** confirma que `fig.show()` de Plotly se ve en el notebook.
- **S08:** el notebook de Deepnote es solo la guía de conceptos y pasos de registro. El archivo `databricks/S08_notebook.py` NO se puede probar desde aquí: no lo modifiques salvo errores de sintaxis evidentes, y recuérdame que lo ensaye en una cuenta Free de Databricks.
- **S09:** prueba también `proyecto_uv/`. Verifica si la terminal de Deepnote está disponible en esta cuenta y si `uv` ya viene instalado ahí. Si la terminal no está, documenta la alternativa en la guía. El pipeline de `proyecto_uv/pipeline.py` lee `datos/`, ejecútalo en la nube (o en local con el parquet descargado) dos veces y confirma que el resultado es idéntico.
- **S10:** `notebooks/S10.deepnote` es la plantilla del proyecto final y va en su propio proyecto (`dist/proyecto_final.deepnote`). Créalo con `deepnote open dist/proyecto_final.deepnote` y registra su ID en `scripts/ids_proyectos.json` (clave `proyecto_final`) si cambió.

**Punto de control 2:** al terminar la sesión 5 y otra vez al terminar la 10, muéstrame un resumen y espera mi visto bueno.

## Parte C: Cierre

### Fase 11: Documentos derivados, clave de variantes y revisión

0. **Clave de variantes:** descarga el dataset a `datos/` (carpeta ignorada por git) con los `curl` de `docs/TAREAS.md`, instala polars (`pip install --user polars`) y ejecuta `python3 scripts/variantes.py clave --datos datos --salida clave/clave_variantes.csv`. Después comprueba en la nube la variante 1 de la tarea de S04 (resuelve la tarea en un notebook de prueba con las soluciones de `docs/TAREAS.md` y compara el resultado con la clave). Si no coincide, detente y repórtalo. La carpeta `clave/` no debe subirse a git (`git status` no debe mostrarla).
1. Ejecuta `python3 scripts/compilar_docs.py` para regenerar `docs/GLOSARIO.md` y `docs/QUIZZES.md` con los cambios de las guías.
2. Ejecuta `./scripts/dn todo` y confirma que todos los notebooks son válidos.
3. Busca rayas largas: `grep -rln "—" . --include="*.md" --include="*.deepnote" --include="*.py"`. Corrige con comas o dos puntos.
4. Revisa que `.env` no esté en el repo: `git ls-files | grep -x ".env"` no debe devolver nada.
5. Revisa que cada guía con aclaraciones "verificar" quede resumida en `docs/REGISTRO_VERIFICACION.md` (qué quedó confirmado y qué sigue pendiente, por ejemplo el ensayo de Databricks).

### Fase 12: Publicación final

1. `python3 scripts/build_curso.py` y valida `dist/curso.deepnote` y `dist/proyecto_final.deepnote`.
2. Sincroniza los dos proyectos (dry-run, luego real). Con el MCP (`get_project`, `get_notebook`) verifica que el proyecto del curso tiene 9 notebooks y el del proyecto final 1, y que el número de bloques coincide con el archivo.
3. Sube `requirements.txt` a ambos proyectos si no está.
4. Ejecuta Run all de cada notebook una última vez con `create_run` y registra el resultado.
5. `git push` de la rama `contenido-completo` y abre un pull request a `main` con `gh pr create` con un resumen de cambios. No hagas merge, lo reviso yo.
6. Con `generate_project_url` dame las URLs de los dos proyectos.

### Entrega final

Entrégame un resumen corto con:

- URL del repo y del pull request
- URL de los dos proyectos de Deepnote
- Resultado de cada notebook en la nube (ok o error)
- Cambios que hiciste a las guías por problemas reales
- Que la clave de variantes se generó y coincide con la nube (sí o no)
- Pendientes, en especial: ensayar `databricks/S08_notebook.py`, solicitar el plan Education, decidir cómo se manejan las correcciones después de repartir (ver `docs/LIMITACIONES.md`) y la prueba de clase (`docs/PRUEBA_DE_CLASE.md`)

## Qué NO hacer

- No invitar personas al workspace ni compartir los proyectos.
- No cambiar el plan, la facturación ni las integraciones del workspace.
- No hacer merge del pull request.
- No modificar el contenido pedagógico (definiciones, orden de temas, ejercicios) salvo para corregir errores que encuentres al ejecutar. Si ves algo discutible, anótalo y pregúntame.

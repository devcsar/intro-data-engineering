# proyecto_uv: el pipeline de la sesión 9 como proyecto de uv

Este proyecto es la demo del bloque de uv (20 minutos) de la sesión 9. Muestra el mismo pipeline bronze, silver y gold del notebook, pero como un script `.py` que se corre desde la terminal con un entorno propio y repetible.

## Qué hay aquí

| Archivo | Para qué sirve |
|---|---|
| `pyproject.toml` | Lista el proyecto y sus dependencias (Polars fijo en 1.43.2, DuckDB y Pandera). |
| `pipeline.py` | El pipeline: lee de `datos/`, valida, manda lo inválido a cuarentena y escribe las tres capas. |
| `README.md` | Estas instrucciones. |

`uv` crea además `uv.lock` (las versiones exactas que quedaron instaladas) y `.venv/` (el entorno). Esos dos no se escriben a mano.

## Qué hace el pipeline

- Lee `datos/viajes_2024_01.parquet` y `datos/zonas.csv`. Los busca en `datos/` o en `../datos/`, así que funciona parado dentro de `proyecto_uv/`. También acepta la variable `DATOS_DIR`.
- Escribe `datos/bronze/`, `datos/silver/`, `datos/gold/` y `datos/quarantine/`, más un resumen en `datos/metricas/ultima_corrida.json`.
- Es idempotente: cada corrida reemplaza los archivos de salida completos. Correrlo dos veces deja el mismo resultado, sin duplicados.
- Valida cinco reglas (nulos, distancia, importe, zona, fecha dentro del mes) y también duplicados. Todo lo rechazado va a `quarantine/` con la columna `motivo`.
- Usa `logging` para contar la historia de la corrida y termina con código distinto de cero si algo falla.

## Comandos del bloque de uv

Estos son los pasos de la demo, en orden. Funcionan igual en la terminal de Deepnote y en una computadora local, con las diferencias que se indican abajo.

### Opción A: construir el proyecto desde cero (lo que se hace en clase)

```bash
# 1. Crear el proyecto. --no-package evita la estructura src/ y deja un proyecto simple de scripts.
uv init --no-package mi-pipeline
cd mi-pipeline

# 2. Agregar dependencias. Se anotan en pyproject.toml y uv las instala en .venv
uv add polars duckdb pandera

# 3. Copiar el script (desde la carpeta proyecto_uv de este repositorio) y correrlo
cp ../proyecto_uv/pipeline.py .
uv run python pipeline.py
```

Importante: `uv add polars` sin versión instala **la última versión disponible**, que puede ser mayor que la del curso. El curso usa Polars 1.43.2. Para quedarte en esa versión escribe:

```bash
uv add "polars==1.43.2" duckdb pandera
```

Se probó `pipeline.py` con Polars 1.43.2. También corrió sin cambios con una versión más nueva (2.0.0), pero en clase usa la fija para que todos vean lo mismo.

### Opción B: usar este proyecto tal cual

```bash
cd proyecto_uv
uv sync                     # crea .venv e instala lo que dice pyproject.toml
uv run python pipeline.py   # corre el pipeline en ese entorno
```

### Comprobar la idempotencia

```bash
uv run python pipeline.py
sha256sum ../datos/silver/viajes.parquet ../datos/gold/ingresos_borough.parquet > corrida1.txt
uv run python pipeline.py
sha256sum ../datos/silver/viajes.parquet ../datos/gold/ingresos_borough.parquet > corrida2.txt
diff corrida1.txt corrida2.txt && echo "Mismo resultado, es idempotente"
```

Si `diff` no imprime nada y aparece el mensaje, las dos corridas dejaron archivos idénticos. En macOS el comando equivalente de `sha256sum` es `shasum -a 256`.

## Qué hacer en la terminal de Deepnote y qué en una computadora local

| Tema | Terminal de Deepnote | Computadora local |
|---|---|---|
| Abrir la terminal | En la barra lateral, botón **+** de Notebooks, "Create a new terminal" (la documentación la marca como función experimental, verificar que tu plan la tenga) | Terminal del sistema (Terminal en macOS, PowerShell o WSL en Windows, cualquier terminal en Linux) |
| Tener uv | Comprobar con `uv --version`. Si no está, `pip install uv` (verificar en la máquina de Deepnote antes de la clase) | Instalarlo siguiendo `https://docs.astral.sh/uv/getting-started/installation/` |
| Dónde viven los datos | La carpeta del proyecto de Deepnote, donde ya está `datos/` | La carpeta que tú crees, con `datos/viajes_2024_01.parquet` y `datos/zonas.csv` |
| Dónde crear el proyecto | Dentro del proyecto de Deepnote, para que `../datos` exista | Al lado de la carpeta `datos/` |
| Qué se conserva | Los archivos de la carpeta de trabajo sobreviven al apagado de la máquina, las variables no | Todo, está en tu disco |
| Aviso | Al crear el proyecto, uv puede inicializar un repositorio de Git dentro de la carpeta. Si no lo quieres, agrega `--vcs none` | Igual |
| Fin de la clase | El entorno `.venv` se queda en la carpeta, pero no es parte del notebook | Puedes seguir usándolo siempre |

## Qué verificó el autor de este material

- Con uv 0.13.1 en Linux, `uv init --no-package nombre` crea `.python-version`, `README.md`, `main.py` y `pyproject.toml` (más `.gitignore` y un repositorio de Git), sin carpeta `src/`. El `pyproject.toml` incluye `requires-python` tomado del Python que encontró y `dependencies = []`.
- `uv add` agregó las dependencias a `pyproject.toml`, creó `uv.lock` y creó `.venv`.
- `uv run python pipeline.py` corrió con Polars 1.43.2 y con una versión más nueva.
- Las pruebas usaron datos sintéticos con filas inválidas a propósito. Con los datos reales de taxis, los conteos y tiempos: verificar en la nube.

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| `FileNotFoundError: No encontré viajes_2024_01.parquet` | Estás en una carpeta sin `datos/` al lado. Entra a la carpeta correcta o define `DATOS_DIR=/ruta/a/datos` |
| `command not found: uv` | uv no está instalado en esa máquina, instálalo (ver tabla) |
| El contrato de silver falló | Pandera encontró algo que no cumple. Lee el cuadro de errores que imprime el log |
| La cuarentena es muy alta | El log avisa si pasa del umbral de ejemplo del script (`UMBRAL_CUARENTENA`). Revisa las reglas y los datos |
| `uv run` instala cosas cada vez | Es normal la primera vez. Después reutiliza `.venv` |

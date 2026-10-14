# Flujo de trabajo

## Principio

Los archivos `notebooks/*.deepnote` en git son la fuente de verdad. Deepnote es el lugar donde se ejecutan y se reparten.

## Crear o cambiar una sesión

1. Pide a Claude Code que genere o edite `notebooks/S0X.deepnote`, usando `S01.deepnote` como plantilla de tono y estructura.
2. Estructura fija de cada notebook:
   - título y callout de "Run all"
   - objetivo de la sesión en un párrafo
   - secciones con explicación y código
   - ejercicio con `...` para completar
   - celda final `verificar_sesion_0X()` con asserts que dicen qué falta
3. Valida: `./scripts/dn check notebooks/S0X.deepnote`, luego `lint` y `stats`.
4. Commit por sesión.

## Publicar

- Primera vez de un notebook nuevo: `./scripts/dn subir notebooks/S0X.deepnote` (crea proyecto) o agregarlo como notebook al proyecto del curso con el MCP (`create_notebook` y `create_block`).
- Cambios posteriores: `deepnote sync`, siempre con `--dry-run` primero. Nunca `--prune` ni `--on-conflict override` sin revisar.
- Los outputs de las celdas no se sincronizan, solo el contenido.

## Lo que se comprobó en la primera prueba (2026-10-14)

- `deepnote open dist/curso.deepnote` falla en WSL con `spawn xdg-open ENOENT` y no crea nada en el workspace. El proyecto se creó con el MCP (`create_project`, `create_notebook`, `create_block`). Los bloques se crean uno por uno con `position`, en orden.
- `create_block` no acepta `sql_integration_id: deepnote-dataframe-sql` en `metadata` (pide un UUID en `integrationId`). El bloque SQL se crea solo con `deepnote_variable_name` y `deepnote_return_variable_type`, y queda con `integrationId: null`.
- `requirements.txt` se sube con `write_file` y queda en el proyecto, pero no se instala solo (ver `docs/REGISTRO_VERIFICACION.md`).
- Sync en seco, hacia un directorio vacío fuera del repo (no escribe nada, usa `DEEPNOTE_TOKEN` del entorno):

```bash
set -a && . ./.env && set +a
deepnote sync <directorio_vacio> --dry-run --all-files
```

  Sync espeja el workspace completo, un directorio por proyecto con un `.deepnote` por notebook. No crea ni borra proyectos. El push real todavía no se ha probado.

## Traer cambios hechos en la nube

Si editas algo directo en Deepnote, corre sync para traerlo al repo y haz commit. Si no, el siguiente sync desde el repo podría pisarlo.

## Arquitectura para los alumnos

- La cuenta Free permite 5 proyectos, por eso se reparten solo 2: "Curso DE" (con los 10 notebooks) y "Proyecto final".
- Mientras el curso se arma, hay un proyecto por archivo. Antes de repartir, se consolida en uno solo (varios notebooks por proyecto es válido en Deepnote).
- Dependencias: `requirements.txt` como archivo del proyecto, no en la configuración del entorno, porque la configuración no se copia cuando el alumno duplica.

## Pendiente de decidir

- Consolidar los 10 notebooks en un solo `.deepnote` (script de unión) o en la nube con el MCP.
- Solicitar el plan Education a help@deepnote.com explicando que Impact Click es una fundación.

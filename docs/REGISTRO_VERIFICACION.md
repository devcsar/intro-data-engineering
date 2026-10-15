# Registro de verificación en la nube

Aquí se anota lo que se comprueba ejecutando los notebooks en Deepnote real. Una fila por prueba. Esta tabla la llena Claude Code durante la construcción y el instructor en los ensayos.

## Corridas

| Fecha | Sesión | Dónde | Resultado | Tiempo de Run all | Notas |
|---|---|---|---|---|---|
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | Error: `ModuleNotFoundError: No module named 'polars'` | 12 s hasta detenerse | `requirements.txt` subido como archivo del proyecto no se instala solo. El run se detiene en el primer error. |
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | Error en el bloque SQL: `This SQL cell is not linked with a connected integration` | 50 s | La celda de instalación ya funcionaba. El MCP creó el SQL sin `sql_integration_id` (no acepta `deepnote-dataframe-sql`). |
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | **OK** (status success, sin errores) | 39 s | Tras corregir el SQL con `deepnote sync` (push). Descarga de 2,964,624 filas en 1 s, guardar el parquet 16 s, SQL 2.5 s. La verificación imprime los 3 "Pendiente" esperados. |

## Valores reales del dataset (reemplazan los "verificar en la nube" de las guías)

| Sesión | Dato | Valor | Cómo se obtuvo |
|---|---|---|---|
| 1 | Viajes con más de un pasajero (`viajes_compartidos`) | 604,258 | Solución de la guía ejecutada con Polars 1.43.2 sobre el mismo parquet, desde `uv run` local (no en la nube) |
| 1 | Viaje más caro: `total_amount` y zona | 5000.0 en la zona 264 (Unknown, N/A) | Igual. Hay 2 viajes empatados en 5000.0, ambos de la zona 264 y con distancia 0.0 |
| | | | |

## Preguntas abiertas a confirmar

- [x] `requirements.txt` se instala solo en la copia del alumno, o hace falta la celda `%pip install`. Resultado (2026-10-14): NO se instala solo. Con el archivo subido al proyecto, `import polars` falla. Hace falta una celda de instalación. `uv` NO viene instalado en la máquina (`uv: command not found`), así que la celda de la sesión 1 hace `!pip install -q uv` y luego `!uv pip install -q --python {sys.executable} -r requirements.txt`. Probado en la nube: instala en unos 15 s.
- [x] Bloque SQL `deepnote-dataframe-sql` consulta DataFrames en memoria (sesión 1). Sí funciona, pero solo si el bloque lleva `sql_integration_id: deepnote-dataframe-sql`, y el MCP no puede ponerlo. Se fijó empujando el `.deepnote` con `deepnote sync`.
- [ ] Run all se detiene en la primera celda con error (taller de errores de la sesión 2)
- [ ] Tiempos y espacio de CSV y NDJSON de la sesión 3 en la máquina Basic
- [ ] Bloques SQL con CTE, `QUALIFY` y `VALUES` en `deepnote-dataframe-sql`
- [ ] Mermaid se dibuja en Markdown de Deepnote
- [ ] Salida real de `explain()` (sesión 6)
- [ ] Plotly se muestra en el notebook (sesión 7)
- [ ] `databricks/S08_notebook.py` ensayado en una cuenta Free de Databricks
- [ ] Cuota diaria y catálogo por defecto en Databricks Free Edition
- [ ] Terminal de Deepnote disponible en cuenta Free y `uv` preinstalado (sesión 9)
- [ ] Un usuario con cuenta Free puede publicar y compartir por enlace (sesión 10)
- [ ] CloudFront accesible desde Deepnote
- [ ] La clave de variantes (`scripts/variantes.py clave`) coincide en la nube con la variante 1 de S04
- [ ] Forms de entrega creado y probado con un código de entrega real

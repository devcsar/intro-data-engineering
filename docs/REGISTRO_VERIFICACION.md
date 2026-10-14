# Registro de verificación en la nube

Aquí se anota lo que se comprueba ejecutando los notebooks en Deepnote real. Una fila por prueba. Esta tabla la llena Claude Code durante la construcción y el instructor en los ensayos.

## Corridas

| Fecha | Sesión | Dónde | Resultado | Tiempo de Run all | Notas |
|---|---|---|---|---|---|
| 2026-10-14 | 1 | Deepnote (run detached, MCP) | Error en la primera celda de código: `ModuleNotFoundError: No module named 'polars'` | 12 s hasta detenerse | `requirements.txt` subido como archivo del proyecto no se instala solo. El run se detiene en el primer error. Pendiente decidir la celda `%pip install`. |

## Valores reales del dataset (reemplazan los "verificar en la nube" de las guías)

| Sesión | Dato | Valor | Cómo se obtuvo |
|---|---|---|---|
| 1 | Viajes con más de un pasajero (`viajes_compartidos`) | | |
| 1 | Viaje más caro: `total_amount` y zona | | |
| | | | |

## Preguntas abiertas a confirmar

- [x] `requirements.txt` se instala solo en la copia del alumno, o hace falta la celda `%pip install`. Resultado (2026-10-14): NO se instala solo. Con el archivo subido al proyecto, `import polars` falla. Hace falta la celda `%pip install -q -r requirements.txt` (pendiente de aprobar).
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

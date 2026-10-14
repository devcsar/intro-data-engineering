# Limitaciones y riesgos (10 alumnos)

Datos de planes verificados en las condiciones de Deepnote al preparar el curso. Confírmalos en la página de precios antes de la primera clase, porque pueden cambiar.

## Cuenta Free del alumno

- Hasta 5 proyectos por workspace, 3 editores. Por eso el curso se reparte en solo 2 proyectos.
- Máquina básica: 5 GB de RAM y 2 vCPU. El dataset de taxis (unos 3 millones de filas, parquet de unos 50 MB) cabe bien con Polars. Evita pandas con datasets grandes.
- La máquina se apaga tras 15 minutos sin actividad y tiene un tope de 8 horas continuas. Al apagarse, las variables se pierden, los archivos en la carpeta de trabajo se conservan.
- Subida web de archivos limitada a 100 MB. Por eso los datos se descargan por URL dentro del notebook.
- Historial de versiones de 7 días.
- Sin Deepnote AI ni máquinas avanzadas en Free.

## Roles y reparto

- Viewers ilimitados: pueden ejecutar notebooks, cambiar inputs y duplicar el proyecto a su workspace.
- Al duplicar no se conservan entornos personalizados ni integraciones.
- Si invitas a los 10 alumnos como **Editors** en el workspace Impact Click, cada uno ocupa un asiento de pago en Team (referencia: 39 USD por editor al mes con pago anual). Con 10 alumnos eso es relevante. Alternativas: Viewers con duplicación, o el plan Education.
- Plan Education: gratuito, requiere correo escolar o aprobación manual escribiendo a help@deepnote.com (ONG, programa de formación). Quita los topes de editores y proyectos. No incluye máquinas avanzadas, programación de ejecuciones ni Deepnote AI. Tarda en aprobarse, pídelo cuanto antes.

## Dependencias

- Las librerías van en `requirements.txt` como archivo del proyecto. En la prueba de clase hay que confirmar que se instalan solas en la copia del alumno.
- Si no se instalan solas, agrega como primera celda de código del notebook:

```python
%pip install -q -r requirements.txt
```

  y pide a los alumnos reiniciar el kernel una vez. Es una solución estándar, pero valídala en la prueba.

## Bloques SQL

- Los bloques `sql` nativos sobre dataframes (`deepnote-dataframe-sql`) solo corren en la nube. No funcionan al ejecutar con el CLI en local.
- Para pruebas locales, usa `duckdb.sql(...)` en una celda de código.

## Correcciones después de repartir

- Cada alumno tiene su propia copia. Si corriges el proyecto original, sus copias no se actualizan.
- Opciones: corregir antes de cada sesión y que el alumno duplique la sesión nueva (un proyecto por semana no cabe en Free, así que mejor entregar notebooks sueltos para importar), o pegar el bloque corregido en vivo durante la clase.
- Regla práctica: congelar el contenido de cada sesión al menos 2 días antes.

## Evaluación

- Deepnote no tiene calificación automática ni integración con plataformas de cursos.
- Se usa: celda `verificar_sesion_0X()` para el alumno, Google Forms para quizzes y rúbrica manual para el proyecto final.
- No hay forma nativa de que veas el avance de cada alumno en su copia. Pide que compartan la URL de su proyecto con permiso de lectura, o que envíen captura de la celda de verificación.

## CLI y sincronización

- `deepnote sync` no crea ni borra proyectos en la nube, solo sincroniza los vinculados.
- Los outputs de las celdas no se sincronizan.
- Archivos de datos hasta 100 MiB por archivo al usar `--all-files`.
- La llave de API es del workspace: quien la tenga puede escribir en él. Guárdala solo en `.env` y rótala si se filtra.

## Riesgos de la primera clase

- Alumnos sin cuenta de Deepnote o con invitación en spam: pídeles crearla antes del día 1.
- Máquina que se apaga a mitad de explicación: recuérdalo en el callout inicial y haz Run all al empezar.
- Cambios de planes o límites de Deepnote: revisa la página de precios la semana previa.

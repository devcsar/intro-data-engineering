# Prueba de clase en Deepnote

Haz este ensayo antes de la primera sesión. Dura unos 45 a 60 minutos y simula lo que vivirá un alumno real con cuenta Free.

## Qué necesitas

- Un correo distinto al tuyo para crear una cuenta Free de prueba (o un voluntario que haga de alumno).
- El proyecto ya creado en el workspace Impact Click (ver `INSTRUCCIONES_CLAUDE_CODE.md`).
- Un cronómetro.

## Paso 1: Preparar al "alumno"

1. En una ventana privada del navegador, crea una cuenta Free en deepnote.com con el correo de prueba.
2. Comprueba que el workspace del alumno es Free (límite de 5 proyectos).

## Paso 2: Compartir el proyecto

1. En tu cuenta, abre el proyecto del curso, botón Share, e invita el correo de prueba con rol **Viewer**.
2. Anota cómo le llega la invitación y cuánto tarda.

## Paso 3: Lo que hace el alumno

1. Acepta la invitación, abre el proyecto.
2. Duplica el proyecto a su workspace (opción Duplicate). Anota cualquier pantalla confusa.
3. Presiona **Run all** y cronometra el tiempo total.
4. Lee el callout inicial y corre la celda de verificación del entorno.

## Paso 4: Qué observar

Marca cada punto como ok o falla:

- [ ] Las librerías (`polars`, `duckdb`, `pandera`) están disponibles sin instalar nada. Si no, ver "Dependencias" en `LIMITACIONES.md`.
- [ ] La descarga del parquet y del CSV de zonas funciona.
- [ ] Se crea la carpeta `datos/` y los archivos se guardan.
- [ ] El bloque SQL corre y devuelve el dataframe `df_pagos`.
- [ ] La celda de verificación muestra los "Pendiente" esperados antes del ejercicio.
- [ ] El alumno resuelve el ejercicio y la verificación dice "Sesión 1 completa".
- [ ] Tiempo total de Run all: ______ minutos.
- [ ] Apagar la máquina (esperar 15 minutos de inactividad o detenerla) y volver: los archivos de `datos/` siguen, las variables no. Un nuevo Run all las recupera.

## Paso 5: Simular un cambio

1. Corrige algo mínimo en el archivo del repo, haz commit y sync.
2. Confirma que la copia del alumno NO cambia. Esto es normal y define cómo se publican las correcciones: ver "Correcciones" en `LIMITACIONES.md`.

## Paso 6: Ensayo con varios alumnos

Si es posible, repite el paso 3 con 3 o 4 personas al mismo tiempo para ver tiempos y dudas reales. Cada alumno corre en su propia máquina, así que la carga no se comparte, pero sí conviene ver cuántos se atoran en la invitación o en la duplicación.

## Después de la prueba

- Escribe aquí los problemas que salieron y cómo se resolvieron.
- Ajusta el notebook, valida con `./scripts/dn todo` y haz commit.
- Prepara para el día 1 una hoja de una página con los pasos de aceptar la invitación, duplicar y Run all, con capturas.

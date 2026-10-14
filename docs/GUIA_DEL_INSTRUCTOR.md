# Guía del instructor: cómo dar el curso

Esta guía explica el método, no el contenido. El contenido de cada sesión está en `docs/guia/S0X.md`.

## El método: programar en vivo, juntos

- El instructor comparte pantalla y abre el notebook de la sesión. Cada alumno tiene su propia copia en su cuenta.
- La regla es "yo escribo, ustedes ejecutan". Las celdas ya vienen en el notebook, pero tú las recorres una por una explicando antes de ejecutar.
- Antes de ejecutar una celda, pide que alguien adivine qué va a pasar. Después ejecuta y compara.
- Las celdas "Tu turno" se hacen solos o en parejas, con el tiempo marcado en el guion. Mientras tanto, recorre la sala o los chats.
- Los alumnos pueden llevarse todo el material. No hay secretos, el valor está en la práctica guiada.

## Línea de tiempo de preparación

### Dos semanas antes

- Solicita el plan de Educación de Deepnote (help@deepnote.com) explicando que Impact Click es una fundación.
- Confirma sede, horario y que el wifi aguante 10 personas en notebooks en la nube (mínimo 25 Mbps estables).
- Haz la prueba de clase completa (`docs/PRUEBA_DE_CLASE.md`).
- Pide a los alumnos crear su cuenta de Deepnote y confirma que todos la tienen.
- Revisa versiones: `pl.__version__`, estado de Polars (hoy existe Polars 2.0 y el curso fija 1.43.2), límites vigentes de Deepnote Free y de Databricks Free Edition.

### Una semana antes de la sesión 8

- Ensaya `databricks/S08_notebook.py` en una cuenta Free de Databricks. No se puede probar desde este repo.
- Pide a los alumnos crear su cuenta de Databricks Free Edition al menos dos días antes de la sesión 8, para que no se pierda tiempo de clase.

### Dos días antes de cada sesión

- Congela el contenido de la sesión. Los alumnos duplican su propia copia, así que cualquier cambio posterior no les llega.
- Ejecuta el notebook completo con Run all en tu cuenta y confirma que no hay errores.
- Lee la guía de la sesión, sobre todo el guion y los errores comunes.

### El día de la sesión

- Llega 20 minutos antes. Abre el notebook, ejecuta Run all y deja la máquina encendida.
- Ten a la mano el plan B de datos (parquet en una carpeta compartida).
- Abre la guía de la sesión en otra ventana para seguir los tiempos.

## Estructura repetible de cada sesión

- **Primeros 10 minutos:** Run all, dudas de la sesión anterior y revisión de la tarea. Repite siempre este ritual, resuelve el apagado por inactividad y enseña reproducibilidad.
- **Bloques de 25 a 35 minutos:** teoría corta, luego código en vivo. No más de 15 minutos seguidos hablando sin tocar el notebook.
- **Descanso de 10 minutos** entre los minutos 40 y 85.
- **Práctica guiada** en el último tercio.
- **Cierre de 5 a 10 minutos:** resumen de tres líneas, tarea, avance de la siguiente sesión y ejecución de `verificar_sesion_0N()`.

## Cómo conducir con 10 alumnos

- Con 10 personas puedes preguntar a cada una en cada sesión. Úsalo para detectar quién se está quedando atrás.
- Forma parejas fijas desde la sesión 2. En la práctica, uno escribe y otro dicta, y cambian en la siguiente sesión.
- Nombra a un "compañero de apoyo" por sesión que ayude a quien se atrasa sin resolverle el ejercicio.
- Si alguien se atora más de 5 minutos, ofrece mostrar la solución en la guía y seguir. No detengas al grupo.
- Pide que activen el chat o un canal (WhatsApp, Discord) para compartir errores con capturas.

## Cómo manejar errores en vivo

- Cuando aparezca un error, léelo en voz alta: última línea del traceback primero, luego el archivo y la línea.
- Pregunta "¿qué dice el mensaje?" antes de dar la solución.
- Los errores comunes de cada sesión están en la sección "Errores comunes" de su guía.
- Si el error es de infraestructura (máquina caída, descarga lenta), pasa al plan B sin perder el ritmo: "mientras se arregla, sigo con la explicación y lo ejecutan después".

## Problemas técnicos frecuentes

| Problema | Qué hacer |
|---|---|
| La máquina se apagó y se perdieron las variables | Run all. Es parte del ritual, se explica en la sesión 1. |
| Un alumno no tiene la invitación o duplicó mal | Reenviar la invitación al correo correcto y, si hace falta, compartir el archivo `.deepnote` de `dist/` para importarlo. |
| La descarga del parquet falla o es muy lenta | Usar la URL de respaldo (`docs/DATASETS.md`) o el parquet ya descargado. |
| Un alumno llegó tarde | Que duplique el proyecto, haga Run all y siga desde la celda actual. |
| El navegador va lento | Cerrar pestañas, usar Chrome o Edge actualizado. |
| Internet de la sede se cae | Plan B: Google Colab con el notebook exportado a `.ipynb` (`deepnote convert`). Ensayarlo antes del curso. |
| Se agota el tiempo en un bloque | Ver "Recortes disponibles" más abajo. |

## Recortes disponibles si el tiempo se agota

- Motor streaming (sesión 7).
- Snowflake schema (sesión 5).
- Orquestadores (sesión 9, ya es solo panorama).
- Delta Lake e Iceberg (sesión 3, ya es solo mención).
- Bloque de uv (sesión 9).
- Genie (sesión 8).

## Ajuste de la sesión 10 para 10 alumnos

El temario original deja 25 minutos para presentaciones, que alcanzan para 5 a 8 alumnos con 3 a 5 minutos. Con 10 alumnos:

- Reduce el taller asistido de 65 a 50 minutos (minutos 55 a 105).
- Amplía las presentaciones a 40 minutos (minutos 105 a 145): 3 minutos por alumno, 1 minuto para cambio y preguntas.
- Las revisiones entre pares se hacen en parejas durante el taller, no al final.

## Después de cada sesión

- Revisa quién entregó la tarea y quién no se conectó, y escríbeles ese mismo día.
- Anota en `docs/REGISTRO_VERIFICACION.md` cualquier error nuevo que apareció y cómo se resolvió, y ajusta la guía.
- Comparte el enlace al notebook de la siguiente sesión con anticipación.
- Si algún bloque se alargó, ajusta tiempos para la próxima cohorte.

## Evaluación

Ver `docs/EVALUACION.md`.

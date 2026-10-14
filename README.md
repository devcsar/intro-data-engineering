# Intro a la Ingeniería de Datos, Impact Click

Curso de 10 sesiones (2 por semana, 150 minutos cada una) para personas que empiezan en tecnología, en español. Todo el trabajo técnico de los alumnos ocurre en Deepnote, sin instalar nada. La sesión 8 usa además Databricks Free Edition.

Empieza por `docs/CURSO.md`, que explica cómo está armado todo y dónde está cada cosa.

## Qué contiene el repo

- `docs/guia/S01.md` a `S10.md`: guías del instructor (definiciones, guion minuto a minuto, código, ejercicios con solución, quiz, tarea).
- `docs/GUIA_DEL_INSTRUCTOR.md`: cómo dar el curso.
- `docs/GLOSARIO.md` y `docs/QUIZZES.md`: generados desde las guías.
- `docs/EVALUACION.md`, `docs/DATASETS.md`, `docs/LIMITACIONES.md`, `docs/PRUEBA_DE_CLASE.md`, `docs/FLUJO_DE_TRABAJO.md`.
- `notebooks/`: un notebook `.deepnote` por sesión y `requirements.txt`.
- `databricks/`, `proyecto_uv/`, `proyecto_final/`: material de las sesiones 8, 9 y 10.
- `scripts/`: herramientas para validar, armar y publicar.
- `INSTRUCCIONES_CLAUDE_CODE.md`: runbook para que Claude Code construya, pruebe y publique todo.

## Requisitos en la máquina de autoría (WSL)

- Node 20 o superior y el CLI: `npm install -g @deepnote/cli`
- Python 3 con `pyyaml` (para los scripts)
- `git` y `gh` (GitHub CLI) con sesión iniciada: `gh auth login`
- MCP de Deepnote conectado a Claude Code
- Una llave de API del workspace Impact Click

## Configurar la llave

1. En Deepnote: Settings & members, Security, API keys, crea una llave.
2. Copia `.env.example` a `.env` y pega la llave: `DEEPNOTE_TOKEN=tu_llave`
3. Nunca la subas al repo. `.env` ya está en `.gitignore`.

## Cómo arrancar con Claude Code

Desde esta carpeta, abre Claude Code y pega:

> Lee INSTRUCCIONES_CLAUDE_CODE.md y ejecútalo fase por fase. Pídeme confirmación antes de escribir en Deepnote y detente en los puntos de control.

## Comandos útiles

- `./scripts/dn todo`: valida todos los notebooks
- `./scripts/dn check notebooks/S01.deepnote`
- `./scripts/dn lint notebooks/S01.deepnote`
- `python3 scripts/build_curso.py`: arma `dist/curso.deepnote` (sesiones 1 a 9) y `dist/proyecto_final.deepnote` (sesión 10)
- `python3 scripts/compilar_docs.py`: regenera glosario y quizzes desde las guías

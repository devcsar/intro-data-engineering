#!/usr/bin/env python3
"""Regenera docs/GLOSARIO.md y docs/QUIZZES.md a partir de las guías docs/guia/S*.md.

Las guías son la fuente. Si cambias una definición o una pregunta en una guía,
corre:  python3 scripts/compilar_docs.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GUIAS = sorted((RAIZ / "docs" / "guia").glob("S[0-9][0-9].md"))


def seccion(texto, titulo):
    m = re.search(rf"^## {re.escape(titulo)}\s*$", texto, re.M)
    if not m:
        return ""
    resto = texto[m.end():]
    n = re.search(r"^## ", resto, re.M)
    return (resto[: n.start()] if n else resto).strip()


def titulo_sesion(texto):
    return texto.splitlines()[0].lstrip("# ").strip()


def compilar(nombre_seccion, salida, encabezado):
    partes = [encabezado, ""]
    for g in GUIAS:
        t = g.read_text(encoding="utf-8")
        cuerpo = seccion(t, nombre_seccion)
        if cuerpo:
            partes += [f"## {titulo_sesion(t)}", "", cuerpo, ""]
    (RAIZ / "docs" / salida).write_text("\n".join(partes), encoding="utf-8")
    print("escrito docs/" + salida)


compilar(
    "Conceptos y definiciones",
    "GLOSARIO.md",
    "# Glosario del curso\n\nTodas las definiciones del curso, por sesión. Se genera con `scripts/compilar_docs.py` a partir de las guías, no se edita a mano.",
)
compilar(
    "Quiz",
    "QUIZZES.md",
    "# Quizzes del curso\n\nPreguntas por sesión, listas para pasarse a Google Forms. Se genera con `scripts/compilar_docs.py` a partir de las guías, no se edita a mano.",
)

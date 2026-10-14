#!/usr/bin/env python3
"""Junta los notebooks sueltos en los dos proyectos que reciben los alumnos.

    notebooks/S01..S09.deepnote  ->  dist/curso.deepnote           (proyecto "Curso DE", 1 notebook por sesión)
    notebooks/S10.deepnote       ->  dist/proyecto_final.deepnote  (proyecto "Proyecto final")

Se hace así porque la cuenta Free del alumno permite solo 5 proyectos.
Los IDs de proyecto quedan guardados en scripts/ids_proyectos.json para que cada
build conserve el mismo proyecto y deepnote sync pueda vincularlo.

Uso:  python3 scripts/build_curso.py
Solo incluye los notebooks que existan en notebooks/.
"""
import json
import sys
import uuid
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
IDS = RAIZ / "scripts" / "ids_proyectos.json"

PROYECTOS = {
    "curso": {
        "archivo": "dist/curso.deepnote",
        "nombre": "Curso Data Engineering - Impact Click",
        "sesiones": [f"S{n:02d}" for n in range(1, 10)],
    },
    "proyecto_final": {
        "archivo": "dist/proyecto_final.deepnote",
        "nombre": "Proyecto final - Impact Click",
        "sesiones": ["S10"],
    },
}


class _Literal(str):
    pass


yaml.add_representer(
    _Literal,
    lambda d, v: d.represent_scalar("tag:yaml.org,2002:str", v, style="|"),
    Dumper=yaml.SafeDumper,
)


def _literalizar(obj):
    """Los textos de varias líneas salen como bloque literal, más legibles en git."""
    if isinstance(obj, dict):
        return {k: _literalizar(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_literalizar(v) for v in obj]
    if isinstance(obj, str) and "\n" in obj:
        return _Literal(obj)
    return obj


def main():
    ids = json.loads(IDS.read_text()) if IDS.exists() else {}
    hubo_cambio_ids = False
    (RAIZ / "dist").mkdir(exist_ok=True)

    for clave, cfg in PROYECTOS.items():
        notebooks, base = [], None
        for ses in cfg["sesiones"]:
            ruta = RAIZ / "notebooks" / f"{ses}.deepnote"
            if not ruta.exists():
                print(f"  (falta {ruta.name}, se omite)")
                continue
            datos = yaml.safe_load(ruta.read_text(encoding="utf-8"))
            base = base or datos
            notebooks.extend(datos["project"]["notebooks"])
        if not notebooks:
            print(f"{clave}: sin notebooks, no se genera archivo")
            continue

        # ids únicos de notebook y de bloque
        vistos_nb, vistos_bl = set(), set()
        for nb in notebooks:
            if nb["id"] in vistos_nb:
                sys.exit(f"ID de notebook repetido: {nb['id']}")
            vistos_nb.add(nb["id"])
            for b in nb["blocks"]:
                if b["id"] in vistos_bl:
                    sys.exit(f"ID de bloque repetido: {b['id']}")
                vistos_bl.add(b["id"])

        if clave not in ids:
            ids[clave] = str(uuid.uuid4())
            hubo_cambio_ids = True

        proyecto = dict(base["project"])
        proyecto.update({"id": ids[clave], "name": cfg["nombre"], "notebooks": notebooks})
        salida = {
            "version": base["version"],
            "metadata": base["metadata"],
            "project": proyecto,
        }
        if "environment" in base:
            salida["environment"] = base["environment"]

        destino = RAIZ / cfg["archivo"]
        destino.write_text(
            yaml.safe_dump(_literalizar(salida), allow_unicode=True, sort_keys=False, width=100),
            encoding="utf-8",
        )
        print(f"{clave}: {len(notebooks)} notebook(s) -> {cfg['archivo']}")

    if hubo_cambio_ids:
        IDS.write_text(json.dumps(ids, indent=2) + "\n")
        print("IDs de proyecto guardados en scripts/ids_proyectos.json (haz commit)")


if __name__ == "__main__":
    main()

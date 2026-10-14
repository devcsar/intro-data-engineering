"""Ayudante para armar notebooks .deepnote sin escribir YAML a mano.

Uso:
    from nb import Notebook
    n = Notebook("S02 - Python esencial")
    n.h1("Sesión 2, Python esencial para datos")
    n.callout("Presiona Run all al empezar.", color="blue")
    n.p("Texto explicativo.")
    n.code("print('hola')")
    n.sql("SELECT * FROM viajes LIMIT 5", variable="df_muestra")
    n.guardar("notebooks/S02.deepnote")

Cada archivo generado es un proyecto .deepnote válido con un notebook.
El script scripts/build_curso.py los junta en un solo proyecto.
"""
import sys
import uuid
from datetime import datetime, timezone

import yaml


class _Literal(str):
    pass


def _literal(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(_Literal, _literal, Dumper=yaml.SafeDumper)

REQUIREMENTS = ["polars==1.43.2", "duckdb", "pandera", "plotly", "pyarrow"]
ENTORNO = {"python": {"environment": "uv", "version": "3.13"}}


def _clave(i):
    # a0, a1 ... a9, aa ... az, b0 ... (ordenables como texto)
    letras = "abcdefghijklmnopqrstuvwxyz"
    digitos = "0123456789abcdefghijklmnopqrstuvwxyz"
    return letras[(i // 36) % 26] + digitos[i % 36]


class Notebook:
    def __init__(self, nombre, proyecto="Curso Data Engineering - Impact Click"):
        self.nombre = nombre
        self.proyecto = proyecto
        self.bloques = []

    def _add(self, tipo, contenido, metadata=None):
        bid = uuid.uuid4().hex
        b = {
            "id": bid,
            "blockGroup": bid,
            "type": tipo,
            "sortingKey": _clave(len(self.bloques)),
            "content": _Literal(contenido.rstrip("\n") + "\n")
            if "\n" in contenido
            else contenido,
        }
        if metadata:
            b["metadata"] = metadata
        self.bloques.append(b)
        return self

    def h1(self, t): return self._add("text-cell-h1", t)
    def h2(self, t): return self._add("text-cell-h2", t)
    def h3(self, t): return self._add("text-cell-h3", t)
    def p(self, t): return self._add("text-cell-p", t)
    def bullet(self, t): return self._add("text-cell-bullet", t)
    def callout(self, t, color="blue"): return self._add("text-cell-callout", t, {"color": color})
    def markdown(self, t): return self._add("markdown", t)
    def code(self, t): return self._add("code", t)

    def sql(self, consulta, variable, integracion="deepnote-dataframe-sql"):
        return self._add(
            "sql",
            consulta,
            {
                "sql_integration_id": integracion,
                "deepnote_variable_name": variable,
                "deepnote_return_variable_type": "dataframe",
            },
        )

    def a_dict(self):
        return {
            "version": "1.0.0",
            "metadata": {"createdAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            "project": {
                "id": str(uuid.uuid4()),
                "name": self.proyecto,
                "notebooks": [
                    {
                        "id": str(uuid.uuid4()),
                        "name": self.nombre,
                        "executionMode": "block",
                        "isModule": False,
                        "blocks": self.bloques,
                    }
                ],
                "settings": {"requirements": REQUIREMENTS},
            },
            "environment": ENTORNO,
        }

    def guardar(self, ruta):
        with open(ruta, "w", encoding="utf-8") as f:
            yaml.safe_dump(self.a_dict(), f, allow_unicode=True, sort_keys=False, width=100)
        print("escrito", ruta, "con", len(self.bloques), "bloques", file=sys.stderr)

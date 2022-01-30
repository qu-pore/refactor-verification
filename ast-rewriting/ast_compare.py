from __future__ import annotations

import ast
from enum import Enum
from pathlib import Path
from pprint import pprint

pp = lambda p: pprint(p, sort_dicts=False)

def simplify(node):
    """
    Modified version of AST pprinter https://stackoverflow.com/a/19598419/
    """
    ignored_node_attributes = (
        "lineno end_lineno col_offset end_col_offset ctx type_comment keywords"
    )
    if isinstance(node, ast.AST):
        res = vars(node).copy()
        for k in ignored_node_attributes.split():
            res.pop(k, None)
        for k, v in res.items():
            res[k] = simplify(v)
        res["__type__"] = type(node).__name__
        return res
    elif isinstance(node, list):
        return list(map(simplify, node))
    else:
        return node

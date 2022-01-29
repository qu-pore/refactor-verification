from __future__ import annotations

import ast
from enum import Enum
from pathlib import Path
from pprint import pprint

pp = lambda p: pprint(p, sort_dicts=False)


class Handlers(Enum):
    guarded = "guarded_handler.py"
    ternary = "ternary_handler.py"
    linear = "handler.py"


all_handler_programs = [ast.parse(Path(h.value).read_text()) for h in Handlers]
all_handler_functions = [tree.body[1] for tree in all_handler_programs]
assert all("handler" in f.name for f in all_handler_functions)
f0, f1, f2 = all_handler_functions

def simplify(node):
    """
    Modified version of AST pprinter https://stackoverflow.com/a/19598419/
    """
    if isinstance(node, ast.AST):
        res = vars(node).copy()
        for k in "lineno end_lineno col_offset end_col_offset ctx".split():
            res.pop(k, None)
        for k, v in res.items():
            res[k] = simplify(v)
        res["__type__"] = type(node).__name__
        return res
    elif isinstance(node, list):
        return list(map(simplify, node))
    else:
        return node

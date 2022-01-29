from __future__ import annotations


def double(a: int | None) -> int | None:
    if a is None:
        output = None
    elif a > 2:
        output = (a * 2)
    else:
        output = None
    return output

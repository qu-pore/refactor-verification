from __future__ import annotations


def guarded_double(a: int | None) -> int | None:
    if a is None:
        return None
    return a * 2

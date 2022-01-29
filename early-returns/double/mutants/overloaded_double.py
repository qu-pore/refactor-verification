from __future__ import annotations

from typing import overload


@overload
def overloaded_double(a: int) -> int:
    ...


@overload
def overloaded_double(a: None) -> None:
    ...


def overloaded_double(a: int | None) -> int | None:
    if a is None:
        output = None
    elif a > 2:
        output = (a * 2)
    else:
        output = None
    return output

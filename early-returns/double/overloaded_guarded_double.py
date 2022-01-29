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
        return None
    return a * 2

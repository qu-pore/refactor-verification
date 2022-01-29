from __future__ import annotations

from typing import overload


@overload
def overloaded_double(a: int) -> int:
    ...


@overload
def overloaded_double(a: None) -> None:
    ...


def overloaded_double(a: int | None) -> int | None:
    return None if a is None else (a * 2)

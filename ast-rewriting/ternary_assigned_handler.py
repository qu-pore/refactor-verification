from __future__ import annotations


def ternary_handler(event: dict) -> int | None:
    payload = event.get("payload")
    output = None if payload is None else len(payload)
    return output

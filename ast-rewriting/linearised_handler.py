from __future__ import annotations


def ternary_assigned_handler(event: dict) -> int | None:
    payload = event.get("payload")
    if payload is None:
        payload = None
    else:
        payload = len(payload)
    return output

from __future__ import annotations


def handler(event: dict) -> int | None:
    payload = event.get("payload")
    if payload is None:
        output = None
    else:
        output = len(payload)
    return output

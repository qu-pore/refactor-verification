from __future__ import annotations


def ternary_handler(event: dict) -> int | None:
    return None if (payload := event.get("payload")) is None else len(payload)

from __future__ import annotations


def ternary_walrusless_handler(event: dict) -> int | None:
    payload = event.get("payload")
    return None if payload is None else len(payload)

from __future__ import annotations


def guarded_handler(event: dict[str, str]) -> int | None:
    if (payload := event.get("payload")) is None:
        return None
    return len(payload)

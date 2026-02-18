from __future__ import annotations

from datetime import datetime


def format_timestamp(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M")

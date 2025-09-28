from __future__ import annotations

import os


def get_env(name: str, default: str | None = None) -> str | None:
    return os.environ.get(name, default)

def get_api_key() -> str | None:
    return get_env("QWEN_API_KEY")

# core/merge_utils.py

from collections.abc import Mapping
from typing import Any


def apply_merge(target: dict, key: str, value: Any, strategy: str = "overwrite") -> dict:
    if key not in target:
        target[key] = value
    elif strategy == "overwrite":
        target[key] = value
    elif strategy == "merge":
        target[key] = deep_merge(target[key], value)
    return target


def deep_merge(a: Any, b: Any) -> Any:
    if isinstance(a, dict) and isinstance(b, dict):
        result = dict(a)
        for k, v in b.items():
            result[k] = deep_merge(result.get(k), v)
        return result
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    return b
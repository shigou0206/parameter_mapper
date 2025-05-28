# utils/error_handler.py

from typing import Any
from utils.logger import logger

def safe_apply(executor, item, context) -> Any:
    try:
        return executor.apply(item, context)
    except Exception as e:
        logger.error(f"Error applying mapping '{item.key}': {e}")
        if item.onError == "default":
            return item.default
        return None
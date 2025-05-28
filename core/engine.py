# core/engine.py

from typing import List, Dict
from dsl.models import MappingItem
from core.dispatcher import get_step_executor
from core.merge_utils import apply_merge
from utils.error_handler import safe_apply


def apply_mappings(input_json: Dict, mappings: List[MappingItem]) -> Dict:
    output = {}

    for item in mappings:
        executor = get_step_executor(item.type)
        value = safe_apply(executor, item, input_json)
        output = apply_merge(output, item.key, value, item.mergeStrategy)

    return output
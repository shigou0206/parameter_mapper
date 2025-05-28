# steps/object_step.py

from steps.base import BaseStep
from dsl.models import MappingItem
from utils.error_handler import safe_apply
from core.merge_utils import apply_merge

class ObjectStep(BaseStep):
    def apply(self, item: MappingItem, context: dict):
        from core.dispatcher import get_step_executor 
        
        result = {}

        for child in item.children or []:
            executor = get_step_executor(child.type)
            value = safe_apply(executor, child, context)
            result = apply_merge(result, child.key, value, child.mergeStrategy)

        return result
# steps/list_step.py

from jsonpath_ng.ext import parse
from steps.base import BaseStep
from dsl.models import MappingItem
from utils.error_handler import safe_apply

class ListStep(BaseStep):
    def apply(self, item: MappingItem, context: dict):
        from core.dispatcher import get_step_executor  # 👈 延迟导入（Lazy Import）

        source_expr = parse(item.source)
        matches = [match.value for match in source_expr.find(context)]

        item_list = matches[0] if matches else []

        results = []
        for raw_item in item_list:
            scope = {item.itemName or "item": raw_item}
            obj = {}

            for child in item.children or []:
                executor = get_step_executor(child.type)
                value = safe_apply(executor, child, scope)
                obj[child.key] = value

            results.append(obj)

        return results
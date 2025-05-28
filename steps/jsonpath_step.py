# steps/jsonpath_step.py

from jsonpath_ng.ext import parse
from steps.base import BaseStep
from dsl.models import MappingItem

class JsonPathStep(BaseStep):
    def apply(self, item: MappingItem, context: dict):
        expr = parse(item.source)
        matches = [match.value for match in expr.find(context)]
        if not matches:
            return None
        return matches[0] if len(matches) == 1 else matches
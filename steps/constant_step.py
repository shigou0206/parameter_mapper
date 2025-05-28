# steps/constant_step.py

from steps.base import BaseStep
from dsl.models import MappingItem

class ConstantStep(BaseStep):
    def apply(self, item: MappingItem, context: dict):
        return item.value
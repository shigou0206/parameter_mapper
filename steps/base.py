# steps/base.py

from typing import Any
from dsl.models import MappingItem

class BaseStep:
    def apply(self, item: MappingItem, context: dict) -> Any:
        raise NotImplementedError("Subclasses must implement this method")
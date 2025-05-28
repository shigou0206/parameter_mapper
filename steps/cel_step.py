# steps/cel_step.py

from steps.base import BaseStep
from dsl.models import MappingItem
from celpy import Environment, json_to_cel, celtypes

class CelStep(BaseStep):
    def apply(self, item: MappingItem, context: dict):
        env = Environment()
        ast = env.compile(item.transform)
        program = env.program(ast)

        cel_context = {"input": json_to_cel(context)}
        result = program.evaluate(cel_context)

        return self.cel_to_python(result)

    def cel_to_python(self, value):
        if isinstance(value, celtypes.BoolType):
            return bool(value)
        elif isinstance(value, celtypes.IntType):
            return int(value)
        elif isinstance(value, celtypes.DoubleType):
            return float(value)
        elif isinstance(value, celtypes.StringType):
            return str(value)
        elif isinstance(value, celtypes.ListType):
            return [self.cel_to_python(v) for v in value]
        elif isinstance(value, celtypes.MapType):
            return {self.cel_to_python(k): self.cel_to_python(v) for k, v in value.items()}
        elif value is None or isinstance(value, celtypes.NullType):
            return None
        else:
            raise ValueError(f"Unsupported CEL type: {type(value)}")
# core/dispatcher.py

from steps.jsonpath_step import JsonPathStep
from steps.cel_step import CelStep
from steps.constant_step import ConstantStep
from steps.template_step import TemplateStep
from steps.object_step import ObjectStep
from steps.list_step import ListStep


def get_step_executor(step_type: str):
    executors = {
        "jsonpath": JsonPathStep(),
        "cel": CelStep(),
        "constant": ConstantStep(),
        "template": TemplateStep(),
        "object": ObjectStep(),
        "list": ListStep(),
    }
    executor = executors.get(step_type)
    if executor is None:
        raise ValueError(f"Unsupported step type: {step_type}")
    return executor
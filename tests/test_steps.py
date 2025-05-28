import pytest
from steps.jsonpath_step import JsonPathStep
from steps.cel_step import CelStep
from steps.constant_step import ConstantStep
from dsl.models import MappingItem

def test_jsonpath_step():
    step = JsonPathStep()
    item = MappingItem(key="name", type="jsonpath", source="$.user.name")
    context = {"user": {"name": "Bob"}}

    result = step.apply(item, context)
    assert result == "Bob"

def test_cel_step():
    step = CelStep()
    item = MappingItem(key="isAdult", type="cel", transform="input.age >= 18")
    context = {"age": 20}

    result = step.apply(item, context)
    assert result == True

def test_constant_step():
    step = ConstantStep()
    item = MappingItem(key="status", type="constant", value="active")
    context = {}

    result = step.apply(item, context)
    assert result == "active"
import pytest
from core.engine import apply_mappings
from dsl.models import MappingItem

@pytest.fixture
def sample_input():
    return {
        "user": {
            "name": "Alice",
            "age": 28,
            "roles": ["admin", "editor"]
        }
    }

def test_apply_simple_mapping(sample_input):
    mappings = [
        MappingItem(key="username", type="jsonpath", source="$.user.name"),
        MappingItem(key="isAdult", type="cel", transform="input.user.age >= 18"),
    ]

    result = apply_mappings(sample_input, mappings)

    assert result == {
        "username": "Alice",
        "isAdult": True
    }

def test_apply_constant_mapping(sample_input):
    mappings = [
        MappingItem(key="fixedValue", type="constant", value="test123"),
    ]

    result = apply_mappings(sample_input, mappings)

    assert result == {"fixedValue": "test123"}
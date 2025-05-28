# dsl/models.py

from pydantic import BaseModel, ConfigDict
from typing import Any, Optional, List, Literal

class MappingItem(BaseModel):
    key: str
    type: Literal["jsonpath", "cel", "constant", "template", "object", "list"]

    source: Optional[str] = None
    transform: Optional[str] = None
    value: Optional[Any] = None
    template: Optional[str] = None

    children: Optional[List["MappingItem"]] = None
    itemName: Optional[str] = "item"

    mergeStrategy: Literal["overwrite", "merge"] = "overwrite"
    onError: Literal["default", "skip"] = "default"
    default: Optional[Any] = None

    # 使用新版Pydantic ConfigDict替代旧版Config
    model_config = ConfigDict(arbitrary_types_allowed=True)

# 使用新版方法替代update_forward_refs()
MappingItem.model_rebuild()
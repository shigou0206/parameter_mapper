# api/schemas.py
from pydantic import BaseModel
from typing import Any, List, Optional

class MappingRequest(BaseModel):
    input: dict
    mappings: List[dict]

class MappingResponse(BaseModel):
    output: dict
    errors: Optional[List[str]] = []

class ErrorResponse(BaseModel):
    detail: str
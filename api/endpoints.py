from fastapi import APIRouter, HTTPException
from api.schemas import MappingRequest, MappingResponse, ErrorResponse
from core.engine import apply_mappings
from utils.logger import logger
from dsl.models import MappingItem

router = APIRouter()

@router.post(
    "/map-preview",
    response_model=MappingResponse,
    responses={500: {"model": ErrorResponse}},
)
def map_preview(req: MappingRequest):
    logger.info(f"Received mapping preview request: {req.dict()}")
    try:
        # 关键修改点：明确转换为MappingItem对象
        mappings = [MappingItem(**item.dict()) if isinstance(item, MappingItem) else MappingItem(**item)
                    for item in req.mappings]

        output = apply_mappings(req.input, mappings)
        logger.info(f"Mapping output: {output}")
        return MappingResponse(output=output, errors=[])
    except Exception as e:
        logger.error(f"Mapping preview failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
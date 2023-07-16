import json

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from rates.schemas import CalculateResult, RateCreateSchema, RatesByDate
from rates.utils import create_or_update_rate_json


router = APIRouter(
    prefix='/insurance',
    tags=['Insurance']
)


@router.post('/upload/file')
async def upload_rates_file(upload_file: UploadFile) -> RateCreateSchema:
    if upload_file.content_type not in ['application/json', ]:
        raise HTTPException(
            400,
            detail=f'File type of {upload_file.content_type} is not supported'
        )

    json_data = json.load(upload_file.file)
    rates_by_date = RatesByDate(**json_data)

    response = await create_or_update_rate_json(rates_by_date.root)

    return JSONResponse(content=jsonable_encoder(response))


@router.post('/upload/json')
async def upload_rates_json(json_data: RatesByDate) -> RateCreateSchema:

    response = await create_or_update_rate_json(json_data.root)

    return JSONResponse(content=jsonable_encoder(response))


@router.post('/calculate')
async def calculate_insurance_cost() -> CalculateResult:
    pass

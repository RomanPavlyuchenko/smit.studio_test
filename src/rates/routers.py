from datetime import date
import json

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import HTTPNotFoundError

from rates.schemas import (
    CalculateResult,
    RateCreateSchema,
    RateSchema,
    RatesByDate,
    HTTPUnsupportedMediaTypeError,
)
from rates.utils import create_or_update_rate_json
from rates.models import Rate


router = APIRouter(
    prefix='/insurance',
    tags=['Insurance']
)


@router.post(
        '/upload/file',
        responses={415: {'model': HTTPUnsupportedMediaTypeError}},
)
async def upload_rates_file(upload_file: UploadFile) -> RateCreateSchema:

    if upload_file.content_type not in ['application/json', ]:
        raise HTTPException(
            415,
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


@router.get('/calculate', responses={404: {'model': HTTPNotFoundError}})
async def calculate_insurance_cost(
        cargo_type: str, declared_value: float,
        date_from: date = None) -> CalculateResult:

    if date_from is None:
        date_from = date.today()

    insurnce_rate = await Rate.filter(
        cargo_type=cargo_type, date_from__lte=date_from).order_by(
        'date_from').first()

    if insurnce_rate is None:
        raise HTTPException(status_code=404, detail=f'Rate for {cargo_type} not found')

    insurance_cost = declared_value * insurnce_rate.rate
    return CalculateResult(insurance_cost=insurance_cost)


@router.get('/rate')
async def get_rate(cargo_type: str, date_from: date = None) -> RateSchema:

    if date_from is None:
        date_from = date.today()

    response = await Rate.filter(
        cargo_type=cargo_type, date_from__lte=date_from).order_by(
        'date_from').first()

    return RateSchema.model_validate(response)

from fastapi import APIRouter
from fastapi import UploadFile

from rates.schemas import CalculateResult


router = APIRouter(
    prefix='/insurance',
    tags=['Insurance']
)


@router.post('/file/')
async def upload_rates_file(file: UploadFile):
    return {
        'filename': file.filename,
        'content_type': file.content_type,
        'file': file.file,
        'size': file.size,
    }


@router.post('/calculate')
async def calculate_insurance_cost() -> CalculateResult:
    pass

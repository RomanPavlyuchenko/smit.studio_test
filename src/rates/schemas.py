from datetime import date
from typing import Dict, List

from pydantic import BaseModel, Field, RootModel, condecimal


class RateSchema(BaseModel):
    cargo_type: str = Field(max_length=50)
    rate: float
    date_from: date

    class Config:
        json_schema_extra = {
            "example": {
                "cargo_type": "Glass",
                "rate": 0.04,
                "date_from": "2023-06-01"
            }
        }
        from_attributes = True


class RateCreateSchema(BaseModel):
    created: List[RateSchema]
    updated: List[RateSchema]


class CalculateResult(BaseModel):
    insurance_cost: float


class CargoItem(BaseModel):
    cargo_type: str
    rate: condecimal(gt=0)


class RatesByDate(RootModel):
    root: Dict[date, List[CargoItem]]


class HTTPUnsupportedMediaTypeError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "Unsupported file extension."},
        }

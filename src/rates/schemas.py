from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Rate


RateSchema = pydantic_model_creator(Rate, name='Rate')

class CalculateResult(BaseModel):
    insurance_cost: float

from typing import List
from rates.models import Rate
from rates.schemas import RateSchema, RatesByDate


async def create_or_update_rate_json(
        json_data: RatesByDate) -> List[RateSchema]:

    processed = {
        'created': list(),
        'updated': list()
    }

    for rate_date, rates in json_data.items():
        for rate in rates:
            created_rate, is_created = await Rate.update_or_create(
                defaults={'rate': rate.rate},
                cargo_type=rate.cargo_type,
                date_from=rate_date
            )
            created_rate = RateSchema.model_validate(created_rate).model_dump()

            processed['created'].append(
                created_rate
            ) if is_created else processed['updated'].append(created_rate)

    return processed

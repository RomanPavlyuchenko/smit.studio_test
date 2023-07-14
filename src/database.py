from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import settings


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=settings.TORTOISE_ORM,
    )

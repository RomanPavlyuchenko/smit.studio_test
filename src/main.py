from fastapi import FastAPI

from database import init_db
from rates.routers import router as rates_router


app = FastAPI(
    title='Сost of insurance'
)

init_db(app)

app.include_router(rates_router)

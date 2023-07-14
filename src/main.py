from fastapi import FastAPI

from database import init_db


app = FastAPI(
    title='Сost of insurance'
)

init_db(app)

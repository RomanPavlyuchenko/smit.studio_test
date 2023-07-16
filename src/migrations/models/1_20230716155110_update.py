from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "rate" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(50) NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "date_from" DATE NOT NULL,
    CONSTRAINT "uid_rate_rate_3b54cf" UNIQUE ("rate", "date_from")
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "rate";"""

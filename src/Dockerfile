FROM python:3.11-slim

RUN mkdir /fastapi_app
WORKDIR /fastapi_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat-traditional postgresql

COPY ./pyproject.toml /fastapi_app/
COPY ./poetry.lock /fastapi_app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 8000

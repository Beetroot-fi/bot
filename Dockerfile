FROM python:3.11.9-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY . .

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/bot

CMD poetry run -m bot
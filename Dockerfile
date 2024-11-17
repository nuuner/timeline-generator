FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY src/ ./src/

EXPOSE 3000

CMD ["poetry", "run", "uvicorn", "src.timeline_generator.main:app", "--host", "0.0.0.0", "--port", "3000"]

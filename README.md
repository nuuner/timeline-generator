# Timeline Generator

A FastAPI service that generates minimalistic vertical SVG timelines from event data.

## Quick Start with Docker

```bash
docker compose up -d
```

The service will be available at http://localhost

## Local Development

Install dependencies:
```bash
poetry install
```

Start the development server:
```bash
poetry run uvicorn src.timeline_generator.main:app --reload
```

## Usage

Generate a timeline by making a GET request to `/timeline.svg` with your events as a JSON string:

```bash
curl "http://localhost:8000/timeline.svg?events=[{\"title\":\"Event 1\",\"date\":\"2024-02-15 09:30\",\"color\":\"blue\"}]" > timeline.svg
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

GNU General Public License v3.0 - See LICENSE file for details
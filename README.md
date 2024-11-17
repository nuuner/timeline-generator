# Timeline Generator

A FastAPI service that generates minimalistic vertical SVG timelines from event data.

## Quick Start with Docker

```bash
docker compose up -d
```

The service will be available at http://localhost:3000

## Example

Input events:
```json
[
  {
    "title": "Project Kickoff Meeting",
    "date": "2024-03-01 09:00",
    "color": "blue"
  },
  {
    "title": "Design Review",
    "date": "2024-03-01 14:30",
    "color": "purple"
  },
  {
    "title": "Client Presentation",
    "date": "2024-03-03 11:00",
    "color": "green"
  },
  {
    "title": "Team Workshop",
    "date": "2024-03-07 13:00",
    "color": "orange"
  },
  {
    "title": "Project Deadline",
    "date": "2024-03-15 17:00",
    "color": "red"
  }
]
```

Output:

![Example Timeline](example_output.svg)

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
curl "http://localhost:3000/timeline.svg?events=[{\"title\":\"Event 1\",\"date\":\"2024-02-15 09:30\",\"color\":\"blue\"}]" > timeline.svg
```

## API Documentation

- Swagger UI: http://localhost:3000/docs
- ReDoc: http://localhost:3000/redoc

## License

GNU General Public License v3.0 - See LICENSE file for details
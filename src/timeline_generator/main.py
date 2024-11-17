from fastapi import FastAPI, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from .models import Event
from .drawing import generate_timeline


def unserialize_events(events: str) -> list[Event]:
    import json
    from .models import EventInput, Event

    try:
        event_list = json.loads(events)
        return [Event.from_input(EventInput(**event)) for event in event_list]
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(
    "/timeline.svg",
    response_class=Response,
    responses={
        200: {
            "content": {"image/svg+xml": {}},
            "description": "Returns an SVG timeline visualization",
        }
    },
)
async def get_timeline(
    events: str = Query(
        ...,
        description='JSON string of events in format: [{"title": "Event 1", "date": "2024-02-15 09:30", "color": "blue"}]',
    )
):
    events_list = unserialize_events(events)
    drawing = generate_timeline(events_list)
    return Response(content=drawing.as_svg(), media_type="image/svg+xml")

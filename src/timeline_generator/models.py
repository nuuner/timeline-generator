from datetime import datetime
from pydantic import BaseModel


class EventInput(BaseModel):
    title: str
    date: str
    color: str


class Event:
    def __init__(self, title: str, date: datetime, color: str):
        self.title = title
        self.date = date
        self.color = color

    @classmethod
    def from_input(cls, event_input: EventInput) -> "Event":
        return cls(
            title=event_input.title,
            date=datetime.strptime(event_input.date, "%Y-%m-%d %H:%M"),
            color=event_input.color,
        )

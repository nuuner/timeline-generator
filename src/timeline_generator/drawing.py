import drawsvg as draw
from .models import Event


def create_line(
    d, x1, y1, x2, y2, stroke="black", stroke_width=2, stroke_dasharray=None
):
    """Helper function to create a line with consistent styling"""
    line = draw.Line(
        x1,
        y1,
        x2,
        y2,
        stroke=stroke,
        stroke_width=stroke_width,
        stroke_dasharray=stroke_dasharray if stroke_dasharray else None,
    )
    d.append(line)


def create_text(d, text, x, y, color="black", text_anchor="start"):
    """Helper function to create text with consistent styling"""
    text_elem = draw.Text(
        text,
        14,
        x,
        y,
        text_anchor=text_anchor,
        center=0.5,
        fill=color,
        font_family="Helvetica",
    )
    d.append(text_elem)


def create_date_circle(d, x, y):
    """Helper function to create date circles with consistent styling"""
    d.append(
        draw.Circle(x, y, 5, fill="white", stroke="black", center=0.5, stroke_width=2)
    )


def draw_date_gap(d, line_x, y, days_between):
    """Handle drawing the gap between dates"""
    if days_between == 1:
        create_line(d, line_x, y - 20, line_x, y)
    elif days_between <= 3:
        # Draw continuous lines for 1-3 days
        for _ in range(days_between - 1):
            create_line(d, line_x, y - 20, line_x, y + 20)
            y += 20
    else:
        # Draw pattern for gaps > 3 days: solid-dotted-solid
        create_line(d, line_x, y - 20, line_x, y)
        y += 20

        create_line(d, line_x, y - 20, line_x, y, stroke_dasharray="2,2")
        create_text(d, f"{days_between}d", line_x - 10, y - 10, text_anchor="end")
        y += 20

        create_line(d, line_x, y - 20, line_x, y)

    return y


def draw_event(d, line_x, y, event):
    """Draw a single event with its time and title"""
    create_text(
        d,
        f"{event.date.strftime('%H:%M')} - {event.title}",
        line_x + 15,
        y,
        color=event.color,
    )


def generate_timeline(events: list[Event]):
    # Sort events by date
    events.sort(key=lambda x: x.date)

    # Calculate canvas dimensions
    start_date = events[0].date
    end_date = events[-1].date
    total_days = (end_date - start_date).days
    width = 500
    height = total_days * 20 + 100
    padding = 20
    line_x = 100
    biggest_x = 0

    d = draw.Drawing(width, height)

    # Group events by date
    events_for_day = {}
    for event in events:
        date = event.date.date()
        if date not in events_for_day:
            events_for_day[date] = []
        events_for_day[date].append(event)

    y = padding
    prev_date = None
    circle_y = y

    for date, day_events in events_for_day.items():
        if prev_date:
            days_between = (date - prev_date).days
            y = draw_date_gap(d, line_x, y, days_between)

        create_date_circle(d, line_x, circle_y)
        create_text(d, date.strftime("%d.%m.%Y"), line_x - 15, y, text_anchor="end")

        # Draw first event
        draw_event(d, line_x, y, day_events[0])
        circle_y = y
        y += 20

        # Draw remaining events for this day
        for event in day_events[1:]:
            create_line(d, line_x, y - 20, line_x, y)
            draw_event(d, line_x, y, event)
            y += 20

        prev_date = date

    create_date_circle(d, line_x, circle_y)

    # Set the actual height to match the content
    d.height = padding + y
    # Set viewBox to maintain proper scaling
    d.view_box = f"0 0 {width} {padding + y}"
    return d

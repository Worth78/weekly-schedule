"""
Generate static .ics file for Apple Calendar subscription.
Run this whenever you update the schedule, then push to GitHub.
"""

from datetime import datetime, timedelta
import random
import string

def generate_uid():
    """Generate unique ID for calendar event."""
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    return f"{int(datetime.now().timestamp())}-{rand}@schedule"

def format_datetime(dt):
    """Format datetime for ICS."""
    return dt.strftime("%Y%m%dT%H%M%S")

def create_event(date, start_hour, start_min, end_hour, end_min, title, description, alarm_minutes=5):
    """Create a calendar event with alarm."""
    start = date.replace(hour=start_hour, minute=start_min, second=0)
    end = date.replace(hour=end_hour, minute=end_min, second=0)

    event = f"""BEGIN:VEVENT
UID:{generate_uid()}
DTSTAMP:{format_datetime(datetime.now())}
DTSTART:{format_datetime(start)}
DTEND:{format_datetime(end)}
SUMMARY:{title}
DESCRIPTION:{description}
BEGIN:VALARM
TRIGGER:-PT{alarm_minutes}M
ACTION:DISPLAY
DESCRIPTION:{title} in {alarm_minutes} minutes
END:VALARM
BEGIN:VALARM
TRIGGER:PT0M
ACTION:AUDIO
END:VALARM
END:VEVENT
"""
    return event

def generate_calendar():
    """Generate the full calendar."""
    # Find next Monday
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    next_monday = today + timedelta(days=days_until_monday)
    next_monday = next_monday.replace(hour=0, minute=0, second=0, microsecond=0)

    events = ""

    # Monday through Friday
    for i in range(5):
        date = next_monday + timedelta(days=i)

        # Common weekday events
        events += create_event(date, 7, 0, 7, 15, "Wake Up", "Alarm off. Feet on floor. Make bed.", 0)
        events += create_event(date, 7, 15, 7, 25, "Prayer", "10 minutes. Quiet, focused, no phone.", 0)
        events += create_event(date, 7, 35, 7, 50, "Morning Yoga", "15-minute flow", 0)
        events += create_event(date, 7, 55, 8, 10, "Breakfast", "Quick breakfast", 0)
        events += create_event(date, 8, 15, 8, 30, "Pre-Market Prep", "Review watchlist, overnight news, set alerts", 5)
        events += create_event(date, 8, 30, 12, 0, "TRADING SESSION", "Full focus. Execute the plan. Log all trades.", 5)
        events += create_event(date, 10, 30, 10, 35, "Water Break", "Stand up. Stretch. Refill water.", 0)
        events += create_event(date, 12, 5, 12, 30, "Lunch", "Eat and recharge", 5)
        events += create_event(date, 12, 45, 16, 15, "CODING SESSION", "SuperTradeBros development", 5)
        events += create_event(date, 14, 0, 14, 10, "Coding Break", "Water. Walk around. Rest eyes.", 0)

        if i == 1:  # Tuesday
            events += create_event(date, 15, 15, 15, 30, "Pre-Workout", "Snack + change clothes", 5)
            events += create_event(date, 15, 30, 16, 20, "WORKOUT", "Light-Moderate Legs (Home)", 5)
            events += create_event(date, 16, 50, 17, 10, "Dinner (Early)", "Quick meal before class", 5)
            events += create_event(date, 17, 50, 18, 0, "Travel to Algo Class", "Leave for class", 10)
            events += create_event(date, 18, 0, 22, 0, "ALGO CLASS", "Full focus. Take good notes.", 5)
            events += create_event(date, 22, 10, 22, 30, "Wind Down", "Quick yoga + bed prep", 0)
            events += create_event(date, 22, 30, 22, 31, "LIGHTS OUT", "Sleep!", 5)
        else:
            events += create_event(date, 16, 15, 16, 30, "Pre-Workout", "Snack + change clothes", 5)
            if i in [2, 4]:  # Wed & Fri - gym days
                workout_name = "Moderate Upper" if i == 2 else "Heavy Lower + Pulls"
                events += create_event(date, 16, 30, 17, 30, "WORKOUT (Gym)", workout_name, 5)
            else:
                workout_name = "Light Upper + Pull-ups" if i == 0 else "Moderate-Heavy Full Body"
                events += create_event(date, 16, 30, 17, 15, "WORKOUT (Home)", workout_name, 5)
            events += create_event(date, 18, 15, 18, 35, "Dinner", "Sit down. No screens. Enjoy the food.", 5)
            events += create_event(date, 18, 55, 19, 25, "Market Analysis", "Review market. Prep watchlist.", 5)
            events += create_event(date, 21, 0, 21, 10, "SCREEN CURFEW", "All screens off. Evening yoga.", 5)
            events += create_event(date, 21, 35, 21, 45, "Bed Prep", "Brush teeth. Set alarm.", 0)
            events += create_event(date, 21, 45, 21, 46, "LIGHTS OUT", "9+ hours of sleep.", 5)

    # Saturday
    saturday = next_monday + timedelta(days=5)
    events += create_event(saturday, 7, 0, 7, 15, "Wake Up", "Make bed.", 0)
    events += create_event(saturday, 7, 15, 7, 25, "Prayer", "10 minutes", 0)
    events += create_event(saturday, 7, 35, 7, 50, "Morning Yoga", "15-minute flow", 0)
    events += create_event(saturday, 7, 50, 8, 15, "Breakfast", "Peak day needs fuel", 0)
    events += create_event(saturday, 8, 55, 10, 15, "Coding / Projects", "Deep focus coding", 5)
    events += create_event(saturday, 11, 0, 12, 5, "PEAK WORKOUT (Gym)", "Power cleans, heavy squats, bench", 15)
    events += create_event(saturday, 12, 45, 13, 10, "Lunch", "", 5)
    events += create_event(saturday, 13, 20, 16, 30, "Coding / Projects", "", 5)
    events += create_event(saturday, 19, 0, 19, 30, "Weekly Review", "Trading, coding, fitness review", 5)
    events += create_event(saturday, 21, 0, 21, 10, "SCREEN CURFEW", "Evening yoga", 5)
    events += create_event(saturday, 21, 45, 21, 46, "LIGHTS OUT", "9+ hours sleep", 5)

    # Sunday
    sunday = next_monday + timedelta(days=6)
    events += create_event(sunday, 6, 30, 6, 45, "Wake Up", "Early for church.", 0)
    events += create_event(sunday, 6, 45, 7, 0, "Prayer", "15 min. Reflect on the week.", 0)
    events += create_event(sunday, 7, 5, 7, 20, "Morning Yoga", "15-minute flow", 0)
    events += create_event(sunday, 7, 20, 7, 50, "Get Ready for Church", "Shower, dress", 0)
    events += create_event(sunday, 8, 0, 8, 30, "Travel to Church", "Leave for church", 10)
    events += create_event(sunday, 8, 30, 9, 30, "CHURCH", "", 0)
    events += create_event(sunday, 9, 45, 10, 15, "Brunch", "Cook something you enjoy", 5)
    events += create_event(sunday, 11, 30, 12, 15, "Grocery Run", "Get items for meal prep", 10)
    events += create_event(sunday, 12, 30, 15, 0, "MEAL PREP", "Batch cook for the week", 10)
    events += create_event(sunday, 15, 0, 15, 30, "Light Walk", "Active recovery. No phone.", 0)
    events += create_event(sunday, 18, 35, 19, 20, "Weekly Planning", "Set Monday plan, coding goals", 5)
    events += create_event(sunday, 21, 0, 21, 10, "SCREEN CURFEW", "Monday starts NOW.", 5)
    events += create_event(sunday, 21, 45, 21, 46, "LIGHTS OUT", "9+ hours to 7:00 AM", 5)

    # Build full calendar
    calendar = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Disciplined Trader Schedule//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Weekly Schedule
X-WR-TIMEZONE:America/New_York
{events}END:VCALENDAR"""

    return calendar

def main():
    ics_content = generate_calendar()

    with open("weekly_schedule.ics", "w", encoding="utf-8") as f:
        f.write(ics_content)

    print("Generated weekly_schedule.ics")
    print("Next steps:")
    print("  1. git add .")
    print("  2. git commit -m 'Update schedule'")
    print("  3. git push")

if __name__ == "__main__":
    main()

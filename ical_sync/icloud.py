
from caldav import Calendar, DAVClient

def get_icloud_calendar(username: str, password: str, calendar_name: str) -> Calendar | None:

    client = DAVClient(url="https://caldav.icloud.com", username=username, password=password)
    principal = client.principal()

    for calendar in principal.calendars():
        if calendar.name.lower() == calendar_name.lower():
            return calendar

    return None
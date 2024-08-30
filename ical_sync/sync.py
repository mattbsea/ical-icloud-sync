

import caldav
import icalendar
from loguru import logger


def prune_deleted_events(apple_cal: caldav.Calendar, ical_cal: icalendar.Calendar, ical_url: str):
    ical_event_ids = [str(e["UID"]) for e in ical_cal.walk("VEVENT")]

    for apple_event in apple_cal.events():
        apple_ical_url = apple_event.icalendar_component.get("X-ICAL-SYNC-URL")
        if apple_ical_url != ical_url:
            continue

        if str(apple_event.icalendar_component.get("UID")) not in ical_event_ids:
            logger.info("Removing event from apple calendar: {}", apple_event.icalendar_instance.to_ical())
            apple_event.delete()


def sync_calendar_events(apple_cal: caldav.Calendar, ical_cal: icalendar.Calendar, ical_url: str):

    for ical_event in ical_cal.walk("VEVENT"):
        ical_event['X-ICAL-SYNC-URL'] = ical_url

        logger.info("Upserted to apple calendar: {}", ical_event.to_ical())
        apple_event = apple_cal.save_event(ical_event.to_ical())

from loguru import logger
import requests
import icalendar


def get_ical_subscription(ical_url: str) -> icalendar.Calendar | None:

    response = requests.get(ical_url)
    if response.status_code < 200 or response.status_code >= 300:
        logger.error("Bad response for URL {} {}", ical_url, response.reason)
        return None

    return icalendar.Calendar.from_ical(response.text)

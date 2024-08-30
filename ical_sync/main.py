import time
from loguru import logger
import click

from . import icloud, ical, sync

@click.command()
@click.option("--icloud-user", envvar="ICLOUD_USER", required=True)
@click.option("--icloud-pass", envvar="ICLOUD_PASS", required=True)
@click.option("--icloud-calendar", envvar="ICLOUD_CALENDAR", required=True)
@click.option("--ical-url", envvar="ICAL_URL", required=True)
@click.option("--poll-interval", envvar="ICAL_POLL_INTERVAL", default=60, type=int, required=True)
def main(icloud_user: str, icloud_pass: str, ical_url: str, icloud_calendar: str, poll_interval: int):

    while True:
        apple_cal = icloud.get_icloud_calendar(icloud_user, icloud_pass, icloud_calendar)
        ical_cal = ical.get_ical_subscription(ical_url)

        if apple_cal is None or ical_cal is None:
            logger.error("Failed to get calendars")
        else:
            sync.prune_deleted_events(apple_cal, ical_cal, ical_url)
            sync.sync_calendar_events(apple_cal, ical_cal, ical_url)

        time.sleep(poll_interval)

if __name__ == "__main__":
    main()
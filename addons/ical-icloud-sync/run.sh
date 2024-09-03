#!/usr/bin/env bash

# Read config options
ICLOUD_USERNAME=$(bashio::config 'icloud_username')
ICLOUD_PASSWORD=$(bashio::config 'icloud_password')
ICLOUD_CALENDAR=$(bashio::config 'icloud_calendar')
ICAL_URL=$(bashio::config 'ical_url')
SYNC_INTERVAL=$(bashio::config 'sync_interval')

# Run the container with the provided configuration
docker run -e ICLOUD_USERNAME=$ICLOUD_USERNAME \
           -e ICLOUD_PASSWORD=$ICLOUD_PASSWORD \
           -e ICLOUD_CALENDAR=$ICLOUD_CALENDAR \
           -e ICAL_URL=$ICAL_URL \
           -e SYNC_INTERVAL=$SYNC_INTERVAL \
           mattbsea/ical-icloud-sync

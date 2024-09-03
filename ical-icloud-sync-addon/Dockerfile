ARG BUILD_FROM
FROM BUILD_FROM

ENV ICLOUD_USER="" \
    ICLOUD_PASS="" \
    ICLOUD_CALENDAR="family" \
    ICAL_URL="" \
    ICAL_POLL_INTERVAL=60

RUN \
    # Allow UID and GID setting
    if [ -f /etc/cont-init.d/02-tamper-check ]; then rm /etc/cont-init.d/02-tamper-check; fi \
    && sed -i 's/bash/bashio/g' /etc/cont-init.d/10-adduser \
    && sed -i 's/{PUID:-911}/(bashio::config "PUID")/g' /etc/cont-init.d/10-adduser \
    && sed -i 's/{PGID:-911}/(bashio::config "PGID")/g' /etc/cont-init.d/10-adduser

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

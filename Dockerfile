FROM ghcr.io/linuxserver/baseimage-alpine:3.19

ARG S6_OVERLAY_VERSION=3.2.0.0

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

COPY rootfs/ /

WORKDIR /app

RUN apk add curl python3

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction

COPY . ./

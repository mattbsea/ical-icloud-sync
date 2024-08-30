FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

WORKDIR /app

RUN apk add curl

RUN curl -sSL https://install.python-poetry.org | python -

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction

COPY . ./

CMD ["poetry", "run", "python", "-m", "ical_sync.main"]

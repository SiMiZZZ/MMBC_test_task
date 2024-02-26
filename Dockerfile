FROM python:3

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1

WORKDIR /app


RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg


RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./pyproject.toml /app/

RUN poetry install --no-interaction --no-ansi
ADD . /app

FROM python:3.11-slim-buster

# Instalar dependências essenciais, incluindo python3, pip e curl
RUN apt-get update -y && apt-get install -y \
    build-essential \
    curl \
    gcc \
    python3 \
    python3-pip \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/"

COPY ./poetry.lock /
COPY ./pyproject.toml /


RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry lock --no-update \ 
    && poetry install --no-root

RUN apt-get remove --purge -y curl


COPY ./app /app

WORKDIR /app

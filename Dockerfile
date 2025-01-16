FROM python:3.13.1-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.13.1-slim

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
COPY . .

RUN pip install --no-cache /wheels/* && \ 
    chmod +x ./entrypoint.sh

USER app
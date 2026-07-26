# bbc-laugh production image
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    BB_CHICKEN_ENV=production \
    FLASK_DEBUG=0 \
    BBC_LAUGH_SITE_NAME=bbc-laugh \
    BBC_LAUGH_DOMAIN=bbc-laugh.com \
    PORT=8080

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

EXPOSE 8080

# Platforms like Render inject $PORT; fall back to 8080.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} --workers 2 --threads 4 --timeout 60 bb_chicken.app:app"]

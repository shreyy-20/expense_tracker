# Stage 1: builder
FROM python:3.11-slim AS builder

LABEL maintainer="developer" \
      description="Smart Expense Tracker Backend Builder" \
      version="1.0.0"

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r /requirements.txt

# Stage 2: production
FROM python:3.11-slim

LABEL maintainer="developer" \
      description="Smart Expense Tracker Backend Production" \
      version="1.0.0"

COPY --from=builder /install /usr/local

RUN useradd -m -s /bin/bash appuser

WORKDIR /app
COPY src/ /app/src/
COPY scripts/ /app/scripts/

RUN mkdir -p /app/data && chown -R appuser:appuser /app

EXPOSE 8000
USER appuser

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/v1/health')"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]


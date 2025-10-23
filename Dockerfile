FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates tini && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
ENV SUPERCRONIC_VERSION=v0.2.3
RUN curl -fsSLo /usr/local/bin/supercronic "https://github.com/aptible/supercronic/releases/download/${SUPERCRONIC_VERSION}/supercronic-linux-amd64" && chmod +x /usr/local/bin/supercronic
COPY . /app/
ENV PORT=8789
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -fsS http://127.0.0.1:${PORT}/healthz || exit 1
ENTRYPOINT ["/usr/bin/tini","--"]
CMD ["bash","-c","supercronic /app/crontab & uvicorn app:app --host 0.0.0.0 --port ${PORT}"]

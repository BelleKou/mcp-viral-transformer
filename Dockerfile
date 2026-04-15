FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir mcp fastmcp httpx beautifulsoup4 pydantic

COPY . .

RUN mkdir -p /app/drafts && chmod 777 /app/drafts

ENTRYPOINT ["python", "server.py"]

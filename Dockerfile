FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
COPY requirements.lock .
RUN uv pip install --no-cache --system -r requirements.lock

COPY src src

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/book.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]

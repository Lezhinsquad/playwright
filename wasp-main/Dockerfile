# Base image
FROM python:3.11-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2 \
    libpangocairo-1.0-0 libxshmfence1 libgtk-3-0 ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Playwright and browsers
RUN pip install playwright && playwright install --with-deps

# 도커 빌드 시 전달할 ARG 설정 (기본값 dev)
ARG ENV=dev
ARG ENV_PATH=docker
ARG KAFKA_URL

# 환경변수 컨테이너내에 설정
ENV ENV=${ENV}
ENV KAFKA_MONITORING_URL=${KAFKA_URL}
ENV ENV_PATH=${ENV_PATH}

COPY . .

# Expose port
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

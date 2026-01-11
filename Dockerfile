FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose internal port
EXPOSE 8000

# IMPORTANT: shell form so $PORT expands
CMD uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}

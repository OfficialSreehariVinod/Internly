FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for numpy/sklearn)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Upgrade pip tooling
RUN pip install --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend ./backend
COPY frontend ./frontend

# Expose port (Railway/Fly will map it)
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

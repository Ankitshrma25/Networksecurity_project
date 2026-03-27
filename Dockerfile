FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (faster builds)
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy full project
COPY . .

# IMPORTANT (force include templates)
COPY templates ./templates

CMD ["python3", "app.py"]
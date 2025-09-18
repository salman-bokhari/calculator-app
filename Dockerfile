# Use official lightweight Python image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure Python sees /app as importable root
ENV PYTHONPATH=/app

# Run tests at build
RUN pytest -v

CMD ["python", "main.py"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest for container testing
RUN pip install pytest

COPY . .

# Ensure Python can find local packages
ENV PYTHONPATH=/app

CMD ["python", "main.py"]

# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run tests when building (to fail early if broken)
RUN pytest -v

# Default command runs the calculator demo
CMD ["python", "main.py"]

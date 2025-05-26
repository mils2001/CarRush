# Use an appropriate base image
FROM python:3.10-slim

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code (you had a typo here)
COPY . .

# Expose Flask default port
EXPOSE 5000

# Command to run your application
CMD ["python", "app.py"]


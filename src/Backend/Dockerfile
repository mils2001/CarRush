FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt



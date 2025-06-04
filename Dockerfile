# Use official Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY app.py .

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port your app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run"]

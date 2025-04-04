# Use the official Python 3.8 slim image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files and directories into the container
COPY app.py requirements.txt ./

# Install dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 8000

# Run the Flask application
CMD ["python", "app.py"]
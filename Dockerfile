# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files
# and to ensure output is sent directly to the terminal without buffering.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
# (This ensures dependencies aren't re-installed unless requirements.txt changes)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on (Change 5000 to your app's port if needed)
EXPOSE 5000

# The command to run the application
# Replace 'main.py' with your specific entry point (e.g., app.py, manage.py)
CMD ["python", "main.py"]
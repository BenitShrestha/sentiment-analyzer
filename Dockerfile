# Use an official Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt .

# Install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY . .

# Expose the port FastAPI will run on 
EXPOSE 8000

# Define default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
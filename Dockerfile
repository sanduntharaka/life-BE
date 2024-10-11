# Use an official Python runtime as a parent image
FROM python:3.10-slim
ENV PYTHONPATH=/app
# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for database URL
ENV DATABASE_URL="postgresql+psycopg2://user:password@db:5432/dbname"

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

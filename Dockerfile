# Use the official Python image from Docker Hub
FROM python:3.10


# Set the working directory to /app inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install dependencies before copying the entire project (to optimize caching)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Run the Django development server (switch to Gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

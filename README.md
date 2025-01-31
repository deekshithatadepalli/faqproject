# FAQ Management System
A multilingual FAQ management system built using Django, with features including WYSIWYG editor support, REST API, translation caching, and Docker deployment.

## Table of Contents:
1. Installation
2. API Usage
3. Contributing
4. Version Control
5. Deployment & Docker Support

## Installation
Follow these steps to set up the project locally:

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Redis (for caching support, optional if not using Redis, but included in Docker setup)

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/deekshithatadepalli/faqproject.git

Navigate to the project directory:
cd faqproject

Set up a virtual environment:
python -m venv venv

Activate the virtual environment:
For Windows:
venv\Scripts\activate

For Mac/Linux:
source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Create a superuser to access the admin panel:
python manage.py createsuperuser


Run the development server:
python manage.py runserver
application should now be accessible at http://localhost:8000


API Usage
The API provides multilingual support for FAQs. Use the lang query parameter to retrieve the FAQ questions in the desired language.

Example Endpoints:
Get FAQs in English (default):
curl http://localhost:8000/api/faqs/

Get FAQs in Hindi:
curl http://localhost:8000/api/faqs/?lang=hi


Get FAQs in Bengali:
curl http://localhost:8000/api/faqs/?lang=bn

Contributing
We welcome contributions to improve the project! Here's how you can contribute:

Fork the repository:
Create a personal copy of the project by forking it on GitHub.

Create a new branch for your changes:
It is always good practice to work on a new branch rather than directly on main.
Contributing
We welcome contributions to improve the project! Here's how you can contribute:

Fork the repository:
Create a personal copy of the project by forking it on GitHub.

Create a new branch for your changes:
It is always good practice to work on a new branch rather than directly on main.
Create a Pull Request:
After pushing your branch to your fork, open a pull request to the main repository.


Version Control
This project uses Git for version control. To make collaboration easier, we follow conventional commits to ensure clean commit history. Here's a quick guide:

feat: Adding a new feature.
Example: feat: Add multilingual FAQ model support.

fix: Fixing a bug.
Example: fix: Corrected translation caching issue.

docs: Updating documentation.
Example: docs: Update README with API usage examples.


Git Workflow:
Commit Changes Atomically:
Each commit should have a single purpose, whether adding a new feature or fixing a bug.

Write Descriptive Commit Messages:
The commit message should describe what was done and why, using the format type: description.

Push and Create Pull Requests:
Once your changes are committed, push them to your branch and create a pull request to the main branch.

Deployment & Docker Support
## Deployment & Docker Support

### Docker Setup
To run the application in a Docker container, follow the steps below. Docker allows you to containerize the application and run it consistently across different environments.

1. **Create a Dockerfile**  
   In the root directory of your project, create a `Dockerfile` with the following content:

   ```Dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.9-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app/

   # Install dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Expose port 8000 for the Django server
   EXPOSE 8000

   # Set environment variables for Django
   ENV PYTHONUNBUFFERED 1

   # Run migrations and start the server
   CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

Create a docker-compose.yml File
In the root directory, create a docker-compose.yml file to define the services and link your database with the application.

version: '3'

services:
  db:
    image: redis:alpine
    container_name: redis
    ports:
      - "6379:6379"
    networks:
      - backend

  web:
    build: .
    container_name: faqproject_web
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - backend

networks:
  backend:

Build and Run with Docker
To build and run your application inside Docker containers:

Open a terminal and navigate to your project directory.

Run the following command to build the Docker containers:
docker-compose build


Once the build completes, start the containers with:
docker-compose up

Access the Application
After starting the containers, you can access your application at http://localhost:8000.

Deployment on Heroku
To deploy the application to Heroku, follow these steps:

Install Heroku CLI
If you don’t have the Heroku CLI installed, download and install it from Heroku's website.

Create a Heroku App

Log in to your Heroku account by running:
heroku login
Create a new Heroku app:
heroku create faqproject-app
Add Heroku Postgres (Optional)
If you're using PostgreSQL, you can add the Heroku Postgres database:
heroku addons:create heroku-postgresql:hobby-dev


Deploy the Application to Heroku

Push the code to Heroku:
bash
Copy
Edit

git push heroku main


Access the App on Heroku
After the deployment is successful, you can access your application using the Heroku URL:
heroku open


Deployment on AWS 
For deploying the application on AWS, you can use services like Elastic Beanstalk or EC2.

Set Up an EC2 Instance

Launch an EC2 instance with a suitable Linux distribution.
SSH into the instance and install Docker.
Push Your Docker Container to AWS

Build and push your Docker image to Amazon ECR (Elastic Container Registry).
Follow the AWS ECR documentation to push your Docker image to ECR.
Run the Application on EC2

SSH into your EC2 instance and pull the Docker image.
Run the container on EC2 using Docker.




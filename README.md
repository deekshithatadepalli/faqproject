# FAQ Management System
A multilingual FAQ management system built using Django, with features including WYSIWYG editor support, REST API, translation caching, and Docker deployment.

## Table of Contents
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Contributing](#contributing)
4. [Version Control](#version-control)
5. [Deployment & Docker Support](#deployment--docker-support)

---

## Installation
Follow these steps to set up the project locally:

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Redis (for caching support, optional if not using Redis, but included in Docker setup)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/deekshithatadepalli/faqproject.git
   ```

2. Navigate to the project directory:
   ```bash
   cd faqproject
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - **For Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **For Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```
   The application should now be accessible at [http://localhost:8000](http://localhost:8000)

---

## API Usage
The API provides multilingual support for FAQs. Use the `lang` query parameter to retrieve FAQ questions in the desired language.

### Example Endpoints
- **Get FAQs in English (default):**
  ```bash
  curl http://localhost:8000/api/faqs/
  ```
- **Get FAQs in Hindi:**
  ```bash
  curl http://localhost:8000/api/faqs/?lang=hi
  ```
- **Get FAQs in Bengali:**
  ```bash
  curl http://localhost:8000/api/faqs/?lang=bn
  ```

---

## Contributing
We welcome contributions to improve the project! Here's how you can contribute:

### Steps
1. **Fork the repository:**
   - Create a personal copy of the project by forking it on GitHub.

2. **Create a new branch:**
   - It is always good practice to work on a new branch rather than directly on `main`.
   ```bash
   git checkout -b feature-branch
   ```

3. **Make changes and commit:**
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

4. **Push to your fork and create a pull request:**
   ```bash
   git push origin feature-branch
   ```
   - Open a pull request to the main repository.

---

## Version Control
This project uses Git for version control. To make collaboration easier, we follow conventional commits to ensure a clean commit history.

### Commit Message Guidelines
- `feat:` Adding a new feature.
  - Example: `feat: Add multilingual FAQ model support`
- `fix:` Fixing a bug.
  - Example: `fix: Corrected translation caching issue`
- `docs:` Updating documentation.
  - Example: `docs: Update README with API usage examples`

### Git Workflow
- **Commit Changes Atomically:** Each commit should have a single purpose.
- **Write Descriptive Commit Messages:** Follow the `type: description` format.
- **Push and Create Pull Requests:** Once your changes are committed, push them and create a PR.

---

## Deployment & Docker Support

### Docker Setup
To run the application in a Docker container, follow these steps.

#### 1. Create a `Dockerfile`
```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django server
EXPOSE 8000

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1

# Run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
```

#### 2. Create a `docker-compose.yml` File
```yaml
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
```

#### 3. Build and Run with Docker
```bash
docker-compose build
docker-compose up
```
Access the application at [http://localhost:8000](http://localhost:8000).

---

## Deployment on Heroku

### Steps
1. **Install Heroku CLI**: [Download Here](https://devcenter.heroku.com/articles/heroku-cli)
2. **Login to Heroku:**
   ```bash
   heroku login
   ```
3. **Create a new Heroku app:**
   ```bash
   heroku create faqproject-app
   ```
4. **(Optional) Add Heroku PostgreSQL:**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```
5. **Deploy the application:**
   ```bash
   git push heroku main
   ```
6. **Open the app:**
   ```bash
   heroku open
   ```

---

## Deployment on AWS

### Steps
1. **Set Up an EC2 Instance**
   - Launch an EC2 instance with a Linux distribution.
   - SSH into the instance and install Docker.
2. **Push Docker Container to AWS ECR**
   - Build and push the Docker image to Amazon ECR.
   - Follow [AWS ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html).
3. **Run the Application on EC2**
   - SSH into EC2, pull the Docker image, and run the container.

---


# FAQ Management System

A multilingual FAQ management system built using Django, featuring WYSIWYG editor support, REST API, translation caching, and Docker deployment.

## Table of Contents
- [Installation](#installation)
- [API Usage](#api-usage)
- [Contributing](#contributing)
- [Version Control](#version-control)
- [Deployment & Docker Support](#deployment--docker-support)

## Installation

### Prerequisites
- Python 3.x
- pip
- Redis (for caching, optional)

### Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/deekshithatadepalli/faqproject.git
    cd faqproject
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # For Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations and start the server:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. Access the application at [http://localhost:8000](http://localhost:8000).

## API Usage

Retrieve FAQs in different languages using the `lang` query parameter.

- **English (default):**

    ```bash
    curl http://localhost:8000/api/faqs/
    ```

- **Hindi:**

    ```bash
    curl http://localhost:8000/api/faqs/?lang=hi
    ```

- **Bengali:**

    ```bash
    curl http://localhost:8000/api/faqs/?lang=bn
    ```

## Contributing

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request.

## Version Control

We follow conventional commits for version control. Commit messages should be:

- `feat:` for new features.
- `fix:` for bug fixes.
- `docs:` for documentation updates.

## Deployment & Docker Support

### Docker Setup

1. Create a `Dockerfile`:

    ```Dockerfile
    FROM python:3.9-slim
    WORKDIR /app
    COPY . /app/
    RUN pip install --no-cache-dir -r requirements.txt
    EXPOSE 8000
    CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
    ```

2. Create a `docker-compose.yml` file:

    ```yaml
    version: '3'
    services:
      db:
        image: redis:alpine
      web:
        build: .
        ports:
          - "8000:8000"
        depends_on:
          - db
    ```

3. Run Docker:

    ```bash
    docker-compose build
    docker-compose up
    ```

### Deployment on Heroku

1. Log in to Heroku:

    ```bash
    heroku login
    ```

2. Create the app and deploy:

    ```bash
    heroku create faqproject-app
    git push heroku main
    ```

### Deployment on AWS

1. Set up an EC2 instance and SSH into it.
2. Build and push Docker image to Amazon ECR.
3. Pull and run Docker container on EC2.


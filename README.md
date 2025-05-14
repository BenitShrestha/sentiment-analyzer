# Sentiment Analyzer API

A simple and effective sentiment analyzer API built with FastAPI and VADER. It evaluates the sentiment (positive, negative or neutral) of a given piece of text.

---

## Features
- Sentiment analysis using VADER
- RESTful API endpoints
- Dockerized Application
- Pytest-based testing
- GitHub Actions CI pipline
- Pre-commit hooks
    - `Flake8` Linting 
    - `Black` Auto-formatting 
    - `isort` Sorting imports

---

## Getting Started 

### Prerequisites 

- Python 3.12+
- Docker for containerized usage

---

### Running the app locally

1. Clone the repo:
```bash
git clone https://github.com/BenitShrestha/sentiment-analyzer.git
cd sentiment-analyzer

pip install -r requirements.txt

uvicorn app.main:app --reload
```
## API Documentation
After starting the app, you can access the interactive API documentation:

- UI: http://127.0.0.1:8000/docs

## Running Tests
```bash
pytest
```

## Using Docker
```bash
docker build -t sentiment-analyzer:latest . 

docker run -p 8000:8000 sentiment-analyzer
```

## Pre Commit Hooks
```bash
pre-commit install

pre-commit run --all-files
```

# Running docker image on any device
```bash
docker pull benitshrestha/sentiment-analyzer:latest

docker run -d -p 8000:8000 benitshrestha/sentiment-analyzer:latest
# The command above outputs the Container ID [CID]

docker logs CID
# Execute this, then follow the link generated to check the FastAPI interface
```

## Project Structure 

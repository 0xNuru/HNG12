# HNG12 Backend stage-0

## Description

This is a simple FastAPI application that returns a JSON object with:

- email
- current_datetime
- github_url

## clone the repo

```bash
git clone https://github.com/0xnuru/hng12.git
```

## Requirements

find the requirements in [requirements.txt](https://github.com/0xnuru/hng12/stage-0/requirements.txt)

## Install the dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn main:app --reload
```

## API Documentation

### Endpoint

- Base URL: `http://localhost:8000`
- Endpoint: `/stage-0` (GET)

### Request/Response Format

**Response Format:**

```json
{
  "email": "string",
  "current_datetime": "string",
  "github_url": "string"
}
```

### Example Usage

```bash
# Using curl
curl http://localhost:8000/stage-0

# Using httpie
http GET http://localhost:8000/stage-0
```

### Related Resources

- [HNG Python Developers](https://hng.tech/hire/python-developers)

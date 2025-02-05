# HNG12 Backend stage-1

## Task Description

Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## clone the repo

```bash
git clone https://github.com/0xnuru/hng12.git
```

## Requirements

find the requirements in [requirements.txt](https://github.com/0xnuru/hng12/stage-1/requirements.txt)

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

- Base URL: `https://hng12-crp8.onrender.com`
- Endpoint: `/stage-0` (GET)

### Request/Response Format

**Number Properties Response Format (200 OK):**

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Error Response Format (400 Bad Request):**

```json
{
  "number": "alphabet",
  "error": true
}
```

### Example Usage

```bash
# Using curl
curl https://hng12-crp8.onrender.com/number/371

# Using httpie
http GET https://hng12-crp8.onrender.com/number/371
```

### Related Resources

- [HNG Python Developers](https://hng.tech/hire/python-developers)

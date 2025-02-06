import requests
import random
from fastapi import FastAPI, status, Response
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/classify-number")
async def classify_number(number: str = None, response: Response = None):
    if number is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"number": "missing", "error": True}

    try:
        num = int(number)
    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"number": number, "error": True}

    categories = ["trivia", "math", "date", "year"]
    category = random.choice(categories)

    fun_fact = requests.get(f"http://numbersapi.com/{num}/{category}")

    properties = [even_odd(num)]
    if armstrong(num):
        properties.insert(0, "armstrong")

    return {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum(num),
        "fun_fact": f"{fun_fact.text} //gotten from the numbers API",
    }


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_perfect(n):
    if n <= 1:
        return False

    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


def even_odd(n):
    return "even" if n % 2 == 0 else "odd"


def armstrong(n):
    num_digits = len(str(n))
    return sum(int(digit) ** num_digits for digit in str(n)) == n


def digit_sum(n):
    return sum(int(digit) for digit in str(n))

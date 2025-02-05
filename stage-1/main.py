import requests
import random
from fastapi import FastAPI, status
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


@app.get("/api/classify-number", status_code=status.HTTP_200_OK)
async def classify_number(number: str = None):
    if number is None:
        return {"number": "missing", "error": True}, status.HTTP_400_BAD_REQUEST

    try:
        num = int(number)
    except ValueError:
        return {"number": number, "error": True}, status.HTTP_400_BAD_REQUEST

    categories = ["trivia", "math", "date", "year"]
    category = random.choice(categories)

    fun_fact = requests.get(f"http://numbersapi.com/{num}/{category}")

    properties = [even_odd(num)]
    if armstrong(num):
        properties.append("armstrong")

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
    return sum(int(digit) ** 3 for digit in str(n)) == n


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    uvicorn.run(app, reload=True, host="0.0.0.0", port=8000)

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome Message": "Hello World"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """add two numbers together"""

    total = num1 + num2
    return {"total is": total}


@app.get("/multiply/{num1}/{num2}")
async def multiply(num1: int, num2: int):
    """add two numbers together"""

    total = num1 * num2
    return {"product is": total}

@app.get("/minus/{num1}/{num2}")
async def minus(num1: int, num2: int):
    """num1 minus num2"""

    diff = num1 - num2
    return {"difference is": diff}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

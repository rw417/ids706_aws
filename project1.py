from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome Message": "Hello World 1:47pm 9/1/21"}


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


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

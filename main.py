from fastapi import FastAPI
import uvicorn

app = FastAPI(debug=True)

@app.get("/add")
def add(number1: int, number2: int):
    return {number1 + number2}

@app.get("/subtract")
def add(number1: int, number2: int):
    return {number1 - number2}

@app.get("/multiply")
def add(number1: int, number2: int):
    return {number1 * number2}

@app.get("/divide")
def add(number1: int, number2: int):
    if number1 or number2 == 0:
        return {"error": "Ділення на нуль не можливе"}
    return {number1 / number2}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)


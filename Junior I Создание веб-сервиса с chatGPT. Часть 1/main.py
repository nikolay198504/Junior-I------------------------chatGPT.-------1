from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ClassCalc(BaseModel):
    a: float
    b: float

# Обработчик для сложения
@app.post('/plus')
def post_plus(data: ClassCalc):
    result = data.a + data.b
    return {'result': result}

# Обработчик для вычитания
@app.post('/minus')
def post_minus(data: ClassCalc):
    result = data.a - data.b
    return {'result': result}

# Обработчик для умножения
@app.post('/multiply')
def post_multiply(data: ClassCalc):
    result = data.a * data.b
    return {'result': result}

# Обработчик для деления
@app.post('/divide')
def post_divide(data: ClassCalc):
    if data.b == 0:  # Проверка деления на ноль
        return {'error': 'Division by zero is not allowed'}
    result = data.a / data.b
    return {'result': result}


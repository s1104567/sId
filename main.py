from typing import Optional

from fastapi import FastAPI

app = FastAPI()  # 建立一个 FastAPI application

@app.get("/")  # 指定 API 路径 (GET 方法)
def hello_world():
    return {"Hello": "World"}

@app.get("/bmi/{student_id}/{name}")  # 指定 API 路径 (GET 方法)
def get_bmi(student_id: int, name: str, height: float, weight: float):
    bmi = weight / (height * height)
    return {"Student ID": student_id, "Name": name, "BMI": bmi}
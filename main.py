from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
class student(BaseModel):
    name:str
    age:int
    email:str
    Roll_number:str
    department:str
class studentResponse(BaseModel):
    id:int
    name:str
    age:int
    email:str
    Roll_number:str
    department:str

@app.get("/")
def read_root():
    return{"hello":"world"}

def create_student(student:student):
    return student

def read_student(id:int):
    return studentResponse(id=id,**student.dict())
def update_student(id:int,student:student):

    return studentResponse(id=id,**student.dict())

def delete_student(id:int):
    return studentResponse(id=id,**student.dict())


@app.post("/student")
def create_student(student:student):
    return create_student(student)

@app.get("/student/{id}")
def read_student(id:int):
    return read_student(id)

@app.put("/student/{id}")
def update_student(id:int,student:student):
    return update_student(id,student)

@app.delete("/student/{id}")
def delete_student(id:int):
    return delete_student(id)

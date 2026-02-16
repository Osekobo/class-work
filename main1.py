from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}


students = {
    1: {"name": "John", "age": 17, "year": "Year 12"},
    2: {"name": "Amina", "age": 19, "year": "Year 11"},
    3: {"name": "Peter", "age": 18, "year": "Year 10"},
}

# pip install -r .\requirements.txt
class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/get_student/{student_id}")
def get_student(student_id: int = Path(..., description="Enter the ID of the student", gt=0, lt=3)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.get("/get_by_name/{student_id}")
def get_student_by_name(*, student_id: int, name: Optional[str] = None, age: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create_student/{student_id}")
def create_students(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]


@app.put("/update_student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]


@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}

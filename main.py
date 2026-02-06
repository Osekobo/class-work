from fastapi import FastAPI, Path, HTTPException
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}


students = {
    1: {"name": "John", "age": 17, "class": "Year 12"},
    2: {"name": "Amina", "age": 19, "class": "Year 11"},
}


@app.get("/get_student/{student_id}")
def get_student(student_id: int = Path(..., description="Enter the ID of the student", gt=0, lt=3)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.get("/get_by_name")
def get_student(*, name: Optional[str] = None, age: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}
# query parameter

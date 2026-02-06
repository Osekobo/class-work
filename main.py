from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}


students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "Year 12"
    }
}


@app.get("/get_student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

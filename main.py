from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#student model
class Student(BaseModel):
    id : int
    name : str
    age : int
    
#inital data (3 studnets)
students = [
    Student(id="1", name="Atharva", age=20),
    Student(id="2", name="Aryan", age=22),
    Student(id="3", name="Sarthak", age=19)
]

#Get all students
@app.get("/students")
def get_students():
    return students

#Get student by id
@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

#Add new student
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully",
            "student": update_student}

#updated student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message": "Student updated successfully",
                    "student": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

#Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

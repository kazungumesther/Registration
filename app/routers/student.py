from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.student import StudentCreate, StudentResponse
import app.repositories.student as repo

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", status_code=201)
def create_student(student: StudentCreate):
   try:
       repo.add_student(student.name, student.age, student.email, student.country, student.idnumber)
       return {"message": "Student created successfully"}
   except Exception as e:
       raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[StudentResponse])
def read_all_students():
   return repo.get_all_students()


@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int):
   student = repo.get_student_by_id(student_id)
   if not student:
       raise HTTPException(status_code=404, detail="Student not found")
   return student


@router.put("/{student_id}")
def update_student(student_id: int, student: StudentCreate):
   if not repo.get_student_by_id(student_id):
       raise HTTPException(status_code=404, detail="Student not found")
   repo.update_student(student_id, student.name, student.age, student.email, student.country, student.idnumber)
   return {"message": "Student updated successfully"}


@router.delete("/{student_id}")
def delete_student(student_id: int):
   if not repo.get_student_by_id(student_id):
       raise HTTPException(status_code=404, detail="Student not found")
   repo.delete_student(student_id)
   return {"message": "Student deleted successfully"}



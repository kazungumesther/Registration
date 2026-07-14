from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.teacher import TeacherCreate, TeacherResponse
import app.repositories.teacher as repo


router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.post("/", status_code=201)
def create_teacher(teacher: TeacherCreate):
   try:
       repo.add_teacher(teacher.name, teacher.email, teacher.department, teacher.phone, teacher.employee_number)
       return {"message": "Teacher created successfully"}
   except Exception as e:
       raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[TeacherResponse])
def read_all_teachers():
   return repo.get_all_teachers()


@router.get("/{teacher_id}", response_model=TeacherResponse)
def read_teacher(teacher_id: int):
   teacher = repo.get_teacher_by_id(teacher_id)
   if not teacher:
       raise HTTPException(status_code=404, detail="Teacher not found")
   return teacher


@router.put("/{teacher_id}")
def update_teacher(teacher_id: int, teacher: TeacherCreate):
   if not repo.get_teacher_by_id(teacher_id):
       raise HTTPException(status_code=404, detail="Teacher not found")
   repo.update_teacher(teacher_id, teacher.name, teacher.email, teacher.department, teacher.phone, teacher.employee_number)
   return {"message": "Teacher updated successfully"}


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int):
   if not repo.get_teacher_by_id(teacher_id):
       raise HTTPException(status_code=404, detail="Teacher not found")
   repo.delete_teacher(teacher_id)
   return {"message": "Teacher deleted successfully"}





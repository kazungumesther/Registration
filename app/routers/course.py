rom fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.course import CourseCreate, CourseResponse
import app.repositories.course as repo


router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/", status_code=201)
def create_course(course: CourseCreate):
   try:
       repo.add_course(course.title, course.code, course.credits, course.semester, course.teacher_id)
       return {"message": "Course created successfully"}
   except Exception as e:
       raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[CourseResponse])
def read_all_courses():
   return repo.get_all_courses()


@router.get("/{course_id}", response_model=CourseResponse)
def read_course(course_id: int):
   course = repo.get_course_by_id(course_id)
   if not course:
       raise HTTPException(status_code=404, detail="Course not found")
   return course


@router.put("/{course_id}")
def update_course(course_id: int, course: CourseCreate):
   if not repo.get_course_by_id(course_id):
       raise HTTPException(status_code=404, detail="Course not found")
   repo.update_course(course_id, course.title, course.code, course.credits, course.semester, course.teacher_id)
   return {"message": "Course updated successfully"}


@router.delete("/{course_id}")
def delete_course(course_id: int):
   if not repo.get_course_by_id(course_id):
       raise HTTPException(status_code=404, detail="Course not found")
   repo.delete_course(course_id)
   return {"message": "Course deleted successfully"}

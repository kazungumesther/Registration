from fastapi import FastAPI
from app.routers import student, teacher, course
from app.models.course import create_table as create_course_table
from app.models.student import create_table as create_student_table
from app.models.teacher import create_table as create_teacher_table

app = FastAPI()

@app.on_event("startup")
def startup_event():
   create_student_table()
   create_teacher_table()
   create_course_table()

app.include_router(student.router)
app.include_router(teacher.router)
app.include_router(course.router)


























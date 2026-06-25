

from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table,add_student,get_students

app=FastAPI()
create_table()

@app.get("/students{id}")
def student_detail(id:int):
    student = get_student(id)
    return student
    
def list_students():
    students=get_students()
    return Students

class Student(BaseModel):
    name:str
    department:str
    email:str
    country:str
    id_number:int

@app.post("/students")
def register_student(student:Student):
    add_student(student.name, student.age, student.country, student.id_number, student.email)
    return {"message":"student registered", "student":Student}

@app.put("/students/{id}")
def update_student(student:Student):
    add_student(student.name, student.age, student.country, student.id_number, student.email)
    return {"message":"student registered", "student":Student}

@app.delete("/students/{id}")
def delete_student(student:Student):
    add_student(student.name, student.age, student.country, student.id_number, student.email)
    return {"message":"student registered", "student":Student}




@app.get("/teachers{id}")
def teacher_detail(id:int):
    teacher = get_teacher(id)
    return teacher
    
def list_teachers():
    teachers=get_teachers()
    return Teachers

class Teacher(BaseModel):
    name:str
    department:str
    email:str
    country:str
    id_number:int

@app.post("/teachers")
def register_teacher(teacher:Teacher):
    add_teacher(teacher.name, teacher.department, teacher.country, teacher.id_number, teacher.email)
    return {"message":"teacher registered", "teacher":Teacher}

@app.put("/teachers/{id}")
def update_teacher(teacher:Teacher):
    add_teacher(teacher.name, teacher.department, teacher.country, teacher.id_number, teacher.email)
    return {"message":"teacher registered", "teacher":Teacher}

@app.delete("/teachers/{id}")
def delete_teacher(teacher:Teacher):
    add_teacher(teacher.name, teacher.department, teacher.country, teacher.id_number, teacher.email)
    return {"message":"teacher registered", "teacher":Teacher}




@app.get("/course{id}")
def course_detail(id:int):
    course = get_course(id)
    return course
    
def list_couses():
    courses=get_couses()
    return Courses

class Course(BaseModel):
    title:str
    department:str
    credits:str
    code:str
    id:int

@app.post("/courses")
def register_course(course:Course):
    add_course(course.title, course.department, course.credits, course.code, course.id)
    return {"message":"course registered", "course":Course}


@app.put("/courses/{id}")
def update_course(course:Course):
    add_course(course.title, course.department, course.credits, course.code, course.id)
    return {"message":"course registered", "course":Course}


@app.delete("/courses/{id}")
def delete_course(course:Course):
    add_course(course.title, course.department, course.credits, course.code, course.id)
    return {"message":"course registered", "course":Course}
























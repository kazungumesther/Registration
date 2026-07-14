from typing import List
import app.repositories.course as repo
from app.schemas.course import CourseCreate

def create_course(course_data: CourseCreate) -> None:
    repo.add_course(
        title= course_data.title,
        code = course_data.code,
        semester = course_data.semester,
        credits = course_data.credits,
        teacher_id = course_data.teacher_id
    )

def get_courses() -> List[dict]:
    return repo.get_all_courses()

def get_course(course_id: int) -> dict:
    return repo.get_course_by_id(course_id)

def update_course(course_id: int, course_data: CourseCreate) -> None:
    repo.update_course(
        course_id = course_id,
        title = course_data.name,
        code = course_data.code,
        credits = course_data.credits,
        semester = course_data.semester,
        teacher_id = course_data.teacher_id
    )

def remove_course(course_id: int) -> None:
    repo.delete_course(course_id)

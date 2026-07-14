

from typing import List
import app.repositories.student as repo
from app.schemas.student import StudentCreate

def create_student(student_data: StudentCreate) -> None:
    repo.add_student(
        name = student_data.name,
        age = student_data.age,
        email = student_data.email,
        country = student_data.id_number
    )

    def get_students() -> List[dict]:
        return repo.get_all_students()

    def get_student(student_id: int) -> dict:
        return repo.get_student_by_id(student_id)

    def update_student(student_id: int, student_data: StudentCreate) -> None:
        repo.update_student(
            student_id = student_id,
            name = student_data.name,
            age = student_data.age,
            email = student_data.email,
            country = student_data.country,
            idnumber = student_data.idnumber
        )

    def remove_student(student_id: int) -> None:
        repo.delete_student(student_id)
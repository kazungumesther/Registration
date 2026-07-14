from typing import List
import app.repositories.teacher as repo
from app.schemas.teacher import TeacherCreate

def create_teacher(teacher_data: TeacherCreate) -> None:
    repo.add_teacher(
        name = teacher_data.name,
        age = teacher_data.age,
        email = teacher_data.email,
        country = teacher_data.id_number
    )

    def get_teachers() -> List[dict]:
        return repo.get_all_teachers()

    def get_teacher(teacher_id: int) -> dict:
        return repo.get_teacher_by_id(teacher_id)

    def update_teacher(teacher_id: int, teacher_data: TeacherCreate) -> None:
        repo.update_teacher(
            teacher_id = teacher_id,
            name = teacher_data.name,
            age = teacher_data.age,
            email = teacher_data.email,
            country = teacher_data.country,
            idnumber = teacher_data.idnumber
        )

    def remove_teacher(teacher_id: int) -> None:
        repo.delete_teacher(teacher_id)
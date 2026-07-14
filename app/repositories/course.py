from app.database import get_connection

def add_course(title: str, code: str, credits: int, semester: str, teacher_id: int):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO courses (title, code, credits, semester, teacher_id) VALUES (?, ?, ?, ?, ?)",
            (title, code, credits, semester, teacher_id),
        )

def get_all_courses():
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM courses")
        return [dict(row) for row in cursor.fetchall()]

def get_course_by_code(code: str):
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM courses WHERE code = ?", (code,))
        row = cursor.fetchone()
        return dict(row) if row else None

def get_course_by_id(course_id: int):
    with get_connection() as connection:
        cursor = connection.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

def update_course(course_id: int, title: str, code: str, credits: int, semester: str, teacher_id: int):
    with get_connection() as connection:
        connection.execute(
            "UPDATE courses SET title = ?, code = ?, credits = ?, semester = ?, teacher_id = ? WHERE id = ?",
            (title, code, credits, semester, teacher_id, course_id),
        )

def delete_course(course_id: int):
    with get_connection() as connection:
        connection.execute("DELETE FROM courses WHERE id = ?", (course_id,))

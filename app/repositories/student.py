from app.database import get_connection

def add_student(name: str, age: int, email: str, country: str, idnumber: int):
   with get_connection() as conn:
       conn.execute(
           "INSERT INTO students (name, age, email, country, idnumber) VALUES (?, ?, ?, ?, ?)",
           (name, age, email, country, idnumber),
       )


def get_all_students():
   with get_connection() as conn:
       cursor = conn.execute("SELECT * FROM students")
       return [dict(row) for row in cursor.fetchall()]


def get_student_by_id(student_id: int):
   with get_connection() as conn:
       cursor = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,))
       row = cursor.fetchone()
       return dict(row) if row else None


def update_student(student_id: int, name: str, age: int, email: str, country: str, idnumber: int):
   with get_connection() as conn:
       conn.execute(
           "UPDATE students SET name=?, age=?, email=?, country=?, idnumber=? WHERE id=?",
           (name, age, email, country, idnumber, student_id),
       )


def delete_student(student_id: int):
   with get_connection() as conn:
       conn.execute("DELETE FROM students WHERE id = ?", (student_id,))



from app.database import get_connection

def add_teacher(name: str, email: str, department: str, phone: str, employee_number: int):
   with get_connection() as conn:
       conn.execute(
           "INSERT INTO teachers (name, email, department, phone, employee_number) VALUES (?, ?, ?, ?, ?)",
           (name, email, department, phone, employee_number),
       )


def get_all_teachers():
   with get_connection() as conn:
       cursor = conn.execute("SELECT * FROM teachers")
       return [dict(row) for row in cursor.fetchall()]

def get_teacher_by_id(teacher_id: int):
   with get_connection() as conn:
       cursor = conn.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
       row = cursor.fetchone()
       return dict(row) if row else None

def update_teacher(teacher_id: int, name: str, email: str, department: str, phone: str, employee_number: int):
   with get_connection() as conn:
       conn.execute(
           "UPDATE teachers SET name=?, email=?, department=?, phone=?, employee_number=? WHERE id=?",
           (name, email, department, phone, employee_number, teacher_id),
       )

def delete_teacher(teacher_id: int):
   with get_connection() as conn:
       conn.execute("DELETE FROM teachers WHERE id = ?", (teacher_id,))


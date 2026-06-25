import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager

def get_connection():
    connection= sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
        connection.execute(''' CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL,
        country TEXT NOT NULL,
        id_number INTEGER NOT NULL
        )''')

def add_student(name,age,email,country,id_number):
    with get_connection() as connection:
        connection.execute(
        'INSERT INTO students(name,age,email,country,id_number) VALUES(?,?,?,?,?)',
        (name, age, email,country,id_number),
        )

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT* FROM students').fetchall()

def get_student(student_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students WHERE id=?', (student_id,)).fetchone()




def create_table():
    with get_connection() as connection:
        connection.execute(''' CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        email TEXT NOT NULL,
        country TEXT NOT NULL,
        id_number INTEGER NOT NULL
        )''')

def add_teacher(name,department,email,country,id_number):
    with get_connection() as connection:
        connection.execute(
        'INSERT INTO teachers(name,department,email,country,id_number) VALUES(?,?,?,?,?)',
        (name, department, email,country,id_number),
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT* FROM teachers').fetchall()

def get_teacher(student_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers WHERE id=?', (teacher_id,)).fetchone()
        



def create_table():
    with get_connection() as connection:
        connection.execute(''' CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        department TEXT NOT NULL,
        credits TEXT NOT NULL,
        code TEXT NOT NULL
        )''')

def add_course(title,department,credits,code,id):
    with get_connection() as connection:
        connection.execute(
        'INSERT INTO courses(title,department,credits,code,id) VALUES(?,?,?,?,?)',
        (title, department, credits,code,id),
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def get_teacher(student_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses WHERE id=?', (course_id,)).fetchone()



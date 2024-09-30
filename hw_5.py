import sqlite3

conn = sqlite3.connect('School.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               full_name TEXT NOT NULL,
               age INTEGER,
               grade TEXT NOT NULL,
               enrollment_date DATE DEFAULT CURRENT_DATE
    )
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
               id INTEGER PRIMARY KEY,
               subject_name TEXT NOT NULL,
               teacher_name TEXT NOT NULL
    )
""")
conn.commit()

def register_student():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    grade = input("Введите свой класс: ")

    cursor.execute(f"""INSERT INTO students
                   (full_name, age, grade)
                   VALUES (?, ?, ?)""", (full_name, age, grade))
    
    conn.commit()
register_student()

def add_subject():
    subject_name = input("Введите название предмета: ")
    teagher_name = input("Введите имя учителя: ")

    cursor.execute(f"""INSERT INTO subjects
                   (subject_name, teacher_name)
                   VALUES (?, ?)""", (subject_name, teagher_name))
    
    conn.commit()

add_subject()

import sqlite3

conn = sqlite3.connect('university.db')

cursor = conn.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)
                ''')


cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
    couses_id INTEGER PRIMARY KEY AUTOINCREMENT,
    courses_name TEXT,
    instructor TEXT
)
                ''')
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


cursor.execute('''CREATE TABLE IF NOT EXISTS student_course (
    student_id INTEGER,
    course_id INTEGER
    FOREING KEY (student_id) REFERENCES students(id)
    FOREING KEY (cource_id) REFERENCES students(courseid)
    PRIMARY KEY (student_id, course_id)
    )''')

while True:
    print("""
          1. add new student
          2. add new course
          3. show student list
          4. show coursw list
          5. enroll student to course
          6. show course students
          7. Exit
          """)
    
    choice = input('enter an option(1-7)')
    match choice:
        case "1":
            name = input("enter student's name")
            age = int(input("enter student's age"))
            major = input("enter student's major")
            cursor.execute("INSERT INTO students (name, age, major) VALUES (?,?,?)", (name, age, major))
            conn.commit()
        case "2":
            course_name = input("enter course name")
            instructor = input("enterrr course instructor")
            cursor.execute("INSERT INTO courses (course_name, instructor) VALUES(?,?)",(course_name, instructor))
            conn.commit()
        case "3":
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            if not students:
                print("not student to show")
            else:
                print("\n students list")
                for student in students:
                    print(student[0], student[1], student[2])
        case "4":
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()
            if not courses:
                print("not courses to show")
            else:
                print("\n courses list")
                for course in courses:
                    print(course[0], course[1])
        case "5":
            student_id = int(input("enter student id"))
            course_id = int(input("enter course id"))
            cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (?,?)",(student_id, course_id ))
        
        case "6":
            course_id = int(input("enter course id"))
            cursor.execute("""SELECT students.id, students.name, students.age, students.major
                           FROM students, student_course
                           WHERE students.id = students_course.student_id
                           AND student_course.course_id = ?""", (course_id))
            students = cursor.fetchall()
            if not students:
                print("not student to show")
            else:
                print("\n students list")
                for student in students:
                    print(student[0], student[1], student[2], student[3])
        case "7":
            break
        case _:
            print("wrong choice")

            

        
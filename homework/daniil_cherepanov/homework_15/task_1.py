import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

try:
    # 1 Создайте студента (student)
    cursor.execute("""
        INSERT INTO students (name, second_name, group_id)
        VALUES (%s, %s, %s)
    """, ("Elizaveta", "Cherepanova", None))

    student_id = cursor.lastrowid
    print("Student created:", student_id)

    # 2 Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
    books = ["418 - я чайник", "JAVA pro"]

    books_data = [(book, student_id) for book in books]

    cursor.executemany("""
        INSERT INTO books (title, taken_by_student_id)
        VALUES (%s, %s)
    """, books_data)

    print("Books added")

    # 3 Создайте группу (group)
    cursor.execute("""
        INSERT INTO `groups` (title, start_date, end_date)
        VALUES (%s, %s, %s)
    """, ("Разработчик JAVA", "2024-03-11", "2026-02-27"))

    group_id = cursor.lastrowid
    print("Group created:", group_id)

    # Определение студента в группу
    cursor.execute("""
        UPDATE students
        SET group_id = %s
        WHERE id = %s
    """, (group_id, student_id))

    print("Student assigned to group")

    # 5 Создайте несколько учебных предметов (subjects)
    subjects = ["Тестирование мобильных приложений", "Нагрузочное тестирование"]
    subject_ids = []

    for subject in subjects:
        cursor.execute("""
            INSERT INTO subjects (title)
            VALUES (%s)
        """, (subject,))

        subject_ids.append(cursor.lastrowid)

    print("Subjects created:", subject_ids)

    # 6 Создайте по два занятия для каждого предмета (lessons)
    lesson_ids = []

    for subject_id in subject_ids:
        for i in range(1, 3):
            cursor.execute("""
                INSERT INTO lessons (title, subject_id)
                VALUES (%s, %s)
            """, (f"Lesson {i}", subject_id))

            lesson_ids.append(cursor.lastrowid)

    print("Lessons created:", lesson_ids)

    # 7 Поставьте своему студенту оценки (marks) для всех созданных вами занятий
    marks_data = [(student_id, lesson_id, 3) for lesson_id in lesson_ids]

    cursor.executemany("""
        INSERT INTO marks (student_id, lesson_id, value)
        VALUES (%s, %s, %s)
    """, marks_data)

    print("Marks added")

    print("Marks added")

    db.commit()

    print("\n--- Student full info ---")

    cursor.execute("""
        SELECT s.name, s.second_name, g.title, b.title,
               l.title, sub.title, m.value
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON s.id = m.student_id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.id = %s
    """, (student_id,))

    for row in cursor.fetchall():
        print(row)


except Exception as e:
    print("Error:", e)
    db.rollback()

finally:
    cursor.close()
    db.close()

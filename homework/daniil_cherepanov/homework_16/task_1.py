import csv
from pathlib import Path
import os
import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()

# Подключение к базе данных
db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

file_path = Path(r"C:\Projects\DaniilCh-New\homework\eugene_okulik\Lesson_16\hw_data\data.csv")

with file_path.open(newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, fieldnames=[
        "name", "second_name", "group_title", "book_title", "subject_title", "lesson_title", "mark"
    ])
    next(reader)
    for row in reader:
        name = row["name"]
        second_name = row["second_name"]
        group_title = row["group_title"]
        book_title = row["book_title"]
        subject_title = row["subject_title"]
        lesson_title = row["lesson_title"]
        mark_value = row["mark"]

        cursor.execute("""
            SELECT s.name
            FROM students s
            LEFT JOIN `groups` g ON s.group_id = g.id
            LEFT JOIN books b ON b.taken_by_student_id = s.id
            LEFT JOIN marks m ON s.id = m.student_id
            LEFT JOIN lessons l ON m.lesson_id = l.id
            LEFT JOIN subjects sub ON l.subject_id = sub.id
            WHERE s.name = %s
            AND s.second_name = %s
            AND g.title = %s
            AND b.title = %s
            AND sub.title = %s
            AND l.title = %s
            AND m.value = %s
        """, (
            name,
            second_name,
            group_title,
            book_title,
            subject_title,
            lesson_title,
            mark_value
        ))

        result = cursor.fetchone()

        if not result:
            print("Missing data in DB:")
            print(row)
            print()

cursor.close()
db.close()

# список студентов
students = ['Ivanov', 'Petrov', 'Sidorov']

# список предметов
subjects = ['math', 'biology', 'geography']

# объединяем элементы
students_str = ", ".join(students)
subjects_str = ", ".join(subjects)

# вывод итогового текста
print(f"Students {students_str} study these subjects: {subjects_str}")

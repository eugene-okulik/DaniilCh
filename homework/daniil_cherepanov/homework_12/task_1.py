from datetime import datetime, timedelta
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()

HOMEWORK_DIR = CURRENT_FILE.parents[2]

FILE_PATH = HOMEWORK_DIR / "eugene_okulik" / "hw_13" / "data.txt"

print("Открываем файл:", FILE_PATH)

with open(FILE_PATH, encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        left_part, action = line.split(" - ", 1)
        number_str, date_str = left_part.split(". ", 1)
        number = int(number_str)

        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        print(f"\nСтрока №{number}")
        print(f"Исходная дата: {date}")

        if number == 1:
            print("Дата через неделю:", date + timedelta(days=7))

        elif number == 2:
            print("День недели:", date.strftime("%A"))

        elif number == 3:
            days_ago = (datetime.now() - date).days
            print(f"Это было {days_ago} дней назад")

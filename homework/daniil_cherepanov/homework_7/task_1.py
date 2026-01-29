import random

# Запрашиваем зарплату
salary = int(input("Введите зарплату: "))

# Определяем, будет ли бонус
bonus = random.choice([True, False])

# Добавляем случайную сумму
if bonus:
    bonus_amount = random.randint(100, 5000)
    salary += bonus_amount

# Вывод результата
print(f"{salary}, {bonus} - '${salary}'")
lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
]


def add_ten_from_line(line):
    number = int(line.split(":")[-1].strip())
    return number + 10


for line in lines:
    print(add_ten_from_line(line))
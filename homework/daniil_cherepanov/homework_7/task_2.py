import math


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
indexes = [5, 200, 1000, 100000]
current_index = 0

for number in fib:
    current_index += 1

    if current_index in indexes:
        if current_index <= 1000:
            print(f"{current_index}-е число Фибоначчи: {number}")
        else:
            digits = int(math.log10(number)) + 1
            print(
                f"{current_index}-е число Фибоначчи содержит {digits} цифр"
            )

    if current_index == max(indexes):
        break

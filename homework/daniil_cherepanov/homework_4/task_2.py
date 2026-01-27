# первая строка
result = "результат операции: 42"

# извлекаем число
number = int(result[result.index(':') + 2:])

# прибавляем 10 и вывод
print(number + 10)


# вторая строка
result = "результат операции: 514"

# извлекаем число
number = int(result[result.index(':') + 2:])

# прибавляем 10 и вывод
print(number + 10)


# третья строка
result = "результат работы программы: 9"

# извлекаем число
number = int(result[result.index(':') + 2:])

# прибавляем 10 и вывод
print(number + 10)

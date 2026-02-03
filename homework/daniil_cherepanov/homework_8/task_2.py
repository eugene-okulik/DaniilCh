# список температур
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

# температура выше 28
hot_days = list(filter(lambda t: t > 28, temperatures))

# Максимальная, минимальная и средняя температура
max_temp = max(hot_days)
min_temp = min(hot_days)

avg_temp = round(sum(hot_days) / len(hot_days), 2)

print("Жаркие дни:", hot_days)
print("Максимальная температура:", max_temp)
print("Минимальная температура:", min_temp)
print("Средняя температура:", avg_temp)

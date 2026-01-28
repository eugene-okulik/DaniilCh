# перебираем числа
for number in range(1, 101):

    # если число кратно и 3 и 5
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")

    # если число кратно 3
    elif number % 3 == 0:
        print("Fuzz")

    # если число кратно 5
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

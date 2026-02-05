def operation_control(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        else:
            operation = "/"

        return func(first, second, operation)

    return wrapper


@operation_control
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        # Округляем
        return round(first / second, 3)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(calc(a, b))

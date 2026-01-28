secret_number = 7

while True:
    guess = int(input("Угадайте цифру от 0 до 9: "))
    if guess == secret_number:
        print("А ты эстрасенс!")
        break
    print("Крути барабан")

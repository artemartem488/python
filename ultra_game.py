import random
secret_number = random.randint(1,10)
print(secret_number)
user_score = 3
while user_score > 0:
    user_score -= 1
    user_number = int(input("Введите число от 1 до 10:"))
    if user_number < secret_number:
        print("Загаданное число больше")
    elif user_number > secret_number:
        print("Загаданное число меньше")
    else:
        print("Ты угадал!")
        break
else:
    print("Ты проиграл!")

import random
hidden_number = random.randint(0, 10)
user_number = int(input("Угадайте число от 1 до 10: "))
if user_number == hidden_number:
    print("Ты отгадал!")
elif user_number < hidden_number:
    print("Мое число больше!")
else:
    print("Мое число меньше!")
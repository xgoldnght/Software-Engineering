class CustomException(Exception):
    pass
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    if num2 == 0:
        raise CustomException("Деление на ноль недопустимо!")
    result = num1 / num2
    print("Результат деления:", result)
except ValueError:
    print("Ошибка: некорректный ввод числа!")
except CustomException as ex:
    print("Ошибка:", str(ex))
def check_age(age):
    if age < 0:
        raise CustomException("Возраст не может быть отрицательным числом!")
    if age > 100:
        raise CustomException("Возраст не может быть больше 100!")
    print("Возраст:", age)
try:
    age = int(input("Введите ваш возраст: "))
    check_age(age)
except ValueError:
    print("Ошибка: некорректный ввод возраста!")
except CustomException as ex:
    print("Ошибка:", str(ex))
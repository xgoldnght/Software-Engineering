# Получение данных от пользователя
user_input = input("Введите последовательность чисел, разделенных пробелом: ")
# Разделение введенной строки на числа
numbers_list = user_input.split()
# Преобразование строковых чисел в целочисленный тип (int)
numbers_list = [int(num) for num in numbers_list]
# Преобразование списка в кортеж
numbers_tuple = tuple(numbers_list)
# Вывод списка и кортежа
print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)
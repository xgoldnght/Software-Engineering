def average(*args):
    if len(args) == 0:
        return 0  # Если нет аргументов, среднее значение равно 0
    total = sum(args)  # Суммируем все аргументы
    return total / len(args)  # Рассчитываем среднее значение

if __name__ == "__main__":
    # Точка входа
    values = []  # Создаем пустой список для аргументов

    # Считываем аргументы от пользователя
    while True:
        try:
            value = float(input("Введите значение (или любой нечисловой символ для завершения): "))
            values.append(value)
        except ValueError:
            break  # Завершаем ввод, если введен нечисловой символ

    avg = average(*values)  # Вызываем функцию и передаем значения из списка
    print(f"Среднее арифметическое: {avg}")
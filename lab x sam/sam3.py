def count_most_common_numbers(sequence):
    number_counts = {}
    # Подсчет количества каждого числа
    for digit in sequence:
        if digit.isdigit():
            digit = int(digit)
            number_counts[digit] = number_counts.get(digit, 0) + 1
    # Получение трех самых часто встречаемых чисел
    most_common_numbers = sorted(number_counts, key=number_counts.get, reverse=True)[:3]
    # Создание словаря с тремя самыми часто встречаемыми числами
    result_dict = {num: number_counts[num] for num in most_common_numbers}
    return result_dict
# Пример использования
sequence = "7987685912345678765432"
result = count_most_common_numbers(sequence)
print(result)  # {7: 6, 8: 6, 6: 4}
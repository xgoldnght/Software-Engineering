# Функция для подсчета количества букв латинского алфавита
def count_letters(text):
    return sum(c.isalpha() and c.isascii() for c in text)
# Функция для подсчета количества слов
def count_words(text):
    return len(text.split())
# Функция для подсчета количества строк
def count_lines(text):
    return text.count('\n') + 1
# Чтение текста из файла
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
# Получение статистики
letter_count = count_letters(text)
word_count = count_words(text)
line_count = count_lines(text)
# Вывод результатов
print(f"Input file contains: {letter_count} letters")
print(f"{word_count} words")
print(f"{line_count} lines")
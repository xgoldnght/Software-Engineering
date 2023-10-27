import re
from collections import Counter

# Функция для подсчета количества слов в файле
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\w+', text)
        return len(words)

# Функция для определения самого часто встречающегося слова
def most_common_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\w+', text)
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)
        return most_common[0]

# Замените 'your_file.txt' на путь к вашему текстовому файлу
file_path = 'your_file.txt'

total_words = count_words(file_path)
most_common = most_common_word(file_path)

print(f"Общее количество слов в файле: {total_words}")
print(f"Самое часто встречающееся слово: '{most_common[0]}' (встречается {most_common[1]} раз)")

# Если вы хотите сохранить результаты в файл, вы можете сделать это следующим образом:
# with open('results.txt', 'w', encoding='utf-8') as result_file:
#     result_file.write(f"Общее количество слов в файле: {total_words}\n")
#     result_file.write(f"Самое часто встречающееся слово: '{most_common[0]}' (встречается {most_common[1]} раз)\n")
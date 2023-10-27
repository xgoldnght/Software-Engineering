from collections import Counter
import re
# Функция для чтения файла и анализа текста
def analyze_text(file_path, num_words=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\w+', text.lower())  # Приводим к нижнему регистру и разбиваем на слова
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(num_words)  # Получаем наиболее часто встречающиеся слова

        return most_common_words
# Замените 'sample.txt' на путь к вашему текстовому файлу
file_path = 'sample.txt'
# Получаем результат анализа
most_common_words = analyze_text(file_path)
# Выводим наиболее часто встречающиеся слова
print("Наиболее часто встречающиеся слова:")
for word, count in most_common_words:
    print(f"{word}: {count} раз")
# Вы можете изменить num_words, чтобы получить больше или меньше слов в выводе
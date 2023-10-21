# Получите предложение от пользователя
sentence = input("Введите предложение на английском: ")

# Выведите длину предложения
sentence_length = len(sentence)
print(f"Длина предложения: {sentence_length} символов")

# Переведите предложение в нижний регистр
lowercase_sentence = sentence.lower()
print(f"Предложение в нижнем регистре: {lowercase_sentence}")

# Подсчитайте количество гласных (a, e, i, o, u) в предложении
vowels_count = sum(1 for char in lowercase_sentence if char in 'aeiou')
print(f"Количество гласных: {vowels_count}")

# Замените все слова "ugly" на "beauty"
replaced_sentence = lowercase_sentence.replace("ugly", "beauty")
print(f"Предложение после замены: {replaced_sentence}")

# Проверьте, начинается ли предложение с "The" и заканчивается ли на "end"
starts_with_the = lowercase_sentence.startswith("the")
ends_with_end = lowercase_sentence.endswith("end")
print(f"Начинается с 'The': {starts_with_the}")
print(f"Заканчивается на 'end': {ends_with_end}")
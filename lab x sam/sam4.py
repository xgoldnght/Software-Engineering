# Функция для замены запрещенных слов в предложении
def censor_sentence(sentence, forbidden_words):
    words = sentence.split()
    censored_words = []
    for word in words:
        # Приводим к нижнему регистру для проверки
        word_lower = word.lower()
        if word_lower in forbidden_words:
            # Заменяем слово на звездочки
            censored_word = '*' * len(word)
            censored_words.append(censored_word)
        else:
            censored_words.append(word)
    return ' '.join(censored_words)
# Замените 'input.txt' на путь к вашему файлу с запрещенными словами
forbidden_words_file = 'input.txt'
# Замените 'input_sentence.txt' на путь к вашему файлу с предложением
input_sentence_file = 'input_sentence.txt'
# Чтение запрещенных слов
forbidden_words = set()
with open(forbidden_words_file, 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip().lower()
        forbidden_words.add(word)
# Чтение предложения для проверки
with open(input_sentence_file, 'r', encoding='utf-8') as file:
    input_sentence = file.read()
# Замена запрещенных слов
censored_sentence = censor_sentence(input_sentence, forbidden_words)
# Вывод результата
print(censored_sentence)
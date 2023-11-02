class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self._occupation = occupation  # Используем префикс _ для инкапсуляции

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет. Я работаю как {self._occupation}.")
# Создадим объект класса Person
person1 = Person("Иван", 30, "Инженер")
# Выведем информацию о человеке
person1.introduce()
# Попытка доступа к "скрытому" атрибуту _occupation
print(f"Моя профессия: {person1._occupation}")
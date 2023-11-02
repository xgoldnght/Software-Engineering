class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")
# Создадим объект класса Person
person1 = Person("Иван", 30)
# Выведем информацию о созданном объекте
person1.introduce()
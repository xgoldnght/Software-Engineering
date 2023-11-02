class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.hobbies = []
    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")
    
    def set_hobbies(self, hobbies):
        self.hobbies = hobbies
    
    def show_hobbies(self):
        if self.hobbies:
            print(f"Мои хобби: {', '.join(self.hobbies)}")
        else:
            print("У меня пока нет хобби.")
# Создадим объект класса Person
person1 = Person("Иван", 30, "Инженер")
# Установим хобби для объекта
person1.set_hobbies(["горные лыжи", "фотография"])
# Выведем информацию о человеке и его хобби
person1.introduce()
person1.show_hobbies()
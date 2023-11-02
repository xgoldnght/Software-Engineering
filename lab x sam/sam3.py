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
class Employee(Person):
    def __init__(self, name, age, occupation, salary):
        super().__init__(name, age, occupation)
        self.salary = salary
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я работаю как {self.occupation}, и моя зарплата составляет {self.salary}.")
# Создадим объект класса Employee
employee1 = Employee("Мария", 25, "Программист", 50000)
# Выведем информацию о работнике
employee1.introduce()
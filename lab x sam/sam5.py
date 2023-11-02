class Dog:
    def make_sound(self):
        return "Гав-гав!"

class Cat:
    def make_sound(self):
        return "Мяу!"

def print_sound(animal):
    print(animal.make_sound())

# Создадим объекты
dog = Dog()
cat = Cat()

# Вызовем метод make_sound для собаки и кошки
print_sound(dog)
print_sound(cat)
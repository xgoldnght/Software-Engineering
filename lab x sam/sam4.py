class Logger:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        # Выводим информацию о вызове функции и переданных аргументах
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: args={args}, kwargs={kwargs}')
        # Вызываем декорируемую функцию
        return self.func(*args, **kwargs)
@Logger
def add(x, y):
    return x + y
@Logger
def subtract(x, y):
    return x - y
# Вызываем декорированные функции
result1 = add(3, 5)
result2 = subtract(10, 7)
print(f'Результат сложения: {result1}')
print(f'Результат вычитания: {result2}')
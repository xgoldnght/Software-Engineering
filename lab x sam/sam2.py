def fib(n):
    a, b = 1, 1
    count = 0
    with open("fib.txt", "w") as file:
        while count < n:
            file.write(str(a) + "\n")
            yield a
            a, b = b, a+b
            count += 1
# Генерируем 200 чисел Фибоначчи
fibonacci_iter = fib(200)
# Выводим результат в консоль
for num in fibonacci_iter:
    print(num)
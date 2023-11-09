def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_numbers = list(fib(200))
print(fib_numbers[-1])
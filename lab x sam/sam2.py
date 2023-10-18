a = int(input())
b = int(input())

if a >= 5 and b >= 6:
    c = a
    a = b
    b = c
    print('Вы выиграли!', a, b)
else:
    print('Вы проиграли')
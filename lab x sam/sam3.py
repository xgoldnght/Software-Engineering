# Заданные списки
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
# Функция для расчета площади треугольника по трем сторонам (по формуле Герона)
def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
# Найдем максимальные и минимальные значения в каждом списке
one_max = max(one)
one_min = min(one)
two_max = max(two)
two_min = min(two)
three_max = max(three)
three_min = min(three)
# Создадим два треугольника, используя максимальные и минимальные значения
triangle1 = [one_max, two_min, three_min]
triangle2 = [one_min, two_max, three_max]
# Рассчитаем площади этих двух треугольников
area1 = calculate_triangle_area(*triangle1)
area2 = calculate_triangle_area(*triangle2)
# Выведем результат в консоль
print("Площадь первого треугольника (максимальные и минимальные значения):", area1)
print("Площадь второго треугольника (максимальные и минимальные значения):", area2)
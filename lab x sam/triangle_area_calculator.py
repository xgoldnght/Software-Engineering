# triangle_area_calculator.py
def calculate_triangle_area(a, b, c):
    # Полупериметр треугольника
    s = (a + b + c) / 2
    # Формула Герона для вычисления площади
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
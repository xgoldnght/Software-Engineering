# user_interaction.py
from triangle_area_calculator import calculate_triangle_area

def main():
    print("Вычисление площади треугольника по формуле Герона")
    print("Введите длины сторон треугольника:")
    a = float(input("Длина стороны a: "))
    b = float(input("Длина стороны b: "))
    c = float(input("Длина стороны c: "))

    # Проверка на существование треугольника (сумма двух сторон больше третьей)
    if a + b > c and a + c > b and b + c > a:
        area = calculate_triangle_area(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")
    else:
        print("Треугольник с такими сторонами не существует.")

if __name__ == "__main__":
    main()
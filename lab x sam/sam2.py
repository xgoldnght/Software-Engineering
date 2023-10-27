import json
from datetime import datetime
# Функция для ввода информации о расходах
def add_expense(expenses, category, amount):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expenses.append({'timestamp': timestamp, 'category': category, 'amount': amount})
# Функция для сохранения расходов в файл
def save_expenses(expenses, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)
# Функция для вывода расходов в консоль
def display_expenses(expenses):
    for expense in expenses:
        print(f"{expense['timestamp']} - {expense['category']}: ${expense['amount']}")
# Замените 'expenses.json' на имя файла, в котором вы хотите хранить данные
expenses_filename = 'expenses.json'
# Заводим пустой список для хранения расходов
expenses = []
# Основной цикл программы
while True:
    print("\n1. Добавить расход")
    print("2. Показать расходы")
    print("3. Выход")
    choice = input("Выберите действие (1/2/3): ")
    if choice == '1':
        category = input("Введите категорию расхода: ")
        amount = float(input("Введите сумму расхода: "))
        add_expense(expenses, category, amount)
        save_expenses(expenses, expenses_filename)
        print("Расход успешно добавлен!")
    elif choice == '2':
        if not expenses:
            print("Нет сохраненных расходов.")
        else:
            print("\nСуществующие расходы:")
            display_expenses(expenses)
    elif choice == '3':
        print("Программа завершена.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
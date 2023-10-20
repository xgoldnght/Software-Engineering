import datetime
import time

# Задаем продолжительность выполнения программы (5 секунд)
duration = 5  # в секундах

# Получаем текущее время и время старта программы
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=duration)

# Запускаем цикл, который выполняется в течение 5 секунд
while datetime.datetime.now() < end_time:
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")  # Форматируем время
    print("Текущее время:", formatted_time)
    time.sleep(1)  # Приостанавливаем выполнение программы на 1 секунду

print("Программа завершена")
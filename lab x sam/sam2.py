file_name = "empty_file.txt"
try:
    with open(file_name, 'r') as file:
        content = file.read()
        if len(content) == 0:
            raise Exception("файл пустой")
        else:
            print(content)
except FileNotFoundError:
    print(f"Файл {file_name} не найден")
except Exception as e:
    print(e)
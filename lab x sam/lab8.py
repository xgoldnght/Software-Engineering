import os
def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f"Папка {catalog[0]} содержит:")
        print(f'Деректории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([folder for folder in catalog[2]])}')
        print('-' * 40)
print_docs('C:/Users/user/Desktop/LAB')
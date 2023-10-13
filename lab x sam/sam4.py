a = input(str())  # Например слово Java
strlen = len(a)
print(strlen, '=Общее количество символов')
if strlen > 5:
    five_element = a[4]
else:
    five_element = 'Строка короче 5 символов'
print(a[0], '=первый', five_element, '=пятый', a[-1], '=последний')
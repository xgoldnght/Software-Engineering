def remove_element_from_tuple(tup, element):
    if element in tup:
        index = tup.index(element)
        new_tuple = tup[:index] + tup[index+1:]
        return new_tuple
    else:
        return tup
# Примеры использования
tup1 = (1, 2, 3)
result1 = remove_element_from_tuple(tup1, 1)
print(result1)  # (2, 3)
tup2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
result2 = remove_element_from_tuple(tup2, 3)
print(result2)  # (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
tup3 = (2, 4, 6, 6, 4, 2)
result3 = remove_element_from_tuple(tup3, 9)
print(result3)  # (2, 4, 6, 6, 4, 2)
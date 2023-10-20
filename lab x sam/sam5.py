def list_to_set(input_list):
    from collections import Counter
    counts = Counter(input_list)
    
    result_set = set()
    for number, count in counts.items():
        for i in range(1, count + 1):
            if i == 1:
                result_set.add(number)
            else:
                result_set.add(str(number) * i)
    return result_set
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(list_to_set(list_1))  # -> {'11', 1, 3, '33', '111'}
print(list_to_set(list_2))  # -> {5, '5555', '555555', '55555', '555', '55', '5555555'}
print(list_to_set(list_3))  # -> {'11', 1, 3, 2, 5, 6, '222222', '222', 7, '2222', '22222', '22'}
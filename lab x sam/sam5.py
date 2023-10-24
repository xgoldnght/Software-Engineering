def merge_lists_without_duplicates(list1, list2):
    merged_list = list(set(list1 + list2))
    return merged_list
# Примеры использования
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result1 = merge_lists_without_duplicates(list1, list2)
print(result1)  # [1, 2, 3, 4, 5, 6]
list3 = ['apple', 'banana', 'orange']
list4 = ['banana', 'grapefruit']
result2 = merge_lists_without_duplicates(list3, list4)
print(result2)  # ['apple', 'banana', 'grapefruit', 'orange']
list5 = []
list6 = [1, 2, 3]
result3 = merge_lists_without_duplicates(list5, list6)
print(result3)  # [1, 2, 3]
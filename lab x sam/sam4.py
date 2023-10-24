def extract_employee_records(records, element):
    if records.count(element) == 0:
        return ()

    if records.count(element) < 2:
        return records[records.index(element):]

    first_index = records.index(element)
    last_index = records.index(element, first_index + 1)

    return records[first_index:last_index+1]

# Примеры использования
records1 = (1, 2, 3)
result1 = extract_employee_records(records1, 8)
print(result1)  # ()

records2 = (1, 8, 3, 4, 8, 8, 9, 2)
result2 = extract_employee_records(records2, 8)
print(result2)  # (8, 3, 4, 8)

records3 = (1, 2, 8, 5, 1, 2, 9)
result3 = extract_employee_records(records3, 8)
print(result3)  # (8, 5, 1, 2, 9)
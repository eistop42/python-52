numbers = [12, 34, 50, 2, 3, 46]
max_number = numbers[0]

for number in numbers:
    # сравнить число с текущим максимумом
    if number > max_number:
        max_number = number
    print(f'Максимум: {max_number}')
print(max_number)

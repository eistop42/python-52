data = [10, -5, 20, -1, 30, 0, -7]

for value in data:
    if value < 0:
        continue  # пропускаем отрицательные значения
    # Выполняем сложную операцию только с положительными и нулём
    print(value)


for value in data:
    if value > 0:
        print(value)
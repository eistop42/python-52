numbers = [5, -2, 1, 3, -4, 0, 7]

for i in range(len(numbers)):
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            # поменять их местами
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    print(numbers)
print(numbers)
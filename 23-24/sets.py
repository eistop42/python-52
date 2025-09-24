a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a|b) # объединение
print(a&b) # пересечение
print(a-b) # разность
print(a^b) # симм.разность

# список --> множество --> список
numbers = [1,1,1,2,3]
print(list(set(numbers)))
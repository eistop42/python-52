# переменные
name = 'ilya'
age = 29

# вывод данных
print(name)
print(age)

# вывод данных друг за другом
print(name, age)

# вставить переменные в строку
print(f'Имя: {name}, Возраст: {age}')

# ввод данных пользователем

name = input('Введи имя: ')
print(f'Привет {name}')

radius = input('Введи радиус: ')
s = 3.14 * int(radius)**2
print(s)

radius = int(input('Введи радиус: '))
s = 3.14 * radius**2
print(s)

# если радиус дробный
radius = float(input('Введи радиус: '))
s = 3.14 * radius**2
print(s)


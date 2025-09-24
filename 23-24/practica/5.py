# Задание 5. Циклы. Итерация по объектам.
#
# Дана строка с буквами и цифрами.
# Подсчитайте количество букв в строке.

s = 'a1s2d3f4g5h6j7k8l9'

count = 0
for i in range(len(s)):
    symb = s[i]
    if symb.isdigit():
        print(symb)
        count += 1
print(f'Всего чисел: {count}')


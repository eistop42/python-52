# Напишите функцию, которая принимает в себя скорость и время,
# возвращает расстояние, которое получится преодолеть.

def find_distance(speed, time):
    return speed * time

print(find_distance(80, 2))

def find_factorial(number):
    res = 1
    for i in range(1, number+1):
        res *= i
    return res

def find_factorial2(number):
    if number == 1:
        return 1
    return number * find_factorial2(number-1)


names = ['alisa', 'bob', 'tom']
name_to_find = 'alisa'

if name_to_find in names:
    print('Есть в списке')

def find_name(name, name_list):
    if name in name_list:
        return True
    return False

print(find_name('alisa', ['alisa', 'tom']))
print(find_name('jack', ['alisa', 'tom']))


s = "привет2312??как77712дела22312"
new = ''
for letter in s:
    if letter.isalpha():
        new += letter
print(new)

def stroka(string):
    new = ''
    for letter in string:
        if letter.isalpha():
            new += letter
    return new

print(stroka('yhasdgfuygasf23465jhsdfg234'))

user = input('Введи выражние: ')

number_1 = int(user[0])
number_2 = int(user[2])
action = user[1]

if action == '+':
    res = number_1 + number_2
    print(res)
elif action == '-':
    res = number_1 - number_2
    print(res)

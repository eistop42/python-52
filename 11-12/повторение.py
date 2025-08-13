# 1
# first_name = input('Введи имя: ')
# last_name = input('Введи фамилию: ')
#
# print(first_name, last_name, '- рады снова видеть вас в академии')
# print(f'{first_name} {last_name} - рады снова видеть вас в академии')

# 2

# radius = int(input('Введи радиус: '))
# if radius > 0:
#     s = radius**2*3.14
#     print(f'Радиус: {s}')
# else:
#     print('Неверные данные')
#

# 3

# for i in range(100):
#     if i % 3 == 0:
#         print(i)

# 4
# all_sum = 0
# for i in range(2):
#     price = int(input('Цена товара: '))
#     count = int(input('Кол-во товара: '))
#
#     if price > 0:
#         res = price * count
#
#         all_sum += res
#         print(f'Cумма: {res}')
#         print(res)
#     else:
#         print('невалидные данные')
#
# print(f'Общая сумма: {all_sum}')

# import random
#
# number = random.randint(1,10)
# question = input('Введи вопрос: ')
# if number > 5:
#     print('Нет')
# else:
#     print('Да')




while True:
    amount = int(input('Введи сумму: '))
    currency = input('Валюта: доллар, евро, юань, выхоод: ')
    if currency == 'доллар':
        res = round(amount / 85)
        print(f'В доллларах: {res}')
    elif currency == 'евро':
        res = round(amount / 90)
        print(f'В евро: {res}')
    elif currency == 'выход':
        break


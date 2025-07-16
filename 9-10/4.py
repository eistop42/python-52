import time

while True:
    rubles = input('Сумма в рублях (введи 0 для выхода)')
    if rubles == '0':
        print('выхожу их программы')
        break
    dollar = int(rubles) / 78
    print(f'В долларах: {dollar}')

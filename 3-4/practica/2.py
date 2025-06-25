summa = int(input('Введи сумму: '))

if summa > 1000:
    itog = summa - (summa * 10)/100
    print(f'C учетом скидки: {itog}')
else:
    print(f'Итог: {summa}')
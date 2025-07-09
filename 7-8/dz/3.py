word = input('ввведи слово: ')
simvol = input('ввведи символ: ')
res = word.find(simvol)

if res >= 0:
    print(f'Символ есть, индекс {res}')
else:
    print('Такого символа нет')

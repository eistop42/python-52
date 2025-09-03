words = {'яблоко': 'apple', 'банан': 'banana', 'вишня': 'cherry'}

for key, value in words.items():
    print(f'Слово: {key}, Перевод: {value}')

userword = input('Введи слово на русском: ')

if userword in words:
    res = words[userword]
    print(f'Перевод: {res}')
else:
    print('такого слова нет')
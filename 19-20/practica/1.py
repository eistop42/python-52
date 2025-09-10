words = {'яблоко': 'apple', 'банан': 'banana', 'вишня': 'cherry'}

for key, value in words.items():
    word = input(f'Введи английский перевод для {key}: ')

    if word == value:
        print('Верно')
    else:
        print('неверно')
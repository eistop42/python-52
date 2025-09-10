words = [
    {'russian': 'яблоко', 'english': 'apple', 'spanish': 'manzana', 'french': 'pomme'},
    {'russian': 'банан', 'english': 'banana', 'spanish': 'plátano', 'french': 'banane'},
    {'russian': 'вишня', 'english': 'cherry', 'spanish': 'cereza', 'french': 'cerise'}
]

user_word = input('Введи слово на русском: ')
user_lang = input('На какой язык перевести: ')

for word in words:
    if user_word == word['russian']:
        if user_lang in word.keys():
            res = word[user_lang]
            print(f'Перевод: {res}')
        else:
            print('нет такого языка')
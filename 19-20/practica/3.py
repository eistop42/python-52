words = [
    {'russian': 'яблоко', 'english': 'apple', 'spanish': 'manzana', 'french': 'pomme'},
    {'russian': 'банан', 'english': 'banana', 'spanish': 'plátano', 'french': 'banane'},
    {'russian': 'вишня', 'english': 'cherry', 'spanish': 'cereza', 'french': 'cerise'}
]

count = 0
for word in words:
    user = input(f'Введи английский перевод для {word["russian"]}: ')
    if user == word['english']:
        print('Верно')
        count += 1
print(f'Баллы: {count}')
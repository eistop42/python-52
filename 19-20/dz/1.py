questions = {'Россия': 'Москва',
             'Франция': 'Париж',
             'Бразилия': 'Бразилиа'
             }

count = 0
for key, value in questions.items():
    city = input(f'Введи столицу страны {key}: ').lower()
    if city == value.lower():
        print('Правильный ответ')
        # count = count + 1
        count += 1
    else:
        print('Неверно')

print(f'Кол-во баллов: {count}')
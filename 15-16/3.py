
questions = [['Столица Италии', 'Рим'],
             ['Длинная река в Египте', 'Нил'],
             ['Самый большой океан', 'Тихий'],
             ['Столица России', 'Москва']
             ]

count = 0
for i in range(len(questions)):
    print(questions[i][0])
    answer = input('Введи ответ: ')

    if answer == questions[i][1]:
        print('Верно!')
        count += 1
    else:
        print('Неправильно')
print(f'Правильных ответов: {count}')



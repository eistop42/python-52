def sum_numbers(a, b):
    return a + b

def multy_numbers(a, b):
    return a * b


actions = {'1': {'text': 'сложить', 'func': sum_numbers},
           '2': {'text': 'умножить', 'func': multy_numbers}
           }

while True:
    number_1 = int(input('Первое число: '))
    number_2 = int(input('Второе число: '))

    print('Доступные операции: ')
    for action_number, action_value in actions.items():
        print(f'{action_number} - {action_value["text"]}')
    user = input('Выбери действие: ')
    if user in actions.keys():
        func = actions[user]['func']
        r = func(number_1, number_2)
        print(f'Результат: {r}')
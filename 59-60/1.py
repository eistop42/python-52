import os
import json

tasks = []

while True:
    user = input('Выбери действие: 1 - добавить задачу, 2 - посмотреть задачи')
    if user == '1':
        name = input('Введи текст: ')
        tasks.append(name)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f)
        print('Задача добавлена!')
    elif user == '2':
        if not os.path.exists('data.json'):
            data = []
        else:
            with open('data.json', encoding='utf-8') as f:
                data = json.load(f)
        if not tasks:
            print('нет задач')
        for number, task in enumerate(data, start=1):
            print(f'{number}.{task}')


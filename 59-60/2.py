import os
import json


def read_data(file):
    if not os.path.exists(file):
        return []
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_data(file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False)


def show_tasks(tasks: list):
    if not tasks:
        print('нет задач')
    for number, task in enumerate(tasks, start=1):
        print(f'{number}.{task}')


DATA_FILE = 'data.json'

tasks = read_data(DATA_FILE)

while True:
    user = input('Выбери действие: 1 - добавить задачу, 2 - посмотреть задачи')
    if user == '1':
        name = input('Введи текст: ')
        tasks.append(name)
        write_data(DATA_FILE)
        print('Задача добавлена!')
    elif user == '2':
        show_tasks(tasks)


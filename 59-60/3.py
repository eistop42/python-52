import os
import json


class DB:
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return f'Класс для работы с файлом {self.filename}'

    def read_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_data(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)


class TaskService:

    def __init__(self, db: DB):
        self.db = db
        self.tasks = self.db.read_data()

    def add_task(self, task_name):
        self.tasks.append(task_name)
        self.db.write_data(self.tasks)
        print('Задача добавлена!')

    def show_tasks(self):
        if not self.tasks:
            print('нет задач')
        for number, task in enumerate(self.tasks, start=1):
            print(f'{number}.{task}')


DATA_FILE = 'data.json'

db = DB(DATA_FILE)
task_service = TaskService(db)

while True:
    user = input('Выбери действие: 1 - добавить задачу, 2 - посмотреть задачи')
    if user == '1':
        name = input('Введи текст: ')
        task_service.add_task(name)
    elif user == '2':
        task_service.show_tasks()

    e

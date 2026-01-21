from task_service import TaskService
from db_service import DB

DATA_FILE = 'data.json'

db = DB(DATA_FILE)
task_service = TaskService(db)

while True:
    user = input('Выбери действие: 1 - добавить задачу, 2 - посмотреть задачи, 3 - удалить')
    if user == '1':
        name = input('Введи текст: ')
        task_service.add_task(name)
    elif user == '2':
        task_service.show_tasks()
    elif user == '3':
        task_service.show_tasks()
        task_number = int(input('Введи номер задачи: '))
        task_service.delete_task(task_number)



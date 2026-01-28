from tasks_service import TaskService
from db_service import DB

DATA_FILE = 'data.json'
db = DB(DATA_FILE)
task_service = TaskService(db)
# print(db)

while True:
    user = input('Выберите действие: 1 - добавить задачу, 2 - посмотреть задачи, 3 - удалить задачу: ')
    if user == '1':
        name = input('Введите текст: ')
        task_service.add_task(name)

    elif user == '2':
        task_service.show_tasks()

    elif user == '3':
        task_service.show_tasks()
        task_number = int(input('Введите номер задачи: '))
        task_service.delete_task(task_number)
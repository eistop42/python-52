from db_service import DB


class BaseTaskService:

    def __init__(self, db: DB):
        self.db = db
        self.tasks = self.db.read_data()

    def show_tasks(self):
        if not self.tasks:
            print('нет задач')
        for number, task in enumerate(self.tasks, start=1):
            print(f'{number}.{task}')

    def delete_task(self, number):
        # 1. Проверить, что есть задача с таким номером
        # 2. Если нет - написать
        # 3. Если есть - перебрать задачи и удалить нужную
        # 4. Сохранить измененный список в базу
        if number < 0 or number > len(self.tasks):
            print('Неправильный номер задачи')
            return
        self.tasks.pop(number-1)
        self.db.write_data(self.tasks)
        print('Удалили задачу')


class TaskService(BaseTaskService):

    def add_task(self, task_name):
        self.tasks.append(task_name)
        self.db.write_data(self.tasks)
        print('Задача добавлена!')


class TaskServiceLimit(TaskService):

    def add_task(self, task_name):
        if len(self.tasks) < 2:
            super(TaskService).add_task(task_name)
        else:
            print('истек лимит')

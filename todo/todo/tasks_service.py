from db_service import DB

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
        for num, task in enumerate(self.tasks, start=1):
            print(f'{num}. {task}')

    def delete_task(self, number):
        # 1. Проверить что есть задача с таким номером
        if number < 1 or number > len(self.tasks):  # Проверяем, существует ли задача с таким номером
            print('Задачи с таким номером не существует')  # Если нет - выводим сообщение
            return  # Выходим из метода
        # 2. Если есть перебрать и удалить
        deleted_task = self.tasks.pop(number - 1)  # Удаляем задачу по индексу (номер - 1)
        # 3. Сохранить изменённый список в базу
        self.db.write_data(self.tasks)  # Сохраняем обновленный список задач в файл
        print(f'Задача "{deleted_task}" удалена!')  # Сообщаем пользователю, что задача удалена
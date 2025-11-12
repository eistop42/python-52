
def add_task(task):
    # запись в файл
    with open('db.txt', 'a', encoding='utf-8') as f:
        f.write(f"{task};в ожидании")
        f.write('\n')


def read_file():
    """Просто прочитать данные из файла"""
    # чтение из файла
    try:
        with open('db.txt', 'r', encoding='utf-8') as f:
            data = f.read().strip()
            return data
    except FileNotFoundError:
        return None

def save_tasks(tasks):
    with open('db.txt', 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task)
            f.write('\n')


def show_tasks():
    """Преобразовать данные из файла в краисвый вид"""
    status_dict = {'в ожидании': '🔄', 'выполнено': '☑' }
    tasks = read_file()
    if not tasks:
        print('дел еще нет!')
        return
    tasks = tasks.split('\n')
    for number, task in enumerate(tasks, start=1):
        task_data = task.split(';')
        status_picture = status_dict[task_data[1]]
        print(f'{number}. Название: {task_data[0]}, Cтатус: {task_data[1]} {status_picture}')


def complete_task(task_number):
    # 1. Получить исходные данные
    # 2. Получить список задач
    # 3. Поменять статус, если есть такой номер задачи
    # 4. Сохранить в файл
    tasks = read_file()
    if not tasks:
        print('дел еще нет!')
        return
    tasks = tasks.split('\n')
    for number, task in enumerate(tasks, start=1):
        if number == task_number:
            task_data = task.split(';')
            task_data[1] = 'выполнено'
            # измени оригинальный спискок, вставь туда новое значение
            tasks[number-1] = ";".join(task_data)
            break
    else:
        print('нет такого дела')
    # сворачиваем данные в строку
    save_tasks(tasks)



while True:
    print('1 - добавить дело')
    print('2 - посмотреть дела')
    print('3 - выполнить дело')

    user = input('выбирай: ')

    if user == '1':
        task = input('введи название: ')
        add_task(task)
        print('дело добавлено!')
        print(show_tasks())

    elif user == '2':
        # вывести красиывый список дел из файла
        show_tasks()

    elif user == '3':
        show_tasks()
        number = int(input('введи номер задачи: '))
        complete_task(number)

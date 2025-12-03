import json
from datetime import datetime, timedelta
from pprint import pprint

def read_database(filename: str):
    """Чтение файла базы данных"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_database(data: dict, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_work_days(data):
    """найти даты для работы"""
    date_now = datetime.now() # текущая дата
    date_now = date_now.replace(hour=0, minute=0, second=0, microsecond=0)
    db_days= data['days'] # даты из базы

    work_days = []
    for day in db_days:
        date = day['date']
        date = datetime.strptime(date, '%d.%m.%Y')
        if date >= date_now:
            work_days.append(day)

    return work_days

def add_days(filename):
    data = read_database(filename)
    work_days = get_work_days(data)

    last_date = work_days[-1]['date']
    last_date = datetime.strptime(last_date, '%d.%m.%Y')
    new_days = []
    if len(work_days) < 15:
        for i in range(15):
            new_date = last_date + timedelta(days=i+1)
            new_date = new_date.strftime('%d.%m.%Y')
            new_day = {'date': new_date, 'free_slots': ['9:00', '12:00', '15:00', '18:00']}
            new_days.append(new_day)

    data['days'] += new_days
    write_database(data, 'data.json')


def get_work_days_keyboard():
    # 1. Заполнение будущих дней, если их нет
    add_days('data.json')

    # 2. Получение дней для записи
    data = read_database('data.json')
    work_days = get_work_days(data)
    keyboard = []
    for day in work_days:
        button = [day['date']]
        keyboard.append(button)

        if len(keyboard) == 3:
            break
    return {'keyboard': keyboard}

print(get_work_days_keyboard())
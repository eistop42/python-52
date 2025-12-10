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

    if work_days:
        last_date = work_days[-1]['date']
    else:
        last_date = datetime.now().strftime('%d.%m.%Y')

    last_date = datetime.strptime(last_date, '%d.%m.%Y')
    new_days = []
    if len(work_days) < 15:
        for i in range(15):
            new_date = last_date + timedelta(days=i+1)
            new_date = new_date.strftime('%d.%m.%Y')
            new_day = {'date': new_date, 'slots_free': ['9:00', '12:00', '15:00', '18:00']}
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


add_days('data.json')

def get_slots_free_keyboard(user_date):
    data = read_database('data.json')

    slots = []
    for day in data['days']:
        if day['date'] == user_date:
            slots = day['slots_free']
    new_slots = [[slot] for slot in slots]
    return {'keyboard': new_slots}

user_date = '12.12.2025'
user_slot = '9:00'
user_name = 'Алиса'
telegram_id = 1234
# прочитать данные из базы
# удалить слот с текущим временем из даты
# создать заявку: telegram_id, дата, время
# сохранить данные в базу
def create_zayavka(user_date, user_slot, user_name, telegram_id):
    data = read_database('data.json')
    zayavka = None
    try:
        for day in data['days']:
            if day['date'] == user_date:
                day['slots_free'].remove(user_slot)

                zayavka = {'name': user_name, 'date': user_date, 'time': user_slot, 'telegram_id': telegram_id}
                data['zayavki'].append(zayavka)
                write_database(data, 'data.json')
    except ValueError as e:
        print('Заявка с ошибкой', e)

    return zayavka


create_zayavka(user_date, user_slot, user_name, telegram_id)
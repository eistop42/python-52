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
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_work_days(data):
    """найти все доступные даты для работы"""
    datetime_now = datetime.now() # текущая дата
    date_now = datetime_now.date()
    time_now = datetime_now.time()
    db_days= data['days'] # даты из базы

    work_days = []
    for day in db_days:
        date = day['date']
        date = datetime.strptime(date, '%d.%m.%Y').date()
        if date == date_now:
            slots = filter_slots(day['slots_free'])
            if not slots:
                continue
            work_days.append(day)
        if date > date_now:
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


def filter_slots(slots: list):
    """Оставить слоты с актуальным временем"""
    current = datetime.now().time()
    filtered_slots = []
    for slot in slots:
        slot_time = datetime.strptime(slot, '%H:%M').time()
        if slot_time > current:
            filtered_slots.append(slot)
    return filtered_slots


def get_slots_free_keyboard(user_date):
    data = read_database('data.json')

    slots = []
    for day in data['days']:
        if day['date'] == user_date:
            slots = day['slots_free']

    if datetime.strptime(user_date, '%d.%m.%Y').date() == datetime.now().date():
        slots = filter_slots(slots)
    slots = [[slot] for slot in slots]
    return {'keyboard': slots}



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

# user_date = '16.12.2025'
# user_slot = '9:00'
# user_name = 'Алиса'
# telegram_id = 1234
# create_zayavka(user_date, user_slot, user_name, telegram_id)
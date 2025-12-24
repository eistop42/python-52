import requests
import random
import time

from db import get_work_days_keyboard, get_slots_free_keyboard, create_zayavka


token = ""
base_url = "https://api.telegram.org/bot" + token

getme_url = base_url + '/getMe' # тестирование
updates_url = base_url + '/getUpdates' # получить все сообщения
send_message_url = base_url + '/sendMessage'
my_id = 158448812


last_update_id = 0
state = None
user_choose_date = None

while True:
    updates = requests.get(updates_url, json={'offset': last_update_id+1}).json()
    for res in updates['result']:

        update_id = res['update_id']

        message = res['message']
        text = message['text']
        chat_id = message['chat']['id']
        telegram_id = message['from']['id']
        first_name = message['from']['first_name']


        print(message)
        if text == '/start':
            keyboard = {"keyboard": [['Записаться']]}
            requests.get(send_message_url, json={'text': "Привет! Это бот для записи на ресницы! Кликай на кнопки.", "chat_id": chat_id, 'reply_markup': keyboard})

        elif text == 'Записаться':
            keyboard = get_work_days_keyboard()
            requests.get(send_message_url, json={'text': text, 'chat_id': chat_id, 'reply_markup': keyboard})

            state = 'choose_date'

        elif state == 'choose_date':
            print('логи', text, keyboard, state)
            if [text] in keyboard['keyboard']:
                # находим свободные слоты по текущей дате
                keyboard = get_slots_free_keyboard(text)
                requests.get(send_message_url, json={'text': 'выбирай время', 'chat_id': chat_id, 'reply_markup': keyboard})
                state = 'choose_time'
                user_choose_date = text
            else:
                requests.get(send_message_url, json={'text': 'не понимаю...', 'chat_id': chat_id})

        elif state == 'choose_time':
            print(text, keyboard)
            if [text] in keyboard['keyboard']:
                slot = text
                date = user_choose_date
                telegram_id = chat_id

                create_zayavka(date, slot, first_name, telegram_id)
                requests.get(send_message_url, json={'text': 'заявка создана!', 'chat_id': chat_id})


    if updates['result']:
        last_update_id = update_id
        print(last_update_id)

    time.sleep(0.5)
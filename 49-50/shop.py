import requests
import time

token = ""
base_url = "https://api.telegram.org/bot" + token

getme_url = base_url + '/getMe'  # тестирование
updates_url = base_url + '/getUpdates'  # получить все сообщения
send_message_url = base_url + '/sendMessage'
send_photo = base_url + '/sendPhoto'

products = [{'name': 'Атлант расправил плечи', 'price': 1000, 'img': 'https://content.img-gorod.ru/pim/products/images/24/e4/019b1303-41e0-75a7-ab66-7a01de1b24e4.jpg?width=1920&height=919&fit=bounds'}]

last_update_id = 0
while True:
    # получение обновлений
    updates = requests.get(updates_url, json={'offset': last_update_id + 1}).json()
    for update in updates['result']:

        message = update['message']['text']
        chat_id = update['message']['chat']['id']
        print(message)

        if message == '/start':
            keyboard = {'keyboard': [['Товары']], 'resize_keyboard': True}
            requests.get(send_message_url, json={'text': 'Привет!',
                                                 'chat_id': chat_id,
                                                 'reply_markup': keyboard})
        if message == 'Товары':
            name = products[0]["name"]
            price = products[0]["price"]
            photo = products[0]['img']

            text = f'Название: {name} \nЦена: {price}'
            requests.get(send_message_url, json={'text': text, 'chat_id': chat_id})

            requests.get(send_photo, json={'photo':photo, 'chat_id': chat_id})

        last_update_id = update['update_id']

    # искусственная задержка

    time.sleep(1)

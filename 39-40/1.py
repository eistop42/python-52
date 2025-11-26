import requests
import pprint
import time

token = "8381198556:AAHf378Akb8iyfr4v2qxjM45YVK4SwOg188"
base_url = "https://api.telegram.org/bot" + token

getme_url = base_url + '/getMe' # тестирование
updates_url = base_url + '/getUpdates' # получить все сообщения
send_message_url = base_url + '/sendMessage'
my_id = 158448812

# res = requests.get(getme_url).json()

# requests.get(send_message_url, json={"chat_id": my_id, "text": 'привет'})


# pprint(updates)

print(updates_url)

last_update_id = 0
while True:
    updates = requests.get(updates_url, json={'offset': last_update_id+1}).json()
    for res in updates['result']:
        update_id = res['update_id']

        message = res['message']
        text = message['text']
        chat_id = message['chat']['id']

        print(message)
        if text == '/start':
            keyboard = {"keyboard": [['Записаться']]}
            requests.get(send_message_url, json={'text': "Привет! Это бот для записи на ресницы! Кликай на кнопки.", "chat_id": chat_id, 'reply_markup': keyboard})


        print(text, chat_id)
        last_update_id = update_id
        print(last_update_id)

    time.sleep(0.5)


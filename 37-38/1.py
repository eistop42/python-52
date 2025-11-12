import requests

token = "8381198556:AAHf378Akb8iyfr4v2qxjM45YVK4SwOg188"

base_url = "https://api.telegram.org/bot" + token

getme_url = base_url + '/getMe' # тестирование
updates_url = base_url + '/getUpdates' # получить все сообщения
my_id = 158448812

send_message_url = base_url + '/sendMessage'

res = requests.get(getme_url) # отправили и получили ответ от телеграма
print(res.json()) # вывели ответ телеграма в консоль

news = ["Фильм «Галактика Супер Марио в кино» выйдет 3 апреля 2026-го — смотрите первый трейлер", "Геймплей Гамбита и подарки к годовщине — о пятом сезоне Marvel Rivals"]
news2 = ["Бывший президент Nintendo удивлён, почему Xbox не спешит на Switch 2"]
# for new in news2:
#     mes = {'chat_id': my_id, 'text': new}
#     requests.get(send_message_url, json=mes)

# получение обновлений
updates = requests.get(updates_url).json()
print(updates)

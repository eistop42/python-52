import requests
from pprint import pprint

token = "8237537854:AAHDWLiVySfQf3_4i2RWxIuDhD5U1mBlpV4"
base_url = f"https://api.telegram.org/bot{token}/"

getme_url = base_url + 'getMe'
updates_url = base_url + 'getUpdates'
send_message_url = base_url + 'sendMessage'

my_id = '158448812'

response = requests.get(updates_url).json()
pprint(response)

requests.get(send_message_url, json={'chat_id': my_id, 'text': 'привет!'})



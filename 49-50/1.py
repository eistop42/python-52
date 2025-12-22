update = {'update_id': 782027312, 'message': {'message_id': 3041, 'from': {'id': 158448812, 'is_bot': False, 'first_name': 'Ilya', 'last_name': 'Evdokimov', 'username': 'evdokimovis', 'language_code': 'ru'}, 'chat': {'id': 158448812, 'first_name': 'Ilya', 'last_name': 'Evdokimov', 'username': 'evdokimovis', 'type': 'private'}, 'date': 1766415534, 'text': '/start', 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}

user = {'name': 'alisa'}

print(user['name'])
print(update['message']['text'])
print(update['message']['chat']['id'])
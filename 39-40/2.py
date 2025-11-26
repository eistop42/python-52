d = {
    'ok': True,
    'result': [
        {
            'message': {
                'text': 'привет'

            },

        },
        {
            'message': {
                'text': 'пока'
            },
            'chat': {
                'id': '158448815'
            }
        }
    ]
}

for res in d['result']:
    print(res['message']['text'])
    print(res['chat']['id'])

user = {'name': 'alisa', 'age': 24, 'pets': [
    {'name': 'тузик', 'age': 2, 'eat': {'name': 'кость'}},
    {'name': 'бобик', 'age': 3, 'eat': {'name': 'большая кость'}}
]}

for pet in user['pets']:
    print(pet['name'])

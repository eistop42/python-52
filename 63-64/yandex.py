import requests

class YandexGPT:
    def __init__(self, token, catalog):

        self.url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
        self.CATALOG = catalog
        self.TOKEN = token

    def get_answer(self, user_question):
        data = {
            'modelUri': f'gpt://{self.CATALOG}/yandexgpt/rc',
            'messages': [
                {
                    'role': 'user',
                    'text': user_question
                }
            ]
        }

        headers = {'Authorization': f'Bearer {TOKEN}', }
        resp = requests.post(self.url, json=data, headers=headers)
        resp = resp.json()
        text = resp['result']['alternatives'][0]['message']['text']
        print(text)


CATALOG = ''
TOKEN = ''

gpt = YandexGPT(TOKEN, CATALOG)

while True:
    user = input('Введи вопрос (q - для выхода): ')
    if user == 'q':
        print("Пока!")
        break
    gpt.get_answer(user)
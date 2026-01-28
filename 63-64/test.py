import requests

url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
CATALOG = 'ваш_каталог'  # Например: b1gxxxxxxxxxxxxxxxx
TOKEN = 'ваш_IAM_токен'

data = {
    'modelUri': f'gpt://{CATALOG}/yandexgpt/latest',
    'completionOptions': {
        'stream': False,
        'temperature': 0.3,
        'maxTokens': 1000
    },
    'messages': [
        {
            'role': 'user',
            'text': 'как дела'
        }
    ]
}

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

resp = requests.post(url, json=data, headers=headers)

if resp.status_code == 200:
    result = resp.json()
    print(result['result']['alternatives'][0]['message']['text'])
else:
    print(f"Ошибка: {resp.status_code}")
    print(resp.text)
import requests
from pprint import pprint

url = 'https://www.cbr-xml-daily.ru/latest.js'

result = requests.get(url)

result = result.json()

usd_course = result['rates']['USD']

user = float(input('Введи рубли: '))
print(f'В долларах: {user*usd_course}')
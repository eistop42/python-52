import json

# with open('db.json', 'w', encoding='utf-8') as file:
#     users = ['Алиса', 'Боб']
#     json.dump(users, file, ensure_ascii=False)

with open('db.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data[0] = 'Алиса 2'

with open('db.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)





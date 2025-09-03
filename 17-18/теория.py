# создание словаря

user = {'name': 'alisa', 'age': 20}

# получение данных
print(user['name'])
print(user['age'])

# добавление данных
user['friend'] = 'bob'
print(user)

#удаление
user.pop('friend')
print(user)

#перебор словаря
for key, value in user.items():
    print(key, value)


# список словарей

users = [{'name': 'alisa', 'age': 20},
         {'name': 'bob', 'age': 30}
         ]

for user in users:
    print(user['name'])
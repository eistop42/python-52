users = [{'name': 'alisa', 'age': 29}, {'name': 'bob', 'age': 40}]

for user in users:
    print(user['name'], user['age'])

username = input('введи имя: ')
age = int(input('введи возраст: '))

new = {'name': username, 'age': age}
users.append(new)

print(users)
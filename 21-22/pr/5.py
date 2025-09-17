users = [
    {"login": "alex123", "profile": {"name": "Алексей", "city": "Москва"}},
    {"login": "maria2025", "profile": {"name": "Мария", "city": "Казань"}}
]

while True:
    print('1 - добавить пользователя')
    print('2 - получить имя по логину')
    user = input('Выбирай: ')
    if user == '1':
        login = input('Логин: ')
        name = input('Имя: ')
        city = input('Город: ')

        user = {'login': login, 'profile': {'name': name, 'city': city}}

        users.append(user)

        print('Добавили пользователя')
        print(users)
    elif user == '2':
        print(users)
        login = input('Логин: ')

        for user in users:
            if user['login'] == login:
                print(f"Имя {user['profile']['name']}")
                break
        else:
            print('нет такого пользователя...')
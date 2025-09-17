
users = []
last_id = 0

while True:
    print('1 - добавить пользователя')
    print('2 - удалить по id')
    user = input('Выбирай: ')
    if user == '1':
        login = input('логин: ')
        password = input('пароль: ')
        last_id = last_id + 1
        user = {'login': login, 'password': password, 'id': last_id}
        users.append(user)

        print(f'Добавили {login}')
        print(users)
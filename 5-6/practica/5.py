login = input('введи логин')
passw = input('введи пароль')

login = login.lower()
if login == 'ilya' and passw == '123':
    print('верно')
else:
    print('неверно ')
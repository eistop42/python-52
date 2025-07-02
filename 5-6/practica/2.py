word = 'колобок'
user = input('введи букву: ')
res = word.count(user)

if res > 0:
    print('угадал')
else:
    print('не угадал')
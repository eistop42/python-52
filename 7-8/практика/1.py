word = 'колобок'

for i in range(5):
    print(f'Попытка №{i+1}')
    user = input('скажи букву:')
    res = word.count(user)

    if res > 0:
        print('такая буква есть')
    else:
        print('такой буквы нету')
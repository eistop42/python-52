library = [
    {"title": "Война и мир", "author": "Л. Толстой", "copies": 3},
    {"title": "Преступление и наказание", "author": "Ф. Достоевский", "copies": 2},
    {"title": "Мастер и Маргарита", "author": "М. Булгаков", "copies": 1}
]

while True:
    print('1 - взять книгу')
    print('2 - добавить книгу')
    user = input('Выбирай: ')
    if user == '1':
        # перебрать все книги, проверить наличие
        print(library)
        user_book = input('Введи название книги: ')
        print('начинаем поиск...')

        for book in library:
            if book['title'] == user_book:
                print('нашли книгу!')
                if book['copies'] > 0:
                    print('Выдали книгу')
                    book['copies'] -= 1
                else:
                    print('книги закончились...')
                break
        else:
            print('такой книги нет')

    elif user == '2':
        # добавить книгу
        name = input('Название: ')
        author = input('Автор: ')
        count = int(input('Количество'))

        book = {'title': name, 'author': author, 'copies': count}
        library.append(book)
        print('Книга добавлена!')
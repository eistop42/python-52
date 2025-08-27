products = []

while True:
    print('Выбери действие')
    print('1 - добавить товар')
    print('2 - выход')

    user = input('выбирай: ')
    if user == '1':
        product = input('Введи название товара: ')
        if product not in products:
            products.append(product.lower())
        else:
            print('такой товар уже есть')
        print(products)
    elif user == '2':
        break
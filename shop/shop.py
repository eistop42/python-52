from pprint import pprint

products = [
    {'name': 'Молоко', 'price': 80, 'count': 5},
    {'name': 'Хлеб', 'price': 50, 'count': 2},
]

def get_product(product_name, products):
    for product in products:
        if product['name'] == product_name:
            return product
    return None


while True:
    print('1-Добавить товар')
    print('2-Посмотреть товары')
    print('3-Купить товар')
    user = input('Выбирай: ')

    if user == '1':
        name = input('Название товара: ')
        count = int(input('Количество: '))

        # проверить, если товар в списке
        product = get_product(name, products)
        if product:
                # увеличиваем количество товаров
                product['count'] += count
                print('Товар добавлен!')
        else:
            # создаем товар
            price = int(input('Цена товара: '))
            new_product = {'name': name, 'count': count, 'price': price}
            products.append(new_product)

    elif user == '2':
        pprint(products)

    elif user == '3':
        name = input('Название товара: ')
        for product in products:
            if product['name'] == name:
                count = int(input('Количество: '))
                if product['count'] >= count:
                    print('Покупаем товар')
                    product['count'] -= count
                else:
                    print('Нет товара в таком количестве')
                break
        else:
            print('Такого товара нет')




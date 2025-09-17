# список словарей с товарами
products = [
    {"name": "Ноутбук", "price": 55000},
    {"name": "Смартфон", "price": 25000},
    {"name": "Планшет", "price": 18000}
]

# второй товар
print(products[1]['price'])
print(products[1]['name'])

# или с использованием переменной
product = products[1]
print(product['price'])
print(product['name'])
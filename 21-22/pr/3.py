products = [
    {"name": "Ноутбук", "details": {"weight": "2000", "color": "серый"}},
    {"name": "Смартфон", "details": {"weight": "180", "color": "черный"}},
    {"name": "Планшет", "details": {"weight": "400", "color": "белый"}}
]
# Дан  словарь словарей с товарами.
# Выведите вес и цвет третьего товара
# Выведите названия всех товаров
# Посчитайте суммарный вес всех товаров
print(products[2]['details']['weight'])
print(products[2]['details']['color'])

weight = 0
for product in products:
    print(product['name'])
    weight = weight + int(product['details']['weight'])

print(f'Суммарный вес: {weight}')
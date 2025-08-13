products = []

for i in range(3):
    product = input('Введи продукт: ')
    products.append(product)

print(products)
# вывод списка в одной строке через запятую
print(",".join(products))
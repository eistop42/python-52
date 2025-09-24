a = [1,2,3,4,5,5,3,1]
b = [2,3,1,7,7]

# уникальные элементы списка a и b
print(list(set(a)))
print(list(set(b)))

# общие элементы списков
c = set(a) & set(b)
print(list(c))

# элементы, которые есть только в a
res = list(set(a) - set(b))
print(res)
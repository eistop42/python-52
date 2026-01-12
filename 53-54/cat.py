from typing import Self

class Cat:
    def __init__(self, init_name):
        self.name = init_name
        self.sytost = 50
        self.PRODUCTS = {'молоко': 10, 'рыба': 20}
        self.friends = []

    def hello(self):
        print(f'Привет, меня зовут {self.name}!')

    def eat(self, product):
        if product in self.PRODUCTS.keys():
            self.sytost += self.PRODUCTS[product]
            print(f'Спасибо! Мой уровень сытости: {self.sytost}')
        else:
            print('я такое не ем...')

    def get_friend(self, cat: Self):
        if cat not in self.friends:
            # добавляем друга себе
            self.friends.append(cat)
            print(f'Добавил друга {cat.name}')
            # добавляем себя в друзья
            cat.friends.append(self)
        else:
            print('уже есть такой друг')

    def show_friends(self):
        print(f'Мои друзья: {self.friends}')


cat = Cat('Мурзик')
cat2 = Cat('Барсик')
cat.hello()
cat.eat('молоко')
cat.eat('картошка')
cat.get_friend(cat2)
cat.get_friend(cat2)
cat.show_friends()
cat2.show_friends()


class Animal():
    def __init__(self, name):
        self.name = name
        self.health = 10

    def walk(self):
        print('Я пошел гулять!')
        self.health += 5


class Dog(Animal):

    def test(self):
        pass

    def eat(self, name):
        if name in ['мясо', 'сухой корм']:
            self.health += 5
            print('Я поел')
        else:
            print('Я такое не ем')


class Cat(Animal):

    def eat1(self, name):
        if name in ['рыба']:
            self.health += 5
            print('Я поел')
        else:
            print('Я такое не ем')


dog = Dog('тузик')
cat = Cat('мурзик')

animals = [dog, cat]

for animal in animals:
    food_name = input(f'Покорми едой {animal.name}: ')
    animal.eat(food_name)
def hello():
    print('Привет!')

def hello2(name, age='', last_name=''):
    print(f'Привет, {name} {last_name} {age}')


def my_sum(number_1, number_2):
    res = number_1 + number_2
    return res

r = my_sum(3 ,4)
print(r)


def hello(name):
    return f'привет {name}'

print(hello('alisa'))
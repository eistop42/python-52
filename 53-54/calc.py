

def sum(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2


while True:
    number1 = int(input('Введи первое число: '))
    number2 = int(input('Введи второе число: '))
    action = input('Введи знак действия: +-')

    if action == '+':
        res = sum(number1, number2)
        print(f'Результат: {res}')

    elif action == '-':
        res = subtract(number1, number2)
        print(f'Результат: {res}')
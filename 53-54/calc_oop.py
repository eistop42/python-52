
class Calculator:
    def __init__(self, init_limit):
        self.operations = 0
        self.limit = init_limit

    def sum(self, number1, number2):
        if self.check_limit():
            self.operations += 1
            return number1 + number2
        raise ValueError('истекли операции')

    def subtract(self, number1, number2):
        if self.check_limit():
            self.operations += 1
            return number1 - number2
        raise ValueError('истекли операции')

    def check_limit(self):
        if self.operations < self.limit:
            return True
        return False


my_calc = Calculator(init_limit=2)

while True:
    number1 = int(input('Введи первое число: '))
    number2 = int(input('Введи второе число: '))
    action = input('Введи знак действия: +-')

    try:
        if action == '+':
            res = my_calc.sum(number1, number2)
            print(f'Результат: {res}')

        elif action == '-':
            res = my_calc.subtract(number1, number2)
            print(f'Результат: {res}')
    except ValueError:
        print('у тебя закончились операции...')
        break

    print(f'Количество операций: {my_calc.operations}')
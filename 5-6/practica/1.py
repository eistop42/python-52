# программа для угадаывания чисел
import random
answer = random.randint(1, 10)
print(f'он загадал {answer}')
number = int(input('введи число'))

if number == answer:
    print('Ты угадал')
else:
    print('не угадал((')
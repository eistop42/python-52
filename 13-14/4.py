import random

words_1 = ['красивый', 'мудрый']
words_2 = ['закат', 'код']
words_3 = ['единорога', 'вселенной']

# красивый закат вселенной
# мудрый код единорого
for i in range(3):
    w1 = random.choice(words_1)
    w2 = random.choice(words_2)
    w3 = random.choice(words_3)
    print(w1, w2, w3)
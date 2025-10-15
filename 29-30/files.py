import random as myrandom

f = open('hello.txt', 'w', encoding='utf-8')

f.write('привет \n')
f.write('пока')
f.write('пока123123')

f.close()
f.write('12333333')
#
# f = open('hello.txt', 'w', encoding='utf-8')
# # читаем все сразу
# # print(f.read())
# # читать построчно
# f.write('пока123123')
#
with open('hello.txt', 'r', encoding='utf-8') as f:
    res = f.readlines()

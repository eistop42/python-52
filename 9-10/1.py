word = 'караван'

count = 0
for i in range(7):
    letter = word[i]
    if letter == 'а':
        count += 1
        print(f'нашел на {i+1} позиции, всего {count}')
print(count)


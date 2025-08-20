string = 'в этом предложении пять слов'

# разделяем строку по пробелу
words = string.split(' ')
print(words)

# два способа подсчета длины списка

# функция len()
print(len(words))

# без использования дополнительных функций
count = 0
for word in words:
    print(word)
    count = count + 1
print(count)
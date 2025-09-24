s1 = 'пьврвщивввввеукт'
s2 = 'ййкзааввкдлдваелолфыa'

s = s1 + s2

for i in range(len(s)):
    if i % 3 == 0:
        print(s[i], end='')
numbers = [[1,2,-4], [6,-1,3], [-12,7,8], [12, -4, 5]]
res = []

for i in range(4):
    s = numbers[i]

    count = 0
    for number in s:
        if number > 0:
            count = count + number
    res.append(count)
print(res)
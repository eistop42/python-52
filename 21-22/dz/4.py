students = {
    'Аня': [5, 4, 5],
    'Борис': [3, 2, 3],
    'Вика': [10, 4, 4],
    'Дима': [2, 2, 3]
}

max_mark = {'name': '', 'mark': 0}
dvoeshniki = []

for name, marks in students.items():
    middle_mark = sum(marks)/len(marks)
    # сохранение максимальной средней
    if middle_mark > max_mark['mark']:
        max_mark['mark'] = middle_mark
        max_mark['name'] = name
    if 2 in marks:
        dvoeshniki.append(name)
    print(f'{name}, Средняя: {middle_mark:.2f}')

print(max_mark['name'], int(max_mark['mark']))
print(f'Двоечники: {",".join(dvoeshniki)}')

names = ['Алиса', 'Боб']
print('-'.join(names))
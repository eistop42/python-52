import json
# 1. Получить данные из базы
# 2. Показать первый вопрос и варинты ответов
# 3. Предложить ввести ответ пользователю
# 4. Если ответил верно - начислить балл
# 5. Если ответл неверно - показать правильный ответ
# 6. Если есть еще вопросы - задать. Если нет - показать сумму баллов


def get_questions():
    with open('db.json', encoding='utf-8') as f:
        questions = json.load(f)
    return questions


# 1. Получить данные из базы
questions = get_questions()
questions_list = questions['questions']
# 2. Показать первый вопрос и варинты ответов

count = 0
for question in questions_list:
    print(f'Вопрос: {question['question']}')

    for number, answer in enumerate(question['answers'], start=1):
        print(f'{number}.{answer}')

    user_answer = input('Введи ответ полностью: ')

    correct = question['correct_answer']

    if user_answer.capitalize() == correct:
        print('Верно')
        count += 1
    else:
        print(f'неправильно, ответ: {correct}')
print(f'Итог: {count}')
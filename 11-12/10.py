import random

questions = ['Столица России', 'Cтолица Франции']
answers = ['Москва', 'Париж']

quest = random.choice(questions)
user_answer = input(f'{quest}: ')

# нашли индекс вопроса
q_index = questions.index(quest)

# совпадает ли ответ по найденному индексу с ответом пользователя
if answers[q_index] == user_answer:
    print('Ответ верный!')
else:
    print('Ответ неверный')
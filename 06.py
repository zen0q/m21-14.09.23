question_1 = print ('Любите ли вы котиков?')
answer_1 = input('Введите ответ на первый вопрос:')
question_2 = print('Умеете ли вы программировать?')
answer_2 = input('Введите ответ на второй вопрос:')
if answer_1 == 'да' and answer_2 == 'да':
    print('Вы невероятны!')
elif answer_1 == 'нет' and answer_2 == 'нет':
    print('Вам стоит полюбить котиков и научиться программировать(')
elif answer_1 == 'да' and answer_2 == 'нет':
    print('У вас еще есть время научиться программировать!')
elif answer_1 == 'нет' and answer_2 == 'да':
    print('Зря вы так с котиками...')
else:
    print('Ошибка')
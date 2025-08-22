# Объявление переменных
score = 0
correct_answers = 0

# Запрос имени
print('''Тест на знание английского!
Прежде чем начать тест, пожалуйста, напишите свое имя.''')
user_name = str(input())
print()

# Вывод приветствия и условия выполнения заданий
print(f'Привет, {user_name}, начнём тестирование!')
print()

# Задание 1
print('''Задание №1.
Вставите пропущенное слово!
My name ___ Vova.''')
task_one = str(input())

# Результат ответа
if task_one == 'is':
    score += 10
    correct_answers += 1
    print('Ответ верный! Вы получаете 10 баллов!')
else:
    print('Неправильно. Правильный ответ: "is"')
print()

# Задание 2
print('''Задание №2.
Вставите пропущенное слово!
I ___ a coder.''')
task_two = str(input())

# Результат ответа
if task_two == 'am':
    score += 10
    correct_answers += 1
    print('Ответ верный! Вы получаете 10 баллов!')
else:
    print('Неправильно. Правильный ответ: "am"')
print()

# Задание 3
print('''Задание №3.
Вставите пропущенные слова!
I live ___ Moscow.''')
task_three = str(input())

# Результат ответа
if task_three == 'in':
    score += 10
    correct_answers += 1
    print('Ответ верный! Вы получаете 10 баллов!')
else:
    print('Неправильно. Правильный ответ: "in"')
print()

# Подсчёт правильных ответов в процентном соотношении
percent = round(float(correct_answers / 3) *100)

# Вывод результата
print(f'Вот и всё, {user_name}')
print(f'Количество верных ответов: {correct_answers}')
print(f'Ваш счёт: {score}')
print(f'Процент правильных ответов: {percent}%')
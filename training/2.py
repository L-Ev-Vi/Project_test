from pygments.lexer import words

# Приветствие и запрос имени
print("Привет! Это викторина по английскому языку. Тебе нужно заполнить пропущенные слова.")
print()
print("Как тебя зовут?")
name = input()
print()
print(f"Привет, {name} \nНачинаем тест! Всего 5 вопросов. Напиши 'stop', чтобы выйти.")
print()

# Создание списка вопросов и списка ответов
questions = [
    "My name ___ Vova.",    # Вопрос 1
    "I ___ a coder.",       # Вопрос 2
    "I live ___ Moscow.",   # Вопрос 3
    "She ___ from London.", # Вопрос 4
    "We ___ learning Python." # Вопрос 5
]
answers = ["is", "am", "in", "is", "are"]

# Объявление переменных
correct_answers = 0 #Счетчик правильных ответов
tеotal_score = 0 #Общий балл
attempts = 0 #Количество попыток

#Перебор вопросов
for  index, question in enumerate(questions):
    print(f"{index + 1} Вопрос \n{question}")
    print()
    answer = (input(f"Вставите пропущенные слово ->"))
#Проверка ввода
    if answer == "stop":
        break
    elif answer == str():
        continue
    elif answer == (answers[index]):
        print("Ответ верный! Вы получаете 10 баллов!")
        correct_answers += 1
        tеotal_score += 10
    else:
        print(f"Неверно. Правильно: {answers[index]}")
    attempts += 1
    print()

# Подсчёт правильных ответов в процентном соотношении
if attempts > 0:
    percent = (correct_answers / attempts) * 100
else:
    0

# Вывод результата
print(f"Итоги: \nВопросов: {len(questions)}")
print(f"Правильно: {correct_answers}")
print(f"Баллы: {tеotal_score}")
print(f"Процент: {round(float(percent))}%")

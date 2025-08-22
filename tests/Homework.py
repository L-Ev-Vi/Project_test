# Подготовка данных, создание словарей

#Легкие вопросы
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута"
}

#Средние вопросы
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать"
}

#Сложные вопросы
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме"
}

#Критерии оценки результатов
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}

#Создание функции
def choose_difficulty():
    """Запрашивает у пользователя уровень сложности и возвращает соответствующий словарь слов."""

    difficulty  = str(input("Выберите уровень сложности: легкий, средний, сложный. \n:").lower())
    if difficulty == "легкий":
        return words_easy
    elif difficulty == "сложный":
        return words_hard
    else:
        return words_medium


#Создание функции
def play_game(words):
    """Задаёт пользователю пять слов и сохраняет результаты ответов."""

    print("Выбран уровень сложности. Мы предложим 5 слов — подберите перевод.")
    print()
    answers = {}
    for key, value in words.items():
        answer = str(input(f"{key}, {len(value)} букв, начинается на {str(value[0])}... \n:").lower())
        print()
        if answer == value.lower():
            print(f"Верно. {key} — это {value}.")
            answers[key] = True
            print()
        else:
            print(f"Неверно. {key} — это {value}.")
            answers[key] = False
            print()
    return answers


#Создание функции
def display_results(answers):
    """Показывает, какие слова были переведены правильно, а какие — нет."""

    correct_words = []
    incorrect_words = []

    for key, value in answers.items():
        if value == True:
            correct_words.append(key)
        else:
            incorrect_words.append(key)
    print("Правильно переведенные слова:")
    print()
    for word in correct_words:
        print(word)
    print()
    print("Ошибки в словах:")
    print()
    for word in incorrect_words:
        print(word)


#Создание функции
def calculate_rank(answers):
    """Определяет ранг пользователя на основе количества правильных ответов."""

    correct_count = sum(answers.values())
    print()
    return f"Ваш ранг:\n{levels[correct_count]}"


words = choose_difficulty()
answers = play_game(words)
display_results(answers)
print(calculate_rank(answers))
print()
print("Завершение программы.")


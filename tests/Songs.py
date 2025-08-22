# Список песен в нашем музыкальном сервисе
songs = [
    {'title': 'Танцы под луной', 'artist': 'Катя Коста', 'genre': 'Поп'},
    {'title': 'Деньги не проблема', 'artist': 'MARAT', 'genre': 'Хип-хоп'},
    {'title': 'Рапсодия любви', 'artist': 'Антон Белов', 'genre': 'Поп'},
    {'title': 'Электрические Носороги', 'artist': 'Лиловый Бармалей', 'genre': 'Рок'},
    {'title': 'Первое правило улиц', 'artist': 'Централ', 'genre': 'Хип-хоп'},
]

# Предпочтения пользователя
user_genre = 'Поп'  # Пользователь предпочитает жанр «Поп»

# Функция для получения рекомендаций
def get_recommendations(songs, user_genre):
    recommendations = []  # Список для хранения рекомендаций

    for song in songs:
        if song['genre'] == user_genre:
            # Добавляем название песни и исполнителя в рекомендации
            recommendations.append(f"{song['title']} - {song['artist']}")

    return recommendations

# Получаем рекомендации
recommended_songs = get_recommendations(songs, user_genre)

# Выводим рекомендации
print("Мы рекомендуем вам послушать следующие песни:")
for title in recommended_songs:
    print("- " + title)
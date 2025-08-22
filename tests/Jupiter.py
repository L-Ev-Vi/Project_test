# %%
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

print("Coffe - ", 300)
print("Bun - ", 150)
print("Nutas - ", 200)
print("Result:", 300 + 150 + 200)
print("Tax:", (300 + 150 + 200) * 13 / 100)
# %%
water_daily = 3
days = 7

water_total = 3 * 7
print(water_total)
# %%
price = 50000
months = 10
type(price)
monthly_fee = float(price / months)
print(type(price))
print(monthly_fee)
# %%
total = int("20000")
tax_value = ("0.1")
x = float(tax_value)
tax_summ = float(total * x)

print(f"Налог на доход хитрых лиц с суммы 20000 составит {tax_summ}")

# %%
tax_value = float("0.1")
print(type(tax_value))
# %%
friends_counts = 5
print(type(friends_counts))
# %%
cookies_kg_price_str = "860"

cookies_kg_price_int = int(cookies_kg_price_str)  # цена за кг печенья
friends_counts = 5  # количество друзей
personal_fee = (cookies_kg_price_int / friends_counts)
personal_account = round(personal_fee)
print(f"Дорогой друг! Надеюсь, печенье понравилось, верни, пожалуйста, {personal_account} !")
# %%
print("Alfa \nBravo \nCharlie \nDelta \nEcho")
# %%
print("Alfa", "Bravo", "Charlie", "Delta", "Echo", sep="\n")
# %%
rhyme = ("""Дама сдавала в багаж
- Диван,
- Чемодан,
- Саквояж,
- Картину,
- Корзину,
- Картонку
И маленькую собачонку""")

print(rhyme)
# %%
print('"abstract type" – Абстрактный тип.')
print("access control – Управление доступом.
basic
type – Простой
тип.
# %%
messages_count = int(input())
if messages_count > 0:
    print("Есть новые сообщения")

if messages_count == 0:
    print()
# %%
residency = input()
salary = input()
experience = input()

residency_int = int(residency)
salary_int = int(salary)
experience_int = int(experience)

counter = 0

if residency_int >= 2:
    counter += 1

if salary_int >= 50000:
    counter += 1

if experience_int >= 2:
    counter += 1

print(f"Ваш кредитный рейтинг - {counter}")
# %%
luggage_weight = int(input())

if luggage_weight <= 5:
    print("Можно взять в салон")

if luggage_weight > 5:
    print("Нужно сдать в багаж")
# %%
# Получаем данные от пользователя
user_input = input()

# Проверяем первый вариант
if user_input == "bird":
    print("это птица")

# Проверяем второй вариант
if user_input == "plane":
    print("это самолет")

if user_input == user_input:
    print("")
# %%
first_number = int(input())
second_number = int(input())

if first_number == second_number:
    the_amounts_are_equal = True

if first_number != second_number:
    the_amounts_are_not_equal = False
the_amounts_are_equal = ("first_number == second_number")
the_amounts_are_not_equal = ("first_number != second_number")

the_amounts_are_equal = True
the_amounts_are_not_equal = False
print(type(the_amounts_are_not_equal))
# %%
first_number = int(input())
second_number = int(input())

if first_number == second_number:
    the_amounts_are_equal = True
print(the_amounts_are_equal)

if not first_number == second_number:
    the_amounts_are_not_equal = False
print(the_amounts_are_not_equal)
# %%
number = int(input())

remains = str(number % 10)
one = "1"

if remains in one:
    number_one = True
print(number_one)

if not remains in one:
    no_number_one = False
print(no_number_one)
# %%
number = int(input())

remains = str(number % 10)
print(remains)
# %%
deposit = int(input())
if deposit >= 500:
    print("Средств достаточно")
else:
    print("Средств недостаточно")
# %%
monday = input() == "True"
tuesday = input() == "True"
wednesday = input() == "True"
thursday = input() == "True"
friday = input() == "True"
saturday = input() == "True"
sunday = input() == "True"

# Начните писать код здесь

if monday == True:
    print("Понедельник")

if tuesday == True:
    print("Вторник")

if wednesday == True:
    print("Среда")

if thursday == True:
    print("Четверг")

if friday == True:
    print("Пятница")

if saturday == True:
    print("Субота")

if sunday == True:
    print("Воскресенье")
# %%
word = input()

has_r = "r" in word
has_l = "l" in word
has_s = "s" in word

print(f"Слово {word}")

if has_r:
    print("Есть буква R")
if has_l:
    print("Есть буква l")
if has_s:
    print("Есть буква s")
# %%
is_dark = bool(int(input()))
is_experience_less_1y = bool(int(input()))
is_raining = bool(int(input()))
is_driver_tired = bool(int(input()))

max_speed = 90

if is_dark == True:
    max_speed -= 20

if is_experience_less_1y == True:
    max_speed -= 10

if is_raining == True:
    max_speed -= 10

if is_driver_tired == True:
    max_speed -= 10

print(max_speed)
# %%
max_speed = 90
print(type(max_speed))
# %%
# Объявление переменных
score = 0
correct_answers = 0

# Запрос имени
user_name = str(input('''Тест на знание английского!
Прежде чем начать тест, пожалуйста, напишите свое имя.'''))

# Вывод приветствия и условия выполнения заданий
print(f'''Привет, {user_name}, начнём тестирование!'
В заданиях необходимо напечатать пропущенные слова!''')

# Задание 1
print('''Вопрос №1.
Вставите пропущенные слова!''')
task_one = str(input('My name ___ Evgenii.'))

# Результат ответа
if task_one == 'is':
    score += 10
correct_answers += 1
print('''Ответ верный!
    Вы получаете 10 баллов!''')
else:
print('Неправильно. Правильный ответ: is')

# Задание 2
print('''Вопрос №2.
Вставите пропущенные слова!''')
task_two = str(input('I ___ a coder.'))

# Результат ответа
if task_two == 'am':
    score += 10
correct_answers += 1
print('''Ответ верный!
    Вы получаете 10 баллов!''')
else:
print('Неправильно. Правильный ответ: am')

# Задание 3
print('''Вопрос №3.
Вставите пропущенные слова!''')
task_three = str(input(' I live ___ Moscow.'))

# Результат ответа
if task_three == 'in':
    score += 10
correct_answers += 1
print('''Ответ верный!
    Вы получаете 10 баллов!''')
else:
print('Неправильно. Правильный ответ: in')

# Подсчёт правильных ответов в процентном соотношении
percent = round(float(correct_answers / 3) * 100)

# Вывод результата
print(f'Вот и всё, {user_name}')
print(f'Количество верных ответов: {correct_answers}')
print(f'Ваш счёт: {score}')
print(f'Процент правильных ответов: {percent}%')

# %%
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print(letters[0:1] + letters[-4:-1])
# %%
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
          "декабрь"]

months_id = int(input())

print(months[months_id - 1])
# %%
timespans = ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13"]

n = int(input())

if n == 1:
    print(timespans[0])
elif n == 2:
    print(timespans[:2])
elif n == 3:
    print(timespans[:3])
elif n == 4:
    print(timespans[:4])
elif n == 5:
    print(timespans[:5])
else:
    print()

# %%
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', '-'
]

position = int(input())

print(alphabet[position:position + 1])
# %%
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
print(len(alphabet))

# %%
colors = ["красный", "оранжевый", "синий", "черный"]

del colors[0]

# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for color in colors:
    print(color)
# %%
my_list = [1, 2, 3, 4, 5, 3, 6]

# Ищем элемент 3, с индекса 3 до индекса 6 (не включая 6)
index = my_list.index(3, 3, 6)
print(index)

# %%
bool_boks = [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
num_random = int(input('Введите число:\n'))
kiflom = bool(bool_boks[num_random])
print(f'Это - {kiflom}')
# %%
num_random = int(input('Введите число: '))
num_random_bool = bool(num_random)
print(f'это - {num_random_bool}')
# %%
price = int(input('Введите полную сумму покупки'))

price_months = range(1, 13)

for one_month in price_months:
    payment = int(price / one_month)
print(f'{one_month} платеж — {payment}/ мес')
# %%
price = int(input('Введите полную сумму покупки'))

for month in range(1, 13):
    payment = int(price / month)
print(f'{month} платеж — {payment}/ мес')
# %%
fruits = ['яблоко', 'банан', 'груша']

# Создаем диапазон индексов от 0 до последнего элемента (длина списка - 1)
for index in range(len(fruits)):
# Получаем текущий индекс
    current_index = index

# Получаем значение элемента по текущему индексу
current_fruit = fruits[current_index]

# Выводим индекс и значение на экран
print(f'Индекс {current_index}: {current_fruit}')
# %%
for n in range(8):
    print(2 ** n)
# %%
x = 5
x_int = int(x)
for n in range(1, x_int, 1):
    print(n)
# %%
words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
         "Foxtrot", "Golf", "Hotel", "India", "Juliett",
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]

for word in range(len(words)):
    if
word < 5:
print(words[word])
# %%
words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
         "Foxtrot", "Golf", "Hotel", "India", "Juliett",
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]

print(words[-5:])

# %%
words = ["Alpha", "Bravo", "Charlie", "Delta", "Echo",
         "Foxtrot", "Golf", "Hotel", "India", "Juliett",
         "Kilo", "Lima", "Mike", "November", "Oscar",
         "Papa", "Quebec", "Romeo", "Sierra", "Tango",
         "Uniform", "Victor", "Whiskey", "X-ray", "Yankee",
         "Zulu"]

for word in range(len(words)):
    n = word - 5
if n <= -1:
    print(words[n])
# %%
weekdays = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
work = [True, True, True, True, True, False, False]
plans = ["за покупками", "отдыхать", "играть", "лениться", "гулять", "кутить", "страдать"]

for weekday in range(len(weekdays)):
    if
weekday <= 5:
work[weekday] = "это рабочий день"
print(f"{weekdays[weekday]} - {work[weekday]}, {plans[weekday]}.")
else:
work[weekday] = "это выходной день"
print(f"{weekdays[weekday]} - {work[weekday]}, {plans[weekday]}.")
# %%
debt = 10000

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
n = 0

while debt > 0:
    sum = int(input(f'{month[n]}. \nВаш долг - {debt}руб. \nВнесите сумму'))
    print(f'Вы внесли {sum}')
    debt -= sum
    n += 1
    if n == len(month):
        n = 0

print('Ваши долги выплачены')

# %%
deposit = 0
replenishment = int(input())

while deposit <= 12000:
    deposit += replenishment
    if deposit <= 12000:
        print(f"Баланс счета = {deposit}")

# %%
day = 1
distance = 2.0

while distance < 5:
    day += 1
    distance = float(distance * 1.2)
    if distance >= 5:
        print(day)
# %%
expenses = 0
while True:
    number = input()
    if number == "стоп":
        print(expenses)
        break
    int_number = int(number)
    expenses += int_number
# %%
words = ["int", "pk", "get", "round", "id", "if"]

for word in words:
    n = len(word)
    # Допишите код тут
    if n > 2:
        print(word)  # Не меняйте эту строку
# %%
fruits = ["яблоко", "банан", "груша", "клубника"]

for index, fruit in enumerate(fruits):
    print(f"Индекс {index}: {fruit}")
# %%
sample = "маленькая змея Василиса говорит «с-с-с-с»!"
print(sample[4:9:200])
# %%
# Вариант 1
word_1 = 'Custom'
word_2 = 'Automatic'
word_3 = 'Transport'

one = word_1[0]
two = word_2[0]
three = word_3[0]

print(one, two, three, sep='')

# Вариант 2
word_1 = 'Custom'
word_2 = 'Automatic'
word_3 = 'Transport'

print(f'{word_1[0]}{word_2[0]}{word_3[0]}')

# Вариант 3
word_1 = 'Custom'
word_2 = 'Automatic'
word_3 = 'Transport'

print(word_1[0] + word_2[0] + word_3[0])

# Вариант 4
word_1 = 'Custom'
word_2 = 'Automatic'
word_3 = 'Transport'

print(word_1[0] + word_2[0] + word_3[0], end=" — для чего здесь параметр 'end'? \n")

# Вариант 5
word_1 = 'Custom'
word_2 = 'Automatic'
word_3 = 'Transport'

print(word_1[0], end="")
print(word_2[0], end="")
print(word_3[0], end=" — вот для чего здесь параметр 'end'!")

# %%
string = "Длина катапульты определяется ускорением, которого мы хотим достигнуть."

letters_count = 0
words_count = 0
space_count = 0

for letter in string:
    if letter not in [",", ".", " ", "!", "?"]:
        letters_count += 1
    elif letter in " ":
        space_count += 1

if space_count > 1:
    words_count = space_count + 1
else:
    words_count = 1

print(f"Буквы: {letters_count}")
print(f"Слова: {words_count}")
# %%
word = input()
symbols = str("*")
for symbol in word:
    print(symbols * len(word))
    break

# %%
line = "STRINGS ARE AWESOME"

for letter in line:
    if letter != " ":
        print(letter, end="")
# %%
word = "0"
word_int = int(word)

n = str(bool(word_int))
print(n)
# %%
sfg = "пос с сор"

sfg_1 = sfg.replace("с", "s")

print(sfg_1)
# %%
code = "Echo Sierra Charlie Alfa Papa Echo"
cod = ""

list_code = code.title().split()

for codi in list_code:
    cod += codi[0]

print(cod)
# %%
numbers = "2 3 4 5"

int_numbers = []

list_numbers = numbers.split()

for number in list_numbers:
    int_numbers.append(int(number))

int_numbers.sort()

print(f"min: {int_numbers[0]} \nmax: {int_numbers[-1]}")
# %%
text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []

list_text = text.split(" ")
for word in list_text:
    if word.isalpha():
        just_words.append(word)

text_cleaned = " ".join(just_words)

print(text_cleaned)
# %%
interpreter = {"cat": "Кошка", "dog": "Собака", "owl": "Сова"}

word = input("Введите слово —>")

print(interpreter[word])
# %%
dictionary = {"яблоки": 100, "груши": 200, "ананас": 300}

fruits = input("Выберите фрукт: —>")
fruits_lower = fruits.lower()

for fruit in store:
    if fruit == fruits_lower:
        weight = float(input("Укажите вес в граммах"))
        price = float(weight * dictionary[fruit] / 1000)
        print(f'Цена: {price} денег')
# %%
guests = {"Алексей": 1000, "Даша": 5000}

print(", ".join(guests.keys()))

v_sum = 0
for v in guests.values():
    v_sum += v
print(f"Того: {v_sum}")
# %%
text = "The quick brown fox jumps over the lazy dog"


def text_length():
    text_replace = text.replace(" ", "")
    print(len(text_replace))


text_length()


# %%
def calculate_product_cost(**kwargs):
    price_per_unit = None
    quantity = None
    if len(kwargs) <= 2:
        return None
    else:
        for key, value in kwargs.items():
            if key == "price_per_unit":
                price_per_unit = float(value)
            elif key == "quantity":
                quantity = value
        return quantity * price_per_unit


print(calculate_product_cost(product_name="Лампочки", price_per_unit=1.5, quantity=10))
print(calculate_product_cost(product_name="Песок", price_per_unit=0.5, quantity=130))
print(calculate_product_cost(product_name="Картошка", price_per_unit=5.5, quantity=159))
print(calculate_product_cost(product_name="Лампочки", price_per_unit=1.5))
print(calculate_product_cost())


# %%
def calculate_product_cost(product_name=None, price_per_unit=None, quantity=None):
    if price_per_unit and quantity:
        return price_per_unit * quantity
    else:
        return None


print(calculate_product_cost(product_name="Лампочки", price_per_unit=1.5, quantity=10))
print(calculate_product_cost(product_name="Песок", price_per_unit=0.5, quantity=130))
print(calculate_product_cost(product_name="Картошка", price_per_unit=5.5, quantity=159))
print(calculate_product_cost(product_name="Лампочки", price_per_unit=1.5))
print(calculate_product_cost())
T
# %%
is_even = lambda x: bool(x % 2 - 1)

print(is_even(5))
print(is_even(3))
print(is_even(20))
print(is_even(11))

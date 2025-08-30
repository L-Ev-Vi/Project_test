def sort_the_same_values(list_one: list[int], list_tow: list[int]) -> list:
    """Принимает два списка
    и возвращает новый список содержащий одинаковые значения
    из первого и второго списка."""
    now_list = list((set(list_one)).intersection(set(list_tow)))
    return now_list


def define_a_palindrome(list_one: list[int]) -> list[int]:
    """Функция, получает на вход список чисел
    и возвращает новый список, содержащий только числа,
    которые являются палиндромами."""
    now_list = []
    for number in list_one:
        number_reverse = int(str(number)[::-1])
        if number == number_reverse:
            now_list.append(number_reverse)
    return now_list


def different_list_items(list_one: list[int], list_tow: list[int]) -> list[int]:
    """Функция, получает на вход два списка чисел
    и возвращает новый список, содержащий только те числа,
    которые есть только в одном из списков."""
    now_list_a = set(set(list_one).difference(set(list_tow)))
    now_list_b = set(set(list_tow).difference(set(list_one)))
    now_list = list(now_list_a.union(now_list_b))
    return now_list


# print(different_list_items([1, 2, 3, 4], [3, 4, 5, 6]))


def different_list(list_one: list[int], list_tow: list[int]) -> list[int]:
    """Функция, получает на вход два списка чисел
    и возвращает новый список, содержащий только те числа,
    которые есть только в одном из списков."""
    return list(set(list_one) - set(list_tow)) + list(set(list_tow) - set(list_one))



assert (different_list([1, 2, "fvfvv", 4], [3, 4, 25515, 6]))

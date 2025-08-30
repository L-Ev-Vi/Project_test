from typing import Any


def add(a: Any, b: Any) -> Any:
    """Складывает два числа"""
    return a + b


x = "./students.txt"


def red(x: str) -> str:
    with open(x, "a", encoding="utf-8") as file:
        file.write("super_men\n")
    with open(x, "r", encoding="utf-8") as file:
        return file.read()


def print_a_line() -> str:
    """Выводит строку 'Привет'."""
    return "Привет"


if __name__ == '__main__':
    assert add(145.58887, 5)

import math


def calculate_logarithm(a, b):
    if a <= 0 or b <= 1:
        raise ValueError('Число не должно быть меньше 0')
    return math.log(a, b)


def reverse_list(ma_list):
    return ma_list[::-1]


if __name__ == '__main__':
    print(calculate_logarithm(0, 2))

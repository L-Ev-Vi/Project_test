from typing import Any


def add(a: Any, b: Any) -> Any:
    """Складывает два числа"""
    a += b
    return a


x = "./students.txt"


def red(x: str) -> str:
    with open(x, "a", encoding="utf-8") as file:
        file.write("super_men\n")
    with open(x, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    print(red(x))


def print_a_line() -> Any:
    """Выводит строку 'Привет'."""
    return "Привет"

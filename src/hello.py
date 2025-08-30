from typing import Callable

__package__ = "src"


from .add import add, print_a_line


def hello(func: Callable) -> None:
    """Выводит строку Hello, World
    и число"""
    x = func
    print(f"Hello, World {x}")


# if __name__ == "__main__":
#     hello(add(2, 4))


def greeting(fun: Callable) -> None:
    """Выводит слова приветствия."""
    print(fun)
    print("Друг")

def add_plys(a: int, b: int) -> int:
    return a+b


# greeting(print_a_line())

assert greeting(add_plys(4,5))
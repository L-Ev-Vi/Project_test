from typing import Callable

__package__ = "src"

# from .add import add, print_a_line


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


# greeting(print_a_line())

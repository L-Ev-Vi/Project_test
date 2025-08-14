from src.add import add, print_a_line
from src.hello import greeting, hello

hello(add(1, 2))

greeting(print_a_line())

from src.foo import get_information_about_the_circle

r = float(input("Enter circle radius (int): "))
"""Запрашивает значение радиуса круга"""
get_information_about_the_circle(r)

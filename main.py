import os

from src.add import add, print_a_line
from src.foo import editing_the_list, editing_the_list_by_languages_and_alphabets
from src.hello import greeting, hello

a = 1
b = 2
hello(add(a, b))

greeting(print_a_line())

print("Hello, World")

file_path = os.path.join(os.path.dirname(__file__), "data", "names.txt")

editing_the_list_by_languages_and_alphabets(file_path)

import pytest

from src.file1 import factorial

def test_factorial(number):
    assert factorial(number) == 3628800
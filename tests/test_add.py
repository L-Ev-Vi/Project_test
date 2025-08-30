import pytest


@pytest.fixture
def ma_list():
    return [[1, 2, 3, 4, 5, 6], ['Python', 'easy'], [True, True, False, False]]



from src.add import add, calculate_logarithm, reverse_list


def test_add():
    assert add(4, 5)
    assert add(155.5, 20)


def test_zero_add():
    assert add(1, 0)


def test_calculate_logarithm():
    with pytest.raises(ValueError) as file:
        calculate_logarithm(0, 2)


@pytest.mark.parametrize('ma_str, rev_str', [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("12345", "54321"),
    ("", "")])
def test_reverse_list(ma_str, rev_str):
    assert reverse_list(ma_str) == rev_str

"""Напишіть тести з використанням pytest, які:
• перевіряють коректний поділ,
• перевіряють викидання виключення ZeroDivisionError, якщо знаменник дорівнює нулю.
Додайте тест із параметризацією для перевірки поділу з різними значеннями."""


import pytest
from divide import divide


# Test for correct division
def test_divide_correct():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(-8, 4) == -2.0


# Test for checking ZeroDivisionError
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="The denominator cannot be zero"):
        divide(10, 0)


# Parameterised test to check division with different values
@pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (-8, 4, -2.0),
        (0, 5, 0.0),
        (100, 25, 4.0),
])

def test_divide_parametrized(a, b, expected):
    assert divide(a, b) == expected

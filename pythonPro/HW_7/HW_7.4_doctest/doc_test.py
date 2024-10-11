"""Завдання 4. Тестування з використанням doctest
Додайте документацію з прикладами використання та напишіть тести з використанням doctest.
Напишіть функції для роботи з числами:
• is_even(n: int) -> bool: перевіряє, чи є число парним.
• factorial(n: int) -> int: повертає факторіал числа.
Додайте doctest-приклади для кожної функції.
Переконайтеся, що doctest проходить для кожної функції запустивши тести через python -m doctest."""


def is_even(n: int) -> bool:
    """
    Checks if the number is even.

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(0)
    True
    >>> is_even(-4)
    True
    >>> is_even(-3)
    False
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calculates the factorial of a number.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    >>> factorial(10)
    3628800
    >>> factorial(-1)  # The factorial for negative numbers is not defined.
    Traceback (most recent call last):
    ValueError: The factorial is defined only for non-negative numbers.
    """
    if n < 0:
        raise ValueError("The factorial for negative numbers is not defined.")
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n

"""Завдання 5. Тестування винятків у pytest (опціонально)
Напишіть функцію divide(a: int, b: int) -> float, яка поділяє два числа.
Якщо знаменник дорівнює нулю, функція повинна викидати виняток ZeroDivisionError."""


def divide(a: int, b: int) -> float:
    """Divides two numbers."""

    # Throwing a ZeroDivisionError if the denominator is zero.
    if b == 0:
        raise ZeroDivisionError("The denominator cannot be zero.")
    return a / b
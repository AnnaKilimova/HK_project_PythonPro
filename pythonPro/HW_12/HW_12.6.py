"""Завдання 6. Перевірка валідності пароля
Напишіть функцію, яка перевіряє, чи є пароль надійним. Пароль вважається надійним, якщо він:
містить як мінімум 8 символів,
містить принаймні одну цифру,
має хоча б одну велику літеру та одну малу,
містить хоча б один спеціальний символ (@, #, $, %, &, тощо)."""

import re


def is_strong_password(password):
    # Checking that the password is at least 8 characters long.
    if len(password) < 8:
        return False

    # Checking that the password contains at least one digit.
    if not re.search(r"\d", password):
        return False

    # Checking that the password contains at least one capital letter.
    if not re.search(r"[A-Z]", password):
        return False

    # Checking that the password contains at least one lowercase letter.
    if not re.search(r"[a-z]", password):
        return False

    # Checking that the password contains at least one special character.
    if not re.search(r"[@#$%&]", password):
        return False

    # If all checks pass, return True.
    return True


# An example of using the function.
password = "StrongPass1@"
if is_strong_password(password):
    print("Пароль надійний.")
else:
    print("Пароль не відповідає вимогам.")

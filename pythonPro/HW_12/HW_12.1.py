"""Завдання 1. Перевірка валідності email
Напишіть функцію, яка перевіряє, чи є email-адреса валідною. Email вважається валідним,
якщо він має формат example@domain.com, де:
example — послідовність з букв, цифр або точок (але точка не може бути на початку або в кінці).
domain — послідовність з букв або цифр.
.com, .net, .org тощо — домен верхнього рівня (TLD) довжиною від 2 до 6 символів."""

import re


def is_valid_email(email):
    # Regular expression for email validation.
    pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"
    # ^[a-zA-Z0-9]+: The address starts with letters or numbers. + means that the characters must be repeated one or more times.
    # (\.[a-zA-Z0-9]+)*: Allows a period (.) within the username, but only between letters/numbers.
    # An asterisk * means that this part may be missing or repeated several times.
    # @[a-zA-Z0-9]+: The @ symbol must be followed by one or more letters or numbers (domain name).
    # \.[a-zA-Z]{2,6}$: A top-level domain (TLD) that starts with a dot and contains 2 to 6 letters (e.g. .com, .org, .net).

    # Performing the check with re.match.
    return bool(re.match(pattern, email))


# Examples of use
emails = [
    "example@domain.com",  # valid
    "user.name@domain.net",  # valid
    ".username@domain.com",  # invalid (starts with a dot)
    "username@domain",  # invalid (no TLD)
    "username@domain.c",  # invalid (too short TLD)
    "username@domain.comm",  # invalid (too long TLD)
    "user@domain.org",  # valid
]

for email in emails:
    print(f"{email} -> {'Валідний' if is_valid_email(email) else 'Невалідний'}")

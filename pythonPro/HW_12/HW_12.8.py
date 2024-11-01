'''Завдання 8. Перевірка на наявність шаблону в тексті
Напишіть функцію, яка перевіряє, чи міститься у тексті рядок формату AB12CD34,
де A, B, C, D — великі літери, а 1, 2, 3, 4 — цифри.'''

import re


def contains_pattern(text):
    # Template for searching a string of format AB12CD34
    pattern = r'\b[A-Z]{2}\d{2}[A-Z]{2}\d{2}\b'
    # \b - limits the pattern at the word boundary to avoid partial matches.
    # [A-Z]{2} - corresponds to two capital letters of the Latin alphabet.
    # \d{2} - matches two digits.
    # [A-Z]{2} - again matches two capital letters.
    # \d{2} - ends the pattern with two digits.

    # Search for a pattern in the text.
    match = re.search(pattern, text)

    # If a match is found, return True, otherwise False
    return bool(match)


# An example of using the function.
text1 = "Приклад рядка AB12CD34, який відповідає шаблону."
text2 = "Рядок не має потрібного формату."

print(contains_pattern(text1))  # Expected result: True
print(contains_pattern(text2))  # Expected result: False

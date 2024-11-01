"""Завдання 2. Пошук телефонних номерів
Напишіть функцію, яка знаходить усі телефонні номери в тексті. Номери можуть бути в форматах:
(123) 456-7890
123-456-7890
123.456.7890
1234567890"""

import re


def find_phone_numbers(text):
    # Regular expression to search for phone numbers.
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    # \(?\d{3}\)?: Searches for three digits that can be surrounded by brackets (). The \(? character means that the
    # open bracket is optional, and \)? means that the closed bracket is also optional.
    # [-.\s]?: Allows one optional separator after three digits. It can be a hyphen (-), a period (.), or a space (\s).
    # \d{3}: The second group of three digits (for example, 456).
    # [-.\s]?: Allows one optional separator after the second group of digits.
    # \d{4}: The last group of four digits (for example, 7890).

    # Search for all phone numbers in a text.
    phone_numbers = re.findall(pattern, text)
    return phone_numbers


# Example text to search for.
text = """
Будь ласка, зв'яжіться з нами за номерами:
(123) 456-7890, 123-456-7890, 123.456.7890 або 1234567890.
А також, можна звертатись на додаткові номери: 987.654.3210 чи (555)123-4567.
"""

# Call the function and display the found numbers.
found_numbers = find_phone_numbers(text)
print("Знайдені телефонні номери:", found_numbers)

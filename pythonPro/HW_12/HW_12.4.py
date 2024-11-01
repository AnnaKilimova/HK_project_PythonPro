'''Завдання 4. Форматування дати
Напишіть функцію, яка перетворює дати з формату DD/MM/YYYY у формат YYYY-MM-DD.'''

import re


def reformat_date(date_text):
    # Template for DD/MM/YYYYY format.
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    # \d{2}: Finds a two-digit number (day or month).
    # /: Looks for the / character separating the day, month and year.
    # \d{4}: Searches for a four-digit number (year).
    # Brackets () are used to create groups so that you can reorder them.

    # Replace the date with the format YYYY-MM-DD.
    formatted_text = re.sub(pattern, r'\3-\2-\1', date_text) # Replacement in the order of \3-\2-\1 (year\month\day).
    return formatted_text


# An example of using the function
text = "Дата народження: 12/04/2023, дата зустрічі: 05/11/2024."
formatted_text = reformat_date(text)
print("Текст з відформатованими датами:", formatted_text)

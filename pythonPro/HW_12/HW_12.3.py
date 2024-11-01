"""Завдання 3. Видобування хеш-тегів з тексту
Напишіть функцію, яка з тексту повертає список хеш-тегів. Хеш-тег — це слово, що починається з #,
і може включати лише букви та цифри."""

import re


def extract_hashtags(text):
    # Regular expression for hashtags.
    pattern = r"#\w+"
    # #: Looks for the # character at the beginning of the hashtag.
    # \w+: Searches for a sequence of one or more characters consisting of letters, numbers, or an underscore (_).
    # \w considers underscores to be part of a word.

    # Search for all hashtags in the text.
    hashtags = re.findall(pattern, text)
    return hashtags


# Example text for hashtag search.
text = """
Це приклад тексту з хештегами #Python, #AI2024, #DataScience та #MachineLearning. 
Також, хештеги можуть бути в середині речення, наприклад, як #Example.
"""

# Call the function and display the found hashtags.
found_hashtags = extract_hashtags(text)
print("Знайдені хештеги:", found_hashtags)

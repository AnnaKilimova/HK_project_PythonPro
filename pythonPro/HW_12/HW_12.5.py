'''Завдання 5. Видалення HTML-тегів
Напишіть функцію, яка видаляє всі HTML-теги з тексту.'''

import re

def remove_html_tags(text):
    # Regular expression to find HTML tags.
    pattern = r'<.*?>'
    # <  > define the boundaries of an HTML tag.
    # .*? searches for any characters within the tag.
    # ? to find the shortest match, ending with the first >, which allows to delete one tag at a time.

    # Remove all HTML tag matches from the text.
    clean_text = re.sub(pattern, '', text)
    return clean_text

# An example of using the function.
html_text = "<p>Hello, <b>World!</b> It's <a href='#'>a link</a>.</p>"
cleaned_text = remove_html_tags(html_text)
print("Текст без HTML-тегів:", cleaned_text)

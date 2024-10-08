'''У файлі string_utils.py реалізуй функції для:
• Перетворення тексту в верхній регістр.
• Видалення пробілів на початку та в кінці рядка.'''

my_str = '  my cat is the best  '
def uppercase_func(text):
    '''
    Converts text to uppercase.
    :param text: str.
    :return: str.
    '''
    return text.upper()

def remove_gaps(text):
    '''
    Delete text at the beginning and end of a string.
    :param text: str.
    :return: str.
    '''
    return text.strip()

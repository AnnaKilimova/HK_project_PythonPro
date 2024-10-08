"""Завдання 1: Built-in область видимості (демонстрація використання
   вбудованих функцій та їх перекриття локальними функціями)."""


# 1. Написати функцію my_sum, яка перекриває вбудовану функцію sum.
#    Функція повинна просто виводити повідомлення:
#    "This is my custom sum function!".
def my_sum(*args):
    """For a local function to overlap an embedded one, it must also be
    called the same (sum),  but the task is ambiguous"""
    print('This is my custom sum function!')


# 2. Створити список чисел і викликати вбудовану функцію sum,
#   щоб підсумувати значення списку.
my_list = [1, 2, 3]
print(sum(my_list))  # 6

# 3. Викликати свою функцію my_sum,
my_sum()  # This is my custom sum function!

# а потім ще раз спробувати скористатися вбудованою функцією sum."""
# Question_1. Що відбувається, коли локальна функція має те саме ім'я, що й вбудована?
# • кожен виклик цієї функції адресован до локальної версії, а не до вбудованої.

# 2. Як можна отримати доступ до вбудованої функції, навіть якщо вона перекрита?
# • через модуль builtins який містить всі вбудовані функції
import builtins

print(builtins.sum((1, 2, 3)))  # 6

"""Завдання 9: Кешування результатів функції
Написати програму для кешування результатів функції, щоб покращити продуктивність.
1. Створити функцію memoize, яка приймає функцію та повертає
   нову функцію, що зберігає результати викликів.
2. Використати цю функцію, щоб кешувати результати обчислень
   (наприклад, факторіал або фібоначі)."""


def memoize(func):
    cache = {}

    def inner(*args):
        if args in cache:
            print(f"Cash for {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return inner


@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(0))
print(factorial(2))
print(factorial(3))

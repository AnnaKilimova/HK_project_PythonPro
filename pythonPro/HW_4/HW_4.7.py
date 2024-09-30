'''Завдання 7: Декоратор для логування викликів методів
Реалізуйте декоратор log_methods, який додається до класу і логуватиме виклики всіх його методів
(назва методу та аргументи).'''

def log_methods(cls):
    """
    Decorator
    :param cls: MyClass
    """
    # Bypassing all class attributes
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)

        # And check if it is a callable method and if it is not a special one
        if callable(attr) and not attr_name.startswith("__"):
            # Wrapping a method in a decorator that will log calls
            setattr(cls, attr_name, wrapper(attr))

    return cls


def wrapper(method):
    """
    Wrapper for log_methods decorator
    :param method: add || subtract
    """

    def inner(self, a, b):
        # Logging the method name and arguments
        """
        :param self: MyClass
        :param a: int
        :param b: int
        :return: add || subtract
        """
        print(f"Logging: {method.__name__} called with {a, b}")
        return method(self, a, b)

    return inner


@log_methods
# Test class
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)

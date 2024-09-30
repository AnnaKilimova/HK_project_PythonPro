'''Завдання 2: Динамічний виклик функцій
Реалізуйте функцію call_function(obj, method_name, *args), яка приймає об'єкт,
назву методу в вигляді рядка та довільні аргументи для цього методу.
Функція повинна викликати відповідний метод об'єкта і повернути результат.'''

def call_function(obj, method_name, *args):
    """
    A function that takes an object, a method name, arguments for this method,
    and call the corresponding object method and return the result
    :method_name: str
    :*args: int
    """

    # Get the method of the object
    selected_method = getattr(obj, method_name)

    # Call the method with the passed arguments and return the result
    return selected_method(*args)


class Calculator:
    """Represent an example class with 'add' and 'subtract' methods"""

    def add(self, a, b):
        """
        Class method
        :a: int
        :b: int
        :return: int
        """
        return a + b

    def subtract(self, a, b):
        """
        Class method
        :a: int
        :b: int
        :return: int
        """
        return a - b


# An instance of the class 'Calculator'
calc = Calculator()

# Pass an instance of the class ‘Calculator’ to the ‘call_function’ function
print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5

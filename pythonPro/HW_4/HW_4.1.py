'''Завдання 1: Перевірка типів і атрибутів об'єктів
Напишіть функцію analyze_object(obj), яка приймає будь-який об'єкт та виводить:
Тип об'єкта & Список всіх методів та атрибутів об'єкта & Тип кожного атрибута.'''

def analyze_object(obj):
    """
    The analyse_object(obj) function that accepts any object and outputs the type of the object,
    a list of all methods and attributes of the object, the type of each attribute.
    """

    # Print the type of object
    print(f"Object type is {type(obj)}")

    for item in dir(obj):
        # Get the value of an attribute/method
        attr_value = getattr(obj, item)
        # Print the name&type of the attribute/method
        print(f"{item}: {type(attr_value)}")


class MyClass:
    """Represent an example class with a value"""

    def __init__(self, value):
        """
        Initialize the MyClass instance with value.
        :type value: str
        """
        self.value = value

    def say_hello(self):
        """
        Class method
        :return: str
        """
        return f"Hello, {self.value}"


# An instance of the class 'MyClass' to be analysed
obj = MyClass("World")
# Pass an instance of the class 'MyClass' to the 'analyze_object' function
analyze_object(obj)

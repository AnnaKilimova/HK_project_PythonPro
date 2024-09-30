'''Завдання 4: Створення класу динамічно
Напишіть функцію create_class(class_name, methods), яка створює клас з заданим іменем та методами.
Методи передаються у вигляді словника, де ключі — це назви методів, а значення — функції.'''

def create_class(class_name, methods):
    """
    The function that creates a Class with a given name and methods.
    :param class_name: str
    :param methods: dict
    :return: new class
    """
    return type(class_name, (object,), methods)


# Functions for methods
def say_hello(self):
    return "Hello!"


def say_goodbye(self):
    return "Goodbye!"


# Methods for Class
methods = {"say_hello": say_hello, "say_goodbye": say_goodbye}

# Create the class
MyDynamicClass = create_class("MyDynamicClass", methods)

# An instance of the class 'MyDynamicClass'
obj = MyDynamicClass()

print(obj.say_hello())  # Hello!
print(obj.say_goodbye())  # Goodbye!

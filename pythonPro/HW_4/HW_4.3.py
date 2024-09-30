'''Завдання 3: Інспекція модулів
Напишіть програму, яка приймає на вхід назву модуля (рядок) та виводить список усіх класів,
функцій та їхніх сигнатур у модулі. Використовуйте модуль inspect.'''

import inspect


def analyze_module(module_name):
    """
    Function to display a list of all classes, functions and their signatures in the module.
    :param module_name: str
    :return:
    """
    try:
        # Importing a module
        module = __import__(module_name)
    except ImportError:
        # ImportError if the 'module_name' is not found.
        print(f"Module {module_name} is not found")
        return

    # Create lists for adding classes and module functions
    functions = []
    classes = []

    # Add items to the function and class lists respectively
    for name, member in inspect.getmembers(module):
        if inspect.isfunction(member):
            # Add functions to the 'functions' list
            func = str(inspect.signature(member))
            functions.append(f"- {name}{func}")
        elif inspect.isclass(member):
            # If there are no functions, add classes
            classes.append(f"- {name}")

    # Print the list of functions
    if functions:
        print("Functions:")
        for function in functions:
            print(function)
    else:
        print("No functions in the module")

    # Print the list of classes
    if classes:
        print("Classes:")
        for cls in classes:
            print(cls)
    else:
        print("No classes in the module")


# Testing
analyze_module("math")
analyze_module("acos(x)")
analyze_module("asin(x)")
analyze_module("atan(x, y)")
analyze_module("os")

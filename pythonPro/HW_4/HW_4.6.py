'''Завдання 6: Інтерсепція методів класу (Proxy)
Напишіть клас Proxy, який приймає на вхід об'єкт і переадресовує виклики методів цього об'єкта,
додатково логуючи виклики (наприклад, виводячи назву методу та аргументи).'''

class Proxy:
    """
    the Proxy class, which accepts an object as an input and redirects calls to
    the methods of this object, additionally logging calls
    """

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        # Get an attribute or method from the original object
        orig_attr = getattr(self._obj, name)

        def method(*args):
            # Log a method call
            print(f"Calling method: \n{name} with args: {args}")
            # Call the original method
            return orig_attr(*args)

        return method

# Test class
class MyClass:
    def greet(self, name):
        return f"Hello, {name}!"


# An instance of the class 'MyClass'
obj = MyClass()
# An instance of the class 'Proxy'
proxy = Proxy(obj)

print(proxy.greet("Alice"))

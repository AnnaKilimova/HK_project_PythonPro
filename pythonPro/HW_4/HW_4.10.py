"""Завдання 10: Метаклас для контролю створення класів
Реалізуйте метаклас SingletonMeta, який гарантує, що клас може мати лише один екземпляр (патерн Singleton).
Якщо екземпляр класу вже створений, наступні виклики повинні повертати той самий об'єкт."""


class SingletonMeta(type):
    """
    The metaclass, which guarantees that a class can have only one instance
    :param _instances: used to store instances of classes that have already been created.
     Cache for objects, to ensure that the same class has only one instance of it
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Controls the creation of instances of the class. When creating new instances, it checks if
        there is an existing object in the _instances dictionary.
        """
        # If the class instance has not yet been created, create it
        if cls not in cls._instances:
            # super(SingletonMeta, cls): returns a reference to the parent class type.
            # __call__: calls the __init__ method passing *args and **kwargs arguments to it.
            # As a result, a new object of class cls is created.
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        # Returning an existing instance
        return cls._instances[cls]

# Test class with metaclass SingletonMeta
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()  # The __call__ method of the SingletonMeta metaclass checks
# if there is already an instance for the Singleton class.
# Since there is no instance yet, the metaclass calls super(SingletonMeta, cls).__call__(*args, **kwargs) -
# new instance of the Singleton class is created via the standard mechanism.
# The instance is stored in the _instances dictionary, and is returned as the result of the call.
obj2 = (Singleton())  # The __call__ method is triggered again, but now the instance already exists
# in the _instances dictionary. Instead of creating a new object, the method simply returns the existing instance.
print(obj1 is obj2)  # True

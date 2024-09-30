'''Завдання 12: Автоматичне логування доступу до атрибутів (опціонально)
Створіть метаклас LoggingMeta, який автоматично додає логування при доступі до будь-якого атрибута класу.
Кожен раз, коли атрибут змінюється або читається, повинно з'являтися повідомлення в консолі.'''

class LoggingMeta(type):
    """
    Metaclass, which automatically adds logging when accessing any class attribute.
    """

    # The method is triggered when an instance of the class is created (MyClass()).
    def __call__(cls, *args, **kwargs):
        # First, an instance is created, which calls the standard constructor to create an object of the class
        instance = super().__call__(*args, **kwargs)
        return cls._wrap_instance(instance)

    @staticmethod
    def _wrap_instance(instance):
        """
        The method is called to modify the created instance to add logging
        when accessing and modifying its attributes.
        It takes the created instance and returns it after ‘wrapping’ it.
        """

        class WrappedInstance(instance.__class__):
            """
            A nested class that inherits from the instance class and overrides the __getattribute__
            and __setattr__ methods, adding logging when accessing and changing attributes,
            in order to preserve all methods and attributes defined in the original class
            when adding functionality for logging.
            """

            def __getattribute__(self, name):
                """
                This method is called every time an instance attribute is accessed.
                By overriding this method, we can add a message that a
                particular attribute has been accessed.
                """
                print(f"Logging: accessed '{name}'")
                # The original method is called to return the value of the attribute.
                # It accesses the base class attribute so that it does not break the instance
                # and returns the real value of the attribute
                return super().__getattribute__(name)

            def __setattr__(self, name, value):
                """The method is called when a new value is assigned to an instance attribute."""
                print(f"Logging: modified '{name}'")
                # It is called to change the attribute value.
                super().__setattr__(name, value)

        # The instance class is changed to WrappedInstance so that all subsequent attribute
        # accesses and attribute changes go through this wrapped class with logging
        instance.__class__ = WrappedInstance
        return instance


# Test class with metaclass LoggingMeta
class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'

'''Завдання 8: Перевірка успадкування та методів класу
Напишіть функцію analyze_inheritance(cls), яка приймає клас, аналізує його спадкування та
виводить усі методи, які він наслідує від базових класів.'''

def analyze_inheritance(cls):
    """
    The function analyses class inheritance and displays all the methods that it inherits from base classes
    :param cls: class
    """

    # Analyse the class inheritance
    for Inherited_attributes in cls.__bases__:
        # Finding methods that a class inherits from base classes
        if not Inherited_attributes.__name__.startswith("__"):
            # Bypassing all class attributes
            for attribute in dir(Inherited_attributes):
                attr = getattr(cls, attribute)

                # Check if it is not a special method
                if not attribute.startswith("__"):
                    print(f"Клас {cls.__name__} наслідує: \n- {attribute} з {Inherited_attributes.__name__}")


# Test classes
class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)
analyze_inheritance(Parent)

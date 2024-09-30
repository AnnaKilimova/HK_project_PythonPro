'''Завдання 11: Метаклас для обмеження кількості атрибутів (опціонально)
Реалізуйте метаклас LimitedAttributesMeta, який дозволяє класам мати лише фіксовану
кількість атрибутів (наприклад, максимум 3). Якщо додати більше атрибутів, має виникати помилка.'''

class LimitedAttributesMeta(type):
    """Metaclass that allows classes to have only a fixed number of attributes"""

    def __new__(cls, name, bases, dict):
        """
        We filter only attributes that are in the class dictionary,
        but not special methods (those that start with __)
        """
        attrs = {key_expression for key_expression in dict.keys() if not key_expression.startswith("__")}

        # If the number of attributes exceeds the limit, throw an error
        if len(attrs) > 3:
            raise TypeError(": Клас LimitedClass не може мати більше 3 атрибутів.")

        # Create a class
        return super().__new__(cls, name, bases, dict)


# Test class with metaclass LimitedAttributesMeta
class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Викличе помилку


obj = LimitedClass()

'''Завдання 13: Автоматична генерація методів для полів класу (опціонально)
Реалізуйте метаклас AutoMethodMeta, який автоматично генерує методи геттера та сеттера для кожного
атрибута класу. Метод повинен починатися з get_<attribute>() та set_<attribute>(value).'''
class AutoMethodMeta(type):
    def __new__(cls, name, bases, dct):
        # Create a new class taking into account the attributes defined in dct
        new_cls = super().__new__(cls, name, bases, dct)

        # Go through all class attributes, except for service attributes
        for attr_name, attr_value in dct.items():
            if not attr_name.startswith("__"):

                # Getter generation
                def get_attribute(attr):
                    '''
                    It is intended to create and return a getter function that will be called
                    to get the value of the attribute and takes a string representing
                    the attribute name as an argument'''
                    def getter(self):
                        '''
                        A function that ‘remembers’ the name of the attribute (attr) for which it was created
                        :param self: a reference to the instance of the class from which this getter is called
                        '''
                        # It returns the value of the specified attribute at the given object
                        # :param self: a reference to the instance of the class from which this getter is called
                        # :param attr: attribute name
                        return getattr(self, attr)
                    return getter

                setattr(new_cls, f'get_{attr_name}', get_attribute(attr_name))

                # Setter generation
                def set_attribut(attr):

                    def setter(self, value):
                        '''
                        A function that ‘remembers’ the name of the attribute (attr) for which it was created
                        :param self: a reference to the instance of the class from which this setter is called
                        '''

                        # It sets the value of the specified attribute at the given object
                        # :param self: a reference to the instance of the class from which this setter is called
                        # :param attr: attribute name
                        # :param attr: attribute value
                        setattr(self, attr, value)
                    return setter

                setattr(new_cls, f'set_{attr_name}', set_attribut(attr_name))

        return new_cls


# Test class with metaclass AutoMethodMeta
class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
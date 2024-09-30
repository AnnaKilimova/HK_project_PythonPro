"""Завдання 9: Динамічне додавання властивостей
Напишіть клас DynamicProperties, в якому можна динамічно додавати властивості через методи.
Використовуйте вбудовані функції property() для створення геттера та сеттера під час виконання програми."""


class DynamicProperties:
    # Сlass for creating objects to which you can dynamically add properties
    def __init__(self):
        """Empty dictionary for storing the values of attributes"""
        self._properties = {}

    def add_property(self, name, value):
        # Method for adding new attributes to a class object
        """
        :param name: the name of the future property
        :param value: the initial value of the future property
        """

        def getter(self):
            """
            The function uses the _properties dictionary to get the value by the name key that was passed to add_property
            and returns the value that was stored in this dictionary for this property.
            :param self: _properties dictionary
            """
            return self._properties[name]

        def setter(self, new_value):
            """
            The function takes the new_value parameter and updates the corresponding value in the
            _properties dictionary for the name key
            :param self: _properties dictionary
            """
            self._properties[name] = new_value

        # Set the initial value of the property
        self._properties[name] = value

        # The built-in property() function to dynamically add a getter and setter
        setattr(DynamicProperties, name, property(getter, setter))


obj = DynamicProperties()
obj.add_property("name", "default_name")
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python

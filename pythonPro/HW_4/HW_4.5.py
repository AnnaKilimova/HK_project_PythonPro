'''Завдання 5: Модифікація атрибутів під час виконання
Напишіть клас MutableClass, який має методи для динамічного додавання та видалення атрибутів об'єкта.
Реалізуйте методи add_attribute(name, value) та remove_attribute(name).'''

class MutableClass:
    """
    The class for dynamically adding and removing object attributes.
    """

    def add_attribute(self, name, value):
        """
        Adds an attribute to the object.
        :param name: str
        :param value: any
        :return: new attribute
        """
        return setattr(self, name, value)

    def remove_attribute(self, name):
        """
        Removes an attribute from an object if it exists.
        :param name: str
        """
        if hasattr(self, name):
            delattr(self, name)
        else:
            print(f"Attribute '{name}' does not exist.")


# An instance of the class 'MutableClass'
obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
# print(obj.name)  # Виникне помилка, атрибут видалений

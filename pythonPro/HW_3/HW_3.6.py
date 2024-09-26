"""6. Access-like
1. Реалізуйте клас User з атрибутами first_name, last_name, email.
   Додайте методи для отримання та встановлення цих атрибутів через декоратор @property.
2. Додайте методи для перевірки формату email-адреси."""

import re


class User:
    def __init__(self, first_name, last_name, email):
        """Initialise new objects of the User class"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def my_first_name(self):
        """Getter for first_name"""
        return self.first_name

    @my_first_name.setter
    def my_first_name(self, value):
        """Setter for first_name"""
        self.first_name = value

    @property
    def my_last_name(self):
        """Getter for last_name"""
        return self.last_name

    @my_last_name.setter
    def my_last_name(self, value):
        """Setter for last_name"""
        self.last_name = value

    @property
    def my_email(self):
        """Getter for email"""
        return self.email

    @my_email.setter
    def my_email(self, value):
        """Setter for email"""
        if self._validate_email(value):
            self.email = value
        else:
            raise ValueError("Invalid email format")

    def _validate_email(self, email):
        """Method for checking email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.email})"


user = User("James", "Scott", "james@gmail.com")

user.my_first_name = "Michael"
print(user.my_first_name)

user.my_last_name = "Long"
print(user.my_last_name)

user.my_email = "michael@gmail.com"
print(user.my_email)

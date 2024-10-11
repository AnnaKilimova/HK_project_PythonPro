'''Завдання 3. Використання фікстур у pytest
Напишіть програму для керування користувачами та напишіть тести з використанням фікстур у pytest.
Напишіть клас UserManager, який реалізує такі методи:
• add_user(name: str, age: int): додає користувача.
• remove_user(name: str): видаляє користувача на ім'я.
• get_all_users() -> list: повертає список усіх користувачів.'''


class UserManager:
    '''User management.'''

    def __init__(self):
        '''Creating an empty list to work with the users.'''
        self.user_list = []

    def add_user(self, name: str, age: int):
        '''Adding a user.'''
        self.user_list.append([name, age])

    def remove_user(self, name: str):
        '''Removing a user.'''
        for user in self.user_list:
            if user[0] == name:
                self.user_list.remove(user)

    def get_all_users(self) -> list:
        '''Returning a list of all users.'''
        return self.user_list

    def __str__(self):
        '''Displaying the result.'''
        return {self.user_list}

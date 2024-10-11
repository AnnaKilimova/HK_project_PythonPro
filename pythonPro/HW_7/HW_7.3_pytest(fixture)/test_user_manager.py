'''Для тестів створіть фікстуру, яка попередньо додаватиме кількох користувачів перед виконанням тестів.
Напишіть тести для перевірки методів add_user, remove_user, get_all_users.
Використовуйте фікстуру в кожному тесті для попереднього налаштування.
Створіть тест, який скипатиметься за певних умов (наприклад, якщо у користувача менше трьох користувачів).'''

import pytest
from user_manager import UserManager


# Fixture for pre-adding several users before running tests.
@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


# Test for add_user() method
def test_add_user(user_manager):
    user_manager.add_user("Eve", 28)
    users = user_manager.get_all_users()
    assert len(users) == 3
    assert users[-1][0] == "Eve"
    assert users[-1][1] == 28


# Test for remove_user() method
def test_remove_user(user_manager):
    user_manager.remove_user("Eva")
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert users[1][0] == "Bob"


# Test for get_all_users() method
def test_get_all_users(user_manager):
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert users[0][0] == "Alice"
    assert users[1][0] == "Bob"


# A test that will be skipped under certain conditions
@pytest.mark.skipif(len(UserManager().get_all_users()) < 3, reason="Має бути принаймні 3 користувача")
def test_skip_if_less_than_three_users(user_manager):
    users = user_manager.get_all_users()
    assert len(users) >= 3

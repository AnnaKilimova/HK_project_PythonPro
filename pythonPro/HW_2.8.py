"""Завдання 8: Зберігання налаштувань користувача
Реалізувати систему зберігання налаштувань користувача за
допомогою замикань.
1. Створити функцію create_user_settings, яка повертає функцію для
   зберігання і отримання налаштувань.
2. Налаштування можуть включати такі параметри, як
   theme, language і notifications.
3. Додати можливість зберігати, змінювати та переглядати налаштування."""


def create_user_settings():
    settings = {
        "theme": "light",
        "language": "English",
    }

    def manage_settings(action, key=None, value=None):
        nonlocal settings

        if action == "get":
            return (
                settings
                if key is None
                else settings.get(key, f"The key '{key}' doesn't exist")
            )

        elif action == "set":
            if key in settings:
                settings[key] = value
                return f"The value of the '{key}' key was changed to '{value}'"
            return f"The key '{key}' doesn't exist"

        elif action == "add" and key not in settings:
            settings[key] = value
            return f"New setting '{key}' was added with the '{value}' value"

        elif action == "remove":
            if key in settings:
                del settings[key]
                return f"The setting '{key}' is removed"
            else:
                return f"The setting '{key}' is not found"

        else:
            return "incorrect data"

    return manage_settings


user_settings = create_user_settings()
print(user_settings("get"))
print(user_settings("get", "theme"))
print(user_settings("set", "theme", "dark"))
print(user_settings("add", "notifications", "sounds"))
print(user_settings("get"))
print(user_settings("remove", "notifications"))
print(user_settings("get"))

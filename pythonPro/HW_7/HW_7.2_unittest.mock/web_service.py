"""Завдання 2. Мокування за допомогою unittest.mock
Напишіть програму для отримання даних з веб-сайту та протестуйте його за допомогою моків.
Напишіть клас WebService, який має метод get_data(url: str) -> dict.
Цей метод повинен використовувати бібліотеку requests, щоб робити GET-запит та повертати JSON-відповідь. """

import requests


class WebService:
    """To receive data from the website."""

    def get_data(self, url: str) -> dict:
        """The method makes a GET request and returns a JSON response."""
        response = requests.get(url)

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()  # Returning JSON data
        else:
            # In case of an error, we return a message with a status code
            return {"error": f"Request failed with status {response.status_code}"}

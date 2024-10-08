'''Завдання 2: Робота з зовнішніми пакетами
Встанови пакет requests за допомогою pip.
Напиши скрипт, який завантажує сторінку з вказаного URL та зберігає її вміст у текстовий файл.
Додай обробку помилок на випадок, якщо сторінка недоступна.'''

import requests


def download_page(url, file_path):
    try:
        # HTTP request to the specified page.
        response = requests.get(url)

        # If the status code is 200, the page has been successfully loaded.
        if response.status_code == 200:
            with open(file_path, 'w', encoding='utf-8') as file:
                # Write page content to a file.
                file.write(response.text) # Write the page content.
            print(f"The page has been successfully saved to {file_path}")
        else:
            print(f"Page failed to load. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # If any error occurs during the request.
        print(f"Page loading error: {e}")


# Example of use:
url = "https://callands-warrington.secure-dbprimary.com/warrington/primary/callands"
file_path = "page.txt"
download_page(url, file_path)

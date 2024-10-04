'''6. Ітерація через файли в каталозі
Напишіть ітератор, який буде повертати всі файли в заданому каталозі по черзі.
Для кожного файлу виведіть його назву та розмір.'''

import os

def file_iterator(directory):
    """Iterator for getting files from the specified directory."""

    # Recursively walks the specified directory and returns the
    # root folder, subdirectories, and files.
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            yield file, file_size

# Specify the path to the folder with the files.
directory = '/Users/kilimovaann/Downloads'

# Display file names and sizes.
for file_name, file_size in file_iterator(directory):
    print(f"Name: {file_name}, Size: {file_size} bits")

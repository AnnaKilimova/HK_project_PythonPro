# Задача 1: завантаження файлів із мережі
# Створіть програму, яка завантажує кілька файлів із мережі одночасно за допомогою потоків.
# Ваша програма повинна використовувати модуль threading для створення декількох потоків,
# кожен з яких відповідає за завантаження окремого файлу.


import threading # To create and manage threads in Python.
# Threads allow performing multiple tasks at the same time (loading multiple files at once).

import requests # To send HTTP requests to Python (to download files from the internet via URL).
import os # Provides functions for working with the OS (for creating directories, working with file paths, etc.).


def download_file(url, save_path):
    '''
    Function for downloading a file.
    :param url: link to the file to be downloaded.
    :param save_path: path to the directory where the file will be saved.
    '''
    try:

        response = requests.get(url) # Send an HTTP request to the specified url to download the file.
        response.raise_for_status()  # Checks the server's response code.
        filename = os.path.join(save_path, url.split("/")[-1]) # Full path to save the file.
        # url.split("/")[-1]: Splits the URL by the / character and takes the last element, the filename.
        # os.path.join(save_path, ...): Combines save_path with the filename to get the full path to save.

        with open(filename, 'wb') as file: # Opens a file for writing in binary mode
            file.write(response.content)  # Writes the contents of the response (binary data of the downloaded file).

        print(f"Файл '{filename}' завантажено успішно.")

    # If the request ended with an error (4xx or 5xx), an HTTPError exception will be raised and handled in this block.
    except Exception as e:
        print(f"Помилка під час завантаження файлу з {url}: {e}")

def main():
    '''The implementation of the programme.'''

    # List of URLs for downloading
    file_urls = [
        "https://fileinfo.com/img/ss/xl/jpg_44-2.jpg",
        "https://img.freepik.com/free-photo/abstract-autumn-beauty-multi-colored-leaf-vein-pattern-generated-by-ai_188544-9871.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png/200px-Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png"
    ]

    # Directory for saving files.
    save_directory = "downloads"
    os.makedirs(save_directory, exist_ok=True) # Creates the downloads directory if it does not already exist.
    # exist_ok=True: indicates that if the folder already exists, the error should not be triggered.

    # Create and launch threads.
    threads = [] # An empty list is created to hold all threads.
    for url in file_urls:
        # A new thread is created for each URL.
        thread = threading.Thread(target=download_file, args=(url, save_directory))
        # The target argument specifies the function to be executed in this thread (download_file).
        # Arguments for this function are passed through args.
        thread.start()  # Starts the created thread, which starts executing the file download.
        threads.append(thread) # Adds a thread to the threads list so that you can wait for it to finish later.

    # We are waiting for the completion of all threads
    for thread in threads:
        thread.join()

    print("Завантаження завершено.")

# Checks if the programme has been run directly and not imported as a module.
if __name__ == "__main__":
    main()

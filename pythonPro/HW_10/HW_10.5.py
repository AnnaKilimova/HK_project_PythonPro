'''Задача 5: паралельний пошук у файлах
Реалізуйте програму, яка шукає певний текст у кількох великих файлах одночасно, використовуючи потоки або процеси.
Для кожного файлу створіть окремий потік або процес.'''

import threading # To create and manage threads in Python.

def search_in_file(file_name, search_text):
    '''
    To search for a given text.
    :param file_name: text file.
    :param search_text: search text.
    '''
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines() # Reads all lines of a file into a list.
            # String enumeration and text search.
            for line_number, line in enumerate(lines, 1):
                if search_text in line:
                    print(f"Знайдено в файлі {file_name} на рядку {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")

def parallel_search(files_param, search_text_param):
    '''
    Starts a parallel text search in several files.
    :param files_param: files.
    :param search_text: search_text.
    '''
    threads = [] # List for the threads.

    # Create and launch threads for each file.
    for file_name in files_param:
        thread = threading.Thread(target=search_in_file, args=(file_name, search_text))
        threads.append(thread)
        thread.start()

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # List of files to search for.
    files = ['/Users/kilimovaann/Documents/transcript (2).txt', '/Users/kilimovaann/Documents/transcript (3).txt']  # замініть на реальні файли
    search_text = 'Hanna'  # Replace with the desired text.

    parallel_search(files, search_text) #  Launches a parallel text search.

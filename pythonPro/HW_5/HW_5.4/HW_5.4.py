"""4. Генератор для обробки великих файлів
Реалізуйте генератор, який читає великий текстовий файл рядок за рядком (наприклад, лог-файл) і
повертає лише ті рядки, що містять певне ключове слово. Використайте цей генератор для фільтрації файлу
та запису відповідних рядків у новий файл."""


def read_generator(read_file, keyword):
    """A generator that returns strings containing a specific keyword."""

    with open(read_file, "r", encoding="utf-8") as file:
        for line in file:
            if keyword in line:
                yield line


def write_generator(write_file):
    """Function for writing data to a file."""

    with open(write_file, "w", encoding="utf-8") as file:
        for string in read_generator("Test_5.4", keyword):
            file.write(string + "\n")


keyword = "word"  # The specific keyword.

with open("new_5.4_test", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # Display of each row.

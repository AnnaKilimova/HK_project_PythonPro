"""Завдання 7. Тестування з використанням фікстур та тимчасових файлів
Напишіть програму для роботи з файлами. Реалізуйте клас FileProcessor, який має такі методи:
• write_to_file(file_path: str, data: str): записує дані у файл.
• read_from_file(file_path: str) -> str: читає дані з файлу."""


class FileProcessor:
    """Working with files."""

    @staticmethod
    def write_to_file(file_path: str, data: str):
        """Writes data to a file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """Reads data from a file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The {file_path} file hasn't been found.")

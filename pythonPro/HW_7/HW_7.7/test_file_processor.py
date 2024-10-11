"""Протестуйте програму для роботи з файлами використовуючи тимчасові файли та фікстури в pytest.
У тестах використовуйте фікстуру tmpdir для створення тимчасового файлу.
Додайте тести для перевірки методів з великими обсягами даних, порожніми рядками,
а також тести на наявність винятків, якщо файл не знайдено."""


import pytest
from file_processor import FileProcessor


# Test for writing and reading data from a file.
def test_file_write_read(tmpdir):
    # Create a temporary file.
    file = tmpdir.join("testfile.txt")

    # Write data to a file.
    FileProcessor.write_to_file(file, "Hello, World!")

    # Reading data from a file.
    content = FileProcessor.read_from_file(file)

    # Check that the data matches.
    assert content == "Hello, World!"


# Test with a large amount of data.
def test_large_data_file(tmpdir):
    large_text = "A" * 1000000  # Create a text with 1 million characters.
    file = tmpdir.join("largefile.txt")

    # Write a large amount of data to a file.
    FileProcessor.write_to_file(file, large_text)

    # Reading data from a file.
    content = FileProcessor.read_from_file(file)

    # Check that the data matches.
    assert content == large_text


# Test for writing and reading an empty string.
def test_empty_data_file(tmpdir):
    file = tmpdir.join("emptyfile.txt")

    # Write an empty string to the file.
    FileProcessor.write_to_file(file, "")

    # Reading data from a file.
    content = FileProcessor.read_from_file(file)

    # Check that the file is empty.
    assert content == ""


# Exception test if file not found.
def test_file_not_found():
    with pytest.raises(FileNotFoundError) as not_found:
        FileProcessor.read_from_file("nonexistent.txt")

    # Check the text of the exception message.
    assert "nonexistent.txt" in str(not_found.value)

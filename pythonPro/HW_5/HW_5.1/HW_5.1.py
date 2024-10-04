"""1. Створення власного ітератора для зворотного читання файлу
Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку —
рядок за рядком з кінця файлу до початку. Це може бути корисно для аналізу лог-файлів,
коли останні записи найважливіші."""


def my_iterator(file_name):
    """An iterator that reads the file in reverse order"""

    # Open the file in read mode
    with open(file_name, "r", encoding="utf-8") as file:
        file.seek(0, 2)  # Move the pointer to the end of the file
        position = file.tell()  # Find the current file position
        line = ""

        # While the position is greater than zero, reduce it by one
        while position > 0:
            position -= 1
            file.seek(position)  # Move the pointer to the current file position
            char = file.read(1)  # Read one character from the current position

            # If the character is not a newline, add it to the line
            if char != "\n":
                line += char
            # If the character is a newline,
            # return the collected string in the forward order
            # and clear the line
            else:
                yield line[::-1]
                line = ""

        if line:
            yield line[::-1]  # Return the last string, if it exists


# Print the result
for string in my_iterator("test"):
    print(string)

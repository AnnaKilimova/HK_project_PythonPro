"""1. Створення власного ітератора для зворотного читання файлу
Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку —
рядок за рядком з кінця файлу до початку. Це може бути корисно для аналізу лог-файлів,
коли останні записи найважливіші."""

class ReverseFileIterator:
    """An iterator that reads the file in reverse order."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
        self.position = 0
        self.line = ''

    def __iter__(self):
        '''Making an object iterable.'''

        # Returns the iterator itself.
        return self

    def __enter__(self):
        """Open the file in read mode"""
        self.file = open(self.file_path, 'r', encoding='utf-8')
        self.file.seek(0, 2)  # Move the pointer to the end of the file.
        self.position = self.file.tell()  # Set the start position to the end of the file.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the file."""
        if self.file:
            self.file.close()

    def __next__(self):
        """Return the next line from the end of the file."""
        if self.position <= 0 and not self.line:
            raise StopIteration  # If the beginning of the file is reached and the buffer is empty.

        while self.position > 0 or self.line:
            # If there is a new line in the buffer, break it
            if '\n' in self.line:
                lines = self.line.splitlines(keepends=True)  # Break it down into lines
                self.line = ''.join(lines[:-1])  # Leave a part of the buffer
                return lines[-1].strip()  # Return the last line

            #
            if self.position > 0:
                #Set the size of the fragment to be read from the file. We try to read as many characters as
                # possible up to the current position, i.e. starting from the end of the file.
                read_size = self.position
                # Update the pointer position in the file so that the pointer moves back the appropriate number
                # of characters to read the fragment in the next line of code.
                self.position -= read_size
                self.file.seek(self.position) # Move the pointer
                chunk = self.file.read()  # Reading a file fragment
                self.line = chunk + self.line  # Add a new fragment to the line


# Example of use:
file_path = 'test'

with ReverseFileIterator(file_path) as iterator:
    for line in iterator:
        print(line)



# def my_iterator(file_name):
#     """An iterator that reads the file in reverse order"""
#
#     # Open the file in read mode
#     with open(file_name, "r", encoding="utf-8") as file:
#         file.seek(0, 2)  # Move the pointer to the end of the file
#         position = file.tell()  # Find the current file position
#         line = ""
#
#         # While the position is greater than zero, reduce it by one
#         while position > 0:
#             position -= 1
#             file.seek(position)  # Move the pointer to the current file position
#             char = file.read(1)  # Read one character from the current position
#
#             # If the character is not a newline, add it to the line
#             if char != "\n":
#                 line += char
#             # If the character is a newline,
#             # return the collected string in the forward order
#             # and clear the line
#             else:
#                 yield line[::-1]
#                 line = ""
#
#         if line:
#             yield line[::-1]  # Return the last string, if it exists
#
#
# # Print the result
# for string in my_iterator("test"):
#     print(string)

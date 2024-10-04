'''6. Ітерація через файли в каталозі
Напишіть ітератор, який буде повертати всі файли в заданому каталозі по черзі.
Для кожного файлу виведіть його назву та розмір.'''


import os

class DirectoryFileIterator:
    def __init__(self, directory):
        """Initialise the directory for iteration"""
        self.directory = directory
        self.files = os.listdir(directory)  # Get a list of all files in the directory
        self.index = 0  # Starting index for iteration

    def __iter__(self):
        """Making an object iterable."""

        # Returns the iterator itself
        return self

    def __next__(self):
        """Returns the next file in the directory"""
        if self.index >= len(self.files):
            raise StopIteration  # End iteration if all files are processed

        current_file = self.files[self.index]
        self.index += 1
        file_path = os.path.join(self.directory, current_file)

        if os.path.isfile(file_path):  # Check if it's a file (not a subdirectory)
            file_size = os.path.getsize(file_path)  # Get the file size in bytes
            return current_file, file_size
        else:
            # If it is not a file, skip it
            return self.__next__()

# Example of use:
directory_path = '/Users/kilimovaann/Downloads'  # The path to the desired directory.

iterator = DirectoryFileIterator(directory_path)

for file_name, file_size in iterator:
    print(f"File: {file_name}, Size: {file_size} bits")



# import os
#
# def file_iterator(directory):
#     """Iterator for getting files from the specified directory."""
#
#     # Recursively walks the specified directory and returns the
#     # root folder, subdirectories, and files.
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_size = os.path.getsize(file_path)
#             yield file, file_size
#
# # Specify the path to the folder with the files.
# directory = '/Users/kilimovaann/Downloads'
#
# # Display file names and sizes.
# for file_name, file_size in file_iterator(directory):
#     print(f"Name: {file_name}, Size: {file_size} bits")

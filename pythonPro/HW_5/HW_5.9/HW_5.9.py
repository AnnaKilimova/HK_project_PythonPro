'''9. Автоматичне резервне копіювання
Напишіть менеджер контексту, який буде створювати резервну копію важливого файлу перед його обробкою.
Якщо обробка пройде успішно, оригінальний файл замінюється новим.
У разі помилки резервна копія автоматично відновлюється.'''

import shutil
import os

class BackupManager:
    def __init__(self, file_path):
        '''''The 'backup_path' attribute is not initialised in the __init__ method because at that moment
        the file is not read yet, it is initialised later, when entering the context through
        the __enter__ method, at this stage the data is loaded into the config attribute'''

        self.file_path = file_path
        self.backup_path = file_path + ".bak"

    def __enter__(self):
        """Method is called when entering a context block, opens the file and returns it"""

        # Method copies the contents of file_path file src to file backup_path.
        # The function returns the file_path path to the location of the newly copied file
        shutil.copy(self.file_path, self.backup_path)
        print(f"Резервна копія створена: {self.backup_path}")
        return self.file_path

    def __exit__(self, exc_type, exc_value, traceback):
        '''
        The method is called when the context block exits, whether an error occurred or not,
        it closes the file.
        :param exc_type: class of the error (TypeError, ValueError) that occurred during code execution inside the with block.
        If no error occurred, the value is None.
        :param exc_value: the actual error object that contains the error message and other details - exception (FileNotFoundError)
        :param traceback: trace object that contains information about the call stack
        (i.e., in which line of code and in which file the error occurred)
        '''

        if exc_type is None:
            # If the processing is successful, replace the original file
            print("Processing is successful, delete the backup.")
            os.remove(self.backup_path)
        else:
            # If the processing is successful, replace the original file
            print("Error! Restore the backup.")
            shutil.copy(self.backup_path, self.file_path)
            os.remove(self.backup_path)  # Delete the backup after restoring
            print("The backup is restored.")

# Example of use:
file_path = "test_file"

# If the write is successful, the backup is deleted
try:
    with BackupManager(file_path) as file:
        with open(file, 'w', encoding='utf-8') as f:
            f.write("New file content.")  # Successful recording
            # raise ValueError("Simulate an error during processing!")  # Causing an error
except ValueError as e:
    print(f"An error occurred: {e}")



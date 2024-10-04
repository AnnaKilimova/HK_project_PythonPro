'''10. Архівування та зберігання великих даних
Реалізуйте менеджер контексту для архівування файлів (за допомогою модуля zipfile).
Менеджер автоматично створює архів, додає файли, а після виходу з блоку with –
завершує архівування та закриває архів.'''

import zipfile
import os

class ZipArchiveManager:
    '''Archiving class'''
    def __init__(self, archive_name):
        '''The 'zip_file' attribute is not initialised in the __init__ method because at that moment
        the file is not read yet, it is initialised later, when entering the context through
        the __enter__ method, at this stage the data is loaded into the config attribute'''

        self.archive_name = archive_name
        self.zip_file = None

    def __enter__(self):
        """Method is called when entering a context block, opens the file and returns it"""

        # Create an archive in write mode
        self.zip_file = zipfile.ZipFile(self.archive_name, 'w')
        print(f"Archive '{self.archive_name}' has ben created.")
        return self.zip_file

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

        # Close the archive after the work is done
        if self.zip_file:
            self.zip_file.close()
            print(f"Archive '{self.archive_name}' successfully closed.")

# Example of use:
files_to_archive = ['file']  # File to be archived
archive_name = 'backup.zip'

# Add file to archive
with ZipArchiveManager(archive_name) as archive:
    for file in files_to_archive:
        if os.path.exists(file):
            archive.write(file)
            print(f"Added '{file}' to archive.")
        else:
            print(f"File'{file}' is not found.")



'''8. Конфігурація через контекстні менеджери
Напишіть власний контекстний менеджер для роботи з файлом конфігурацій (формат .ini або .json).
Менеджер має автоматично зчитувати конфігурацію при вході в контекст і записувати зміни в файл
після завершення роботи.'''

import json


class ConfigManager:
    """Context manager for working with the configuration file."""

    def __init__(self, file_path):
        '''The 'config' attribute is not initialised in the __init__ method because at that moment
        the file is not read yet, it is initialised later, when entering the context through
        the __enter__ method, at this stage the data is loaded into the config attribute'''

        self.file_path = file_path
        self.config = None

    def __enter__(self):
        """Method is called when entering a context block, opens the file and returns it"""

        # Read configuration from a file when entering a context
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.config = json.load(file)  # Takes a file object and returns the json object (key/value pair).
        except FileNotFoundError:
            # If the file does not exist, create an empty configuration
            self.config = {}
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        The method is called when the context block exits, whether an error occurred or not,
        it closes the file.
        :param exc_type: class of the error (TypeError, ValueError) that occurred during code execution inside the with block.
        If no error occurred, the value is None.
        :param exc_value: the actual error object that contains the error message and other details - exception (FileNotFoundError)
        :param traceback: trace object that contains information about the call stack
        (i.e., in which line of code and in which file the error occurred)
        '''

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.config, file, indent=4, ensure_ascii=False)  # convert Python object into a JSON string


# Example of use:
config_file = "config.json"

# Open the configuration file, modify it, and automatically save the changes
with ConfigManager(config_file) as config:
    # Display the current configuration
    print("Current configuration:", config)

    # Add a new parameter or change an existing one
    config["username"] = "admin"
    config["password"] = "1234"
    config["debug"] = True

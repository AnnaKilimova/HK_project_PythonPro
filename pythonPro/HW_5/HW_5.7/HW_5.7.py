'''7. Парсинг великих лог-файлів для аналітики
Уявіть, що у вас є великий лог-файл від веб-сервера. Створіть генератор, який зчитує файл порціями (по рядку)
і повертає тільки рядки з помилками (код статусу 4XX або 5XX). Запишіть ці помилки в окремий файл
для подальшого аналізу.'''

def log_error_filter(log_file):
    """A generator that returns lines with errors (4XX or 5XX) from a log file."""

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            # Divide the status code string into parts
            parts = line.split()
            if len(parts) > 1:
                status_code = parts[-2]  # Take the status code
                if status_code.startswith(("4", "5")):
                    yield line.strip()


def write_errors(log_file, errors_file):
    """The function of writing erroneous lines to a file."""

    with open(errors_file, "w", encoding="utf-8") as out_file:
        for error_line in log_error_filter(log_file):
            out_file.write(error_line + "\n")


log_file = "my_log_file.log"  # Specify the path to the folder with the files.

errors_file = "errors_only.log"  # File to save lines with errors.

write_errors(log_file, errors_file)

print(f"Errors from the '{log_file}' have been saved to '{errors_file}'")

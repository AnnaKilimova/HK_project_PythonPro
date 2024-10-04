"""3. Збір статистики про зображення
У вас є каталог з великою кількістю зображень. Напишіть ітератор, який по черзі відкриває кожне зображення
(наприклад, за допомогою модуля PIL), витягує з нього метадані (розмір, формат тощо)
і зберігає ці дані у файл CSV."""

import os
import csv
from PIL import Image


def image_get_data_iterator(catalogue):
    """Iterator that opens each image in turn and extracts metadata from it."""

    # Go through all the files in the directory (file name).
    for filename in os.listdir(catalogue):
        # Get the full path to each file connecting paths in a way that is specific to the OS (file path).
        file_path = os.path.join(catalogue, filename)
        # Use the Image.open() function of the Pillow module to open and identify image files.
        with Image.open(file_path) as img:
            data = {
                "filename": filename,
                "format": img.format,
                "size": img.size,
                "path": file_path,
            }
            yield data


def save_metadata_to_csv(catalogue_path, csv_file):
    """Function for writing data to a file."""

    # Open the CSV file for writing
    with open(csv_file, mode="w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["filename", "format", "size", "path"])

        # Specify the path to the file folder for Iterator that opens each image in turn
        # and extracts metadata from it.
        for data in image_get_data_iterator(catalogue_path):
            # Write down each line of data.
            writer.writerow(data)


# Specify the path to the folder with the files.
catalogue_path = "/Users/kilimovaann/Documents/images/Simpsons"

# Specify the name of the new file.
csv_output_file = "image_data.csv"

# Specify the path to the file folder for the function of writing data to a file.
save_metadata_to_csv(catalogue_path, csv_output_file)

print(f"Image data is saved to a file {csv_output_file}")

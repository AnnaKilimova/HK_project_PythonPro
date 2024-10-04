"""3. Збір статистики про зображення
У вас є каталог з великою кількістю зображень. Напишіть ітератор, який по черзі відкриває кожне зображення
(наприклад, за допомогою модуля PIL), витягує з нього метадані (розмір, формат тощо)
і зберігає ці дані у файл CSV."""

import os
import csv
from PIL import Image

class ImageMetadataCollector:
    def __init__(self, directory, csv_file):
        self.directory = directory  # Catalogue with images
        self.csv_file = csv_file    # Path to the CSV file
        self.files = [f for f in os.listdir(directory)]  # List of files
        self.index = 0 # Index of the current file

    def __iter__(self):
        '''Making an object iterable.'''

        # Returns the iterator itself.
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration  # End iteration if all files are viewed

        image_file = self.files[self.index]
        self.index += 1
        image_path = os.path.join(self.directory, image_file)

        with Image.open(image_path) as img:
           return {
                "filename": image_file,
                "format": img.format,
                "size": img.size,
                "path": image_path
            }

    def save_to_csv(self):
        """Method for saving metadata to CSV file"""
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["filename", "format", "size", "path"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for metadata in self:
                if metadata:
                    writer.writerow(metadata)

# Example of use:
directory_path = '/Users/kilimovaann/Documents/images/Simpsons'  # Catalogue with images
csv_file_path = 'image_metadata.csv'  # File for saving metadata

collector = ImageMetadataCollector(directory_path, csv_file_path)
collector.save_to_csv()

print(f"Metadata saved to file {csv_file_path}")



# import os
# import csv
# from PIL import Image
#
#
# def image_get_data_iterator(catalogue):
#     """Iterator that opens each image in turn and extracts metadata from it."""
#
#     # Go through all the files in the directory (file name).
#     for filename in os.listdir(catalogue):
#         # Get the full path to each file connecting paths in a way that is specific to the OS (file path).
#         file_path = os.path.join(catalogue, filename)
#         # Use the Image.open() function of the Pillow module to open and identify image files.
#         with Image.open(file_path) as img:
#             data = {
#                 "filename": filename,
#                 "format": img.format,
#                 "size": img.size,
#                 "path": file_path,
#             }
#             yield data
#
#
# def save_metadata_to_csv(catalogue_path, csv_file):
#     """Function for writing data to a file."""
#
#     # Open the CSV file for writing
#     with open(csv_file, mode="w", encoding="utf-8") as file:
#         writer = csv.DictWriter(file, fieldnames=["filename", "format", "size", "path"])
#
#         # Specify the path to the file folder for Iterator that opens each image in turn
#         # and extracts metadata from it.
#         for data in image_get_data_iterator(catalogue_path):
#             # Write down each line of data.
#             writer.writerow(data)
#
#
# # Specify the path to the folder with the files.
# catalogue_path = "/Users/kilimovaann/Documents/images/Simpsons"
#
# # Specify the name of the new file.
# csv_output_file = "image_data.csv"
#
# # Specify the path to the file folder for the function of writing data to a file.
# save_metadata_to_csv(catalogue_path, csv_output_file)
#
# print(f"Image data is saved to a file {csv_output_file}")

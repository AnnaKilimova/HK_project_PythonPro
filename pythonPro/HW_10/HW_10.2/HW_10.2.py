# Задача 2: паралельна обробка зображень
# Напишіть програму, яка обробляє кілька зображень одночасно (наприклад, змінює їх розмір або застосовує фільтр).
# Використовуйте модуль concurrent.futures і виконуйте обробку зображень у кількох процесах або потоках.
# Підказка: можна використовувати бібліотеку Pillow для обробки зображень.


from concurrent.futures import ThreadPoolExecutor # Allows tasks to be performed in parallel using threads
from PIL import Image, ImageFilter # To work with images (filters for image processing, such as blur).
import os # Provides functions for working with the OS (for creating directories, working with file paths, etc.).


def process_image(image_path, output_path):
    '''
    To work with images
    :param image_path: path to the original image.
    :param output_path: path to the directory where the file will be saved.
    '''
    try:
        with Image.open(image_path) as img:
            # Apply a blur filter.
            img = img.filter(ImageFilter.GaussianBlur(5))

            # Resize the image.
            img = img.resize((800, 600))

            # Save the processed image.
            img.save(output_path)
            print(f"Зображення {image_path} оброблено та збережено як {output_path}")
    except Exception as e:
        print(f"Помилка під час обробки зображення {image_path}: {e}")

def main():
    '''The implementation of the programme.'''

    # List of images to be processed.
    image_paths = [
        "/Users/kilimovaann/Documents/images/Simpsons/8.jpg",
        "/Users/kilimovaann/Documents/images/Simpsons/7.jpg",
        "/Users/kilimovaann/Documents/images/Simpsons/6.jpg"
    ]

    # Directory for saving files.
    save_directory = "processed_images"
    os.makedirs(save_directory, exist_ok=True) # Creates the downloads directory if it does not already exist.
    # exist_ok=True: indicates that if the folder already exists, the error should not be triggered.

    with ThreadPoolExecutor(max_workers=3) as executor: # Up to three tasks will be performed simultaneously.
        futures = [] # An empty list is created to hold all threads.
        for image_path in image_paths: # # A new thread is created for each image.
            # The target argument specifies the function to be executed in this thread (process_image).
            output_path = os.path.join(save_directory, f"processed_{os.path.basename(image_path)}")
            # Adds a thread to the threads list.
            futures.append(executor.submit(process_image, image_path, output_path))

        # Waiting for all the assignments to be completed
        for future in futures:
            future.result()

    print("Усі зображення оброблено.")

# Checks if the programme has been run directly and not imported as a module.
if __name__ == "__main__":
    main()

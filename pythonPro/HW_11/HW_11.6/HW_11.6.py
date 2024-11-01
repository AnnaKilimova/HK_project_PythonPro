import asyncio # For organising asynchronous operations and managing functions that can be suspended and resumed.
import aiohttp # To send and receive HTTP requests without blocking the main thread.

async def download_image(url: str, filename: str):
    """
    For downloading an image.
    :param url: URL of the image for downloading.
    :param filename: File name for saving the image.
    """
    try:
        async with aiohttp.ClientSession() as session: # Create a session to execute HTTP requests.
            async with session.get(url, ssl=False) as response: # Making an image request.
                if response.status == 200: # Check if the request was successful.
                    image_data = await response.read() # Reading image data.
                    # Save the image to a file.
                    with open(filename, 'wb') as file:
                        file.write(image_data)
                    print(f"Успешно скачано: {filename}")
                else:
                    print(f"Ошибка {response.status} при загрузке {url}")
    except aiohttp.ClientError as e:
        print(f"Ошибка соединения с {url}: {e}")

async def main(image_urls: list):
    """
    To download multiple images.
    :param image_urls: A list of tuples where each contains an image URL and a file name.
    """
    tasks = [download_image(url, filename) for url, filename in image_urls]
    await asyncio.gather(*tasks)

# List of image URLs and file names to be saved.
image_urls = [
    ("https://img.freepik.com/free-photo/highly-detailed-view-fox-its-natural-environment_23-2151570814.jpg", "image1.jpg"),
    ("https://thumbs.dreamstime.com/b/pug-dog-adorable-expression-23622253.jpg", "image2.jpg"),
    ("https://www.shutterstock.com/image-photo/portrait-cute-funny-raccoon-closeup-260nw-1569920464.jpg", "image3.jpg")
]

# Starting asynchronous loading of images.
if __name__ == "__main__":
    asyncio.run(main(image_urls))

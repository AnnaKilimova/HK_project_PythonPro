'''Завдання 2: Робота з асинхронними HTTP-запитами
Використовуючи бібліотеку aiohttp, створіть асинхронну функцію fetch_content(url: str), яка виконує HTTP-запит
до вказаного URL і повертає вміст сторінки.
Створіть асинхронну функцію fetch_all(urls: list), яка приймає список URL і завантажує вміст усіх сторінок паралельно.
Використайте await та об'єднання кількох завдань (asyncio.gather()), щоб завантаження всіх сторінок виконувалося одночасно.
Обробіть можливі помилки запитів, щоб у разі проблеми з підключенням функція повертала відповідне повідомлення про помилку.'''


import asyncio # For organising asynchronous operations and managing functions that can be suspended and resumed.
import aiohttp #  To send and receive HTTP requests without blocking the main thread.

async def fetch_content(url: str):
    '''For loading page content.'''
    try:
        async with aiohttp.ClientSession() as session: # Creates a session to execute HTTP requests.
            # Sends an asynchronous GET request to the specified url.
            async with session.get(url, ssl=False) as response:  # Disables SSL certificate verification.
                if response.status == 200: # Checks whether the request is successful.
                    content = await response.text() # Loads the text content of the page into the variable.
                    print(f"Успішно завантажено: {url}")
                    return content # Returns the contents of the page.
                # Handles cases where the HTTP status is different from 200.
                else:
                    print(f"Помилка {response.status} під час завантаження: {url}")
                    return None
    # Intercepts exceptions that may arise from connection problems.
    except aiohttp.ClientError as e:
        print(f"Помилка підключення до {url}: {e}")
        return None # Returns None if a connection error occurred.

async def fetch_all(urls: list):
    '''For loading multiple pages at the same time.'''
    tasks = [fetch_content(url) for url in urls] # Creates a list of tasks consisting of calls for each URL.
    results = await asyncio.gather(*tasks) # Starts all tasks at the same time.
    return results # Returns a list containing the results of loading all pages.

# List with URLs of pages to be loaded.
urls = [
    "https://www.apple.com/",
    "https://lms.ithillel.ua/groups/66979c9ecabfcfef6169e5fb/homeworks/6717f740cdf4456b52164583",
    "https://nonexistent-url.org" # Incorrect URL to check the error processing.
]

# To check if the script is running as a main programme.
if __name__ == "__main__":
    results = asyncio.run(fetch_all(urls)) # Waits for all pages to finish loading and returns the list.
    print("\nЗавантажений вміст усіх сторінок:")
    for idx, content in enumerate(results):
        if content:
            print(f"Вміст сторінки {urls[idx]}:\n{content[:100]}...\n")
        else:
            print(f"Не вдалося завантажити {urls[idx]}")

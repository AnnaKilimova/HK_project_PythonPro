'''Завдання 1: Основи асинхронності
Напишіть асинхронну функцію download_page(url: str), яка симулює завантаження сторінки за допомогою asyncio.sleep().
Функція повинна приймати URL та "завантажувати" сторінку за випадковий проміжок часу від 1 до 5 секунд.
Після завершення завантаження, функція повинна вивести повідомлення з URL і часом завантаження.
Напишіть асинхронну функцію main(urls: list), яка приймає список з декількох URL і завантажує їх одночасно,
використовуючи await для паралельного виконання функції download_page().'''


import asyncio # For organising asynchronous operations and managing functions that can be suspended and resumed.
import random # For generating random numbers for random page load time.

async def download_page(url: str):
    '''To simulate page loading.'''
    load_time = random.randint(1, 5) # Generate a random delay time.
    # Pauses the function, allowing other tasks to run while this function ‘waits’ for the load to finish.
    await asyncio.sleep(load_time)
    print(f"Завантажено: {url} за {load_time} секунд")

async def main(urls: list):
    '''For loading multiple pages at the same time.'''
    # Use await to execute download_page for each URL in parallel.
    tasks = [download_page(url) for url in urls]  # Create a list of tasks.
    await asyncio.gather(*tasks)  #  Perform the download simultaneously.

# List of URLs for download simulation.
urls = [
    "http://example.com/page1",
    "http://example.com/page2",
    "http://example.com/page3",
    "http://example.com/page4",
]

# Running an asynchronous programme.
asyncio.run(main(urls))

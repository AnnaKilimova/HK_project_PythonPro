import time
import requests
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# URL for the test request.
URL = "https://www.apple.com/"
NUM_REQUESTS = 100  # Number of requests.

# Synchronised approach.
def sync_request():
    for i in range(NUM_REQUESTS):
        try:
            response = requests.get(URL, timeout=5)
            print(f"[Синхронный] Запрос {i+1} завершен со статусом {response.status_code}")
        except requests.RequestException as e:
            print(f"[Синхронный] Ошибка при запросе {i+1}: {e}")

# Multithreaded approach.
def thread_request():
    def make_request(i):
        try:
            response = requests.get(URL, timeout=5)
            print(f"[Многопоточный] Запрос {i+1} завершен со статусом {response.status_code}")
        except requests.RequestException as e:
            print(f"[Многопоточный] Ошибка при запросе {i+1}: {e}")

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(make_request, range(NUM_REQUESTS))

# Multiprocessor approach.
def process_request():
    def make_request(i):
        try:
            response = requests.get(URL, timeout=5)
            print(f"[Многопроцессорный] Запрос {i+1} завершен со статусом {response.status_code}")
        except requests.RequestException as e:
            print(f"[Многопроцессорный] Ошибка при запросе {i+1}: {e}")

    with ProcessPoolExecutor(max_workers=20) as executor:
        executor.map(make_request, range(NUM_REQUESTS))

# Asynchronous approach.
async def async_request():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, i) for i in range(NUM_REQUESTS)]
        await asyncio.gather(*tasks)

async def fetch(session, i):
    try:
        async with session.get(URL, timeout=5) as response:
            await response.text()
            print(f"[Асинхронный] Запрос {i+1} завершен со статусом {response.status}")
    except aiohttp.ClientError as e:
        print(f"[Асинхронный] Ошибка при запросе {i+1}: {e}")

def measure_time(func):
    '''Function for measuring the runtime.'''
    start_time = time.time()
    func()
    end_time = time.time()
    return end_time - start_time

def measure_async_time(async_func):
    '''For measuring asynchronous code execution time.'''
    start_time = time.time()
    asyncio.run(async_func())
    end_time = time.time()
    return end_time - start_time

# Main function for running tests.
if __name__ == "__main__":
    # Synchronous mode.
    print("Синхронный режим:")
    sync_time = measure_time(sync_request)
    print(f"Час виконання: {sync_time:.2f} секунд")

    # Multithreaded mode.
    print("Многопоточный режим:")
    thread_time = measure_time(thread_request)
    print(f"Час виконання: {thread_time:.2f} секунд")

    # Multiprocessor mode.
    print("Многопроцессорный режим:")
    process_time = measure_time(process_request)
    print(f"Час виконання: {process_time:.2f} секунд")

    # Asynchronous mode.
    print("Асинхронный режим:")
    async_time = measure_async_time(async_request)
    print(f"Час виконання: {async_time:.2f} секунд")

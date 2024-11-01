'''Завдання 5: Створення простого асинхронного веб-сервера
1. Використовуючи бібліотеку aiohttp, створіть простий асинхронний веб-сервер, який має два маршрути:
/, який повертає простий текст "Hello, World!".
/slow, який симулює довгу операцію з затримкою в 5 секунд і повертає текст "Operation completed".
2. Запустіть сервер і перевірте, що він може обробляти кілька запитів одночасно
(зокрема, маршрут /slow не блокує інші запити).'''

from aiohttp import web # Allows to easily create asynchronous HTTP servers.
import asyncio # For organising asynchronous operations and managing functions that can be suspended and resumed.


async def handle_hello(request):
    '''Handles requests for route ‘/’.'''
    return web.Response(text="Hello, World!")  # Return text response.


async def handle_slow(request):
    '''Handles requests for the route ‘/slow.'''
    await asyncio.sleep(5)  # # Asynchronous delay of 5 seconds to simulate a long operation.
    return web.Response(text="Operation completed")  # Return a text response after completion.


def main():
    '''To create and run a web server.'''
    app = web.Application()  # Creating a web application aiohttp
    app.add_routes([
        web.get('/', handle_hello),  # The route for ‘/’ that is handled by handle_hello.
        web.get('/slow', handle_slow)  # The route for ‘/slow’, which is handled by the handle_slow function.
    ])

    web.run_app(app, port=8080) # Running a web server on port 8080.


# Programme entry point.
if __name__ == "__main__":
    main()

'''Завдання 4: Асинхронний таймаут
Напишіть функцію slow_task(), яка імітує виконання завдання протягом 10 секунд.
Використовуючи asyncio.wait_for(), викличте slow_task() з таймаутом 5 секунд.
Якщо завдання не встигає виконатися за цей час, виведіть повідомлення про перевищення часу очікування.'''


import asyncio # For organising asynchronous operations and managing functions that can be suspended and resumed.

async def slow_task():
    '''Simulates a long task completion.'''
    print("Beginning of execution slow_task()...")
    await asyncio.sleep(10)  # Simulation of task execution within 10 seconds.
    print("slow_task() completed.")

async def main():
    '''Calls slow_task with timeout.'''
    try:
        # Set timeout for slow_task() execution.
        await asyncio.wait_for(slow_task(), timeout=5)  # Timeout for 5 seconds.
    except asyncio.TimeoutError:
        # Handle exception if execution exceeds timeout.
        print("The time to wait for the task to complete has exceeded the set timeout.")

# Running an asynchronous program.
asyncio.run(main())

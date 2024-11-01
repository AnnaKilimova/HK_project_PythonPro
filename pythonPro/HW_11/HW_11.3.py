'''Завдання 3: Асинхронні черги
Реалізуйте асинхронну чергу завдань за допомогою asyncio.Queue. Створіть функцію producer(queue),
яка додає 5 завдань до черги із затримкою в 1 секунду.
Напишіть функцію consumer(queue), яка забирає завдання з черги, виконує його (наприклад, виводить повідомлення),
імітуючи роботу з кожним завданням із затримкою в 2 секунди.
Створіть функцію main(), яка одночасно запускає і producer, і кілька споживачів (consumer)
за допомогою asyncio.gather(), щоб споживачі обробляли завдання в міру їх появи в черзі.'''


import asyncio # For organising asynchronous operations and managing functions that can be suspended and resumed.

async def producer(queue):
    '''Adds a task to the queue.'''
    for i in range(5):
        await asyncio.sleep(1)  # Simulate the time to create a task.
        task = f"Завдання {i+1}"
        await queue.put(task)  # Add tasks to the queue.]
        print(f"Producer: Додав {task} в чергу")

async def consumer(queue, consumer_id):
    '''Processes tasks from the queue.'''
    while True:
        task = await queue.get()  # Receive tasks from the queue.
        print(f"Consumer {consumer_id}: Отримав {task}")
        await asyncio.sleep(2)  # Simulate task processing.
        print(f"Consumer {consumer_id}: Виконав {task}")
        queue.task_done()  # Mark the task as completed.

async def main():
    '''To launch producer and consumer functions.'''
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue)) # Launching producer.
    consumer_tasks = [asyncio.create_task(consumer(queue, i)) for i in range(3)] # Launching several consumer.
    await producer_task # Waiting for producer to finish adding tasks.
    await queue.join() # Waiting for all tasks in the queue to be processed.

    for task in consumer_tasks:
        task.cancel() # Stopping the consumer.

    await asyncio.gather(*consumer_tasks, return_exceptions=True) # Waiting for the completion of consumer.

asyncio.run(main()) # Launch the application

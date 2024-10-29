# Задача 3: підрахунок суми чисел у великому масиві
# Створіть програму, яка ділить великий масив чисел на кілька частин і рахує суму кожної частини паралельно
# в різних процесах. Використовуйте модуль multiprocessing.

import multiprocessing # Allows creation and management of processes.
import numpy as np # Provides tools for working with arrays and vector calculations.

def partial_sum(array_slice):
    '''
    For calculating the sum of a part of an array.
    :param array_slice: array slice
    '''
    return sum(array_slice)

def main():
    '''The implementation of the programme.'''

    # Generating a large array of random numbers.
    large_array = np.random.randint(1, 100, size=1000000)

    # Number of processes for parallel processing.
    num_processes = 4

    # Divide the array into parts for each process.
    chunk_size = len(large_array) // num_processes
    chunks = [large_array[i*chunk_size:(i+1)*chunk_size] for i in range(num_processes)]

    # Create a process pool.
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Calculate the amounts in parallel
        result = pool.map(partial_sum, chunks)

    # Calculate the total amount
    total_sum = sum(result)
    print(f"Загальна сума: {total_sum}")

# Checks if the programme has been run directly and not imported as a module.
if __name__ == "__main__":
    main()

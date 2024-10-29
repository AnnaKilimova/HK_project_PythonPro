'''Задача 7: обчислення факторіалу великих чисел
Напишіть програму, яка обчислює факторіал великого числа за допомогою декількох потоків або процесів,
розподіляючи обчислення між ними.'''

import multiprocessing as mp
import math
import sys

# Change the limit for the number of digits when processing large numbers.
sys.set_int_max_str_digits(1000000)  # Set the maximum number of digits allowed.


def partial_factorial(start, end):
    '''Calculating the factorial of a range of numbers.'''
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def parallel_factorial(n, num_processes=4):
    '''Distribution of factorial calculation between processes.'''

    # Calculating the number range for each process.
    chunk_size = n // num_processes
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes)]

    # If there are any remaining numbers (n % num_processes != 0), add them to the last process.
    if n % num_processes != 0:
        ranges[-1] = (ranges[-1][0], n)

    # Use multiprocessing to calculate parts of a factorial in parallel.
    with mp.Pool(processes=num_processes) as pool:
        results = pool.starmap(partial_factorial, ranges)

    # Multiply all partial results to obtain the final factor.
    factorial_result = math.prod(results)
    return factorial_result


if __name__ == "__main__":
    n = 100000  # A number to calculate the factorial.
    num_processes = 4  # Number of processes.

    result = parallel_factorial(n, num_processes)
    print(f"Факторіал числа {n} дорівнює: {result}")

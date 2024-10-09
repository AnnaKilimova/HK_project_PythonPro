'''3. У файлі main.py імпортуй функції з модулів і продемонструй їх роботу,
викликавши кожну з функцій.'''

from math_utils import fact, gcd
from string_utils import uppercase_func, remove_gaps, my_str


# Get results
print(f'Factorial of the number is {fact(4)}')
print(f"The greatest common divisor is: {gcd(18, 12)}")
print(uppercase_func(my_str))
print(remove_gaps(my_str))
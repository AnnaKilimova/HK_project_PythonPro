'''Реалізуй у файлі math_utils.py функцію, яка обчислює факторіал числа,
а також функцію для знаходження найбільшого спільного дільника двох чисел.'''

def fact(x):
    '''
    Find factorial of the number.
    :param x: int.
    :return: int.
    '''
    if x == 1:
        return 1
    return fact(x - 1) * x

def gcd(a, b):
    """
    Find the greatest common divisor of two numbers a and b.
    :param a: int.
    :param b: int.
    :return: int.
    """
    while b != 0:
        a, b = b, a % b
    return a
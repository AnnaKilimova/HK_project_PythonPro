'''1. Dunder methods
1. Реалізуйте клас Fraction (дробові числа), який має методи для додавання,
   віднімання, множення та ділення двох об'єктів цього класу.
   Використайте спеціальні методи __add__, __sub__, __mul__, __truediv__.
2. Реалізуйте метод __repr__, щоб можна було коректно виводити об'єкти цього
   класу у форматі "numerator/denominator"'''

import math


class Fraction:
    def __init__(self, numerator, denominator):
        '''Initialises a new object of the Fraction class'''
        if denominator == 0:
            raise ValueError('Denominator can\'t be 0')
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        '''Find the greatest common divisor of the two integers for reducing fraction'''
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        # Normalise the sign so that the denominator is always positive
        if self.denominator < 0:
            self.denominator = abs(self.denominator)

    def __add__(self, other):
        '''Adding two fractions'''
        if isinstance(other, Fraction):
            new_numerator = (
                self.numerator * other.denominator
                + other.numerator * self.denominator
            )
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        '''Subtracting two fractions'''
        if isinstance(other, Fraction):
            new_numerator = (
                self.numerator * other.denominator
                - other.numerator * self.denominator
            )
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        '''Multiply two fractions'''
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        raise TypeError('It must be an instance of Fraction')

    def __truediv__(self, other):
        '''Dividing two fractions'''
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError(
                    'Can\'t divide by a fraction with a numerator of 0'
                )
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        raise TypeError('It must be an instance of Fraction')

    def __repr__(self):
        '''Returns a string representation of a fraction'''
        return f'{self.numerator}/{self.denominator}'


fraction_1 = Fraction(1, 2)  # 1/2
fraction_2 = Fraction(5, 6)  # 5/6

print(f'fraction_1 + fraction_2 = {fraction_1 + fraction_2}')  # Add
print(f'fraction_1 - fraction_2 = {fraction_1 - fraction_2}')  # Sub
print(f'fraction_1 * fraction_2 = {fraction_1 * fraction_2}')  # Mul
print(f'fraction_1 / fraction_2 = {fraction_1 / fraction_2}')  # Truediv

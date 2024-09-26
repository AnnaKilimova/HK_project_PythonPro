'''2. Numeric-like
1. Реалізуйте клас Vector, що підтримує операції додавання,
   віднімання, множення на число та порівняння за довжиною.
   Використовуйте відповідні dunder-методи
   (__add__, __sub__, __mul__, __lt__, __eq__).
2. Додайте до класу метод для отримання довжини вектора'''

import math


class Vector:
    def __init__(self, x, y):
        '''Initialise a new object of the Vector class with two coordinates x and y'''
        self.x = x
        self.y = y

    def __add__(self, other):
        '''Adding operation'''
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError('The operand isn\'t an instance of Vector')

    def __sub__(self, other):
        '''Subtracting operation'''
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError('The operand isn\'t an instance of Vector')

    def __mul__(self, number):
        '''Multiplication by number'''
        if isinstance(number, (int, float)):
            return Vector(self.x * number, self.y * number)
        raise TypeError('The operand isn\'t a number')

    def length(self):
        '''Vector length'''
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        '''Comparison by length'''
        if isinstance(other, Vector):
            return self.length() < other.length()
        return NotImplemented

    def __eq__(self, other):
        '''Comparison by length'''
        if isinstance(other, Vector):
            return self.length() == other.length()
        return NotImplemented

    def __str__(self):
        '''Representing a vector as a string'''
        return f'Vector({self.x}, {self.y})'


vector_1 = Vector(1, 2)
vector_2 = Vector(3, 4)
vector_3 = Vector(1, 2)

add_vectors = vector_1 + vector_2  # Add
print(f'vector_1 + vector_2 = {add_vectors}')

sub_vectors = vector_1 - vector_2  # Sub
print(f'vector_1 - vector_2 = {sub_vectors}')

mul_vector_1 = vector_1 * 2  # Mul
print(f'vector_1 * 2 = {mul_vector_1}')

print(f'Length of vector_1: {vector_1.length()}') # Vector length
print(f'Length of vector_2: {vector_2.length()}') # Vector length
print(f'Length of vector_3: {vector_3.length()}') # Vector length

print(f'vector_1 == vector_2: {vector_1 == vector_2}') # Comparison by length
print(f'vector_1 == vector_2: {vector_1 == vector_3}') # Comparison by length
print(f'vector_1 < vector_2: {vector_1 < vector_2}') # Comparison by length

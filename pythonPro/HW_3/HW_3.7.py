'''7. Vector class implementation
1. Створіть клас Vector, який представляє вектор у просторі з n вимірами.
   Додайте методи для додавання, віднімання векторів та обчислення скалярного добутку.
   Використовуйте dunder-методи (__add__, __sub__, __mul__).
2. Додайте можливість порівняння двох векторів за їх довжиною.'''

import math


class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        '''Adding two vectors'''
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions")
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        '''Subtracting two vectors'''
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions")
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def __iter__(self):
        """Implement the __iter__() method to make the class iterable"""
        return iter(self.components)

    def __mul__(self, other):
        '''Scalar product'''
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same number of dimensions")
            mul_res = Vector(*(x * y for x, y in zip(self.components, other.components)))
            return sum(mul_res)

    def length(self):
        """Length (module) of the vector"""
        return math.sqrt(sum(x**2 for x in self.components))

    def __lt__(self, other):
        """Comparison of vector lengths (less)"""
        return self.length() < other.length()

    def __eq__(self, other):
        """Comparing the length of vectors (equal)"""
        return self.length() == other.length()

    def __gt__(self, other):
        """Comparing the length of vectors (more)"""
        return self.length() > other.length()

    def __repr__(self):
        """Output"""
        return f"Vector{self.components}"


vector_1 = Vector(1, 2, 3)
vector_2 = Vector(4, 5, 6)

vector_3 = vector_1 + vector_2  # Add
print(f"vector_1 + vector_2 = {vector_3}")

vector_4 = vector_1 - vector_2  # Sub
print(f"vector_1 - vector_2 = {vector_4}")

scalar_product = vector_1 * vector_2  # Scalar product
print(f"scalar product = {scalar_product}")

# Comparison
print(f"Is vector_1 < vector_2? {vector_1 < vector_2}")
print(f"Is vector_1 == vector_2? {vector_1 == vector_2}")
print(f"Is vector_1 > vector_2? {vector_1 > vector_2}")
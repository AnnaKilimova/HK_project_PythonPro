"""4. Binary
1. Реалізуйте клас BinaryNumber, який представляє двійкове число.
   Додайте методи для виконання двійкових операцій:
   AND (__and__), OR (__or__), XOR (__xor__) та NOT (__invert__).
2. Напишіть тест для цих операцій"""


class BinaryNumber:
    def __init__(self, value):
        """Accepts a string in binary format or an integer"""
        if isinstance(value, str):
            self.value = int(value, 2)  # Convert a binary number string to an integer
        elif isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Value can only be a string in binary format or an integer")

    def __and__(self, other):
        """AND"""
        return BinaryNumber(self.value & other.value)

    def __or__(self, other):
        """OR"""
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other):
        """XOR"""
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self):
        """NOT"""
        return BinaryNumber(~self.value & ((1 << self.value) - 1))

    def __repr__(self):
        """Returns a binary number in string format"""
        return f"{bin(self.value)[2:]} (decimal: {self.value})"  # Remove the '0b' prefix used to denote binary numbers in Python


binary_number_1 = BinaryNumber("10101")  # 21 decimal
binary_number_2 = BinaryNumber(13)  # 13 decimal

assert (binary_number_1 & binary_number_2).value == 5  # 101 (decimal: 5) - AND
assert (binary_number_1 | binary_number_2).value == 29  # 11101 (decimal: 29) - OR
assert (binary_number_1 ^ binary_number_2).value == 24  # 11000 (decimal: 24) - XOR
assert (~binary_number_2).value == 8178  # 1111111110010 (decimal: 8178)
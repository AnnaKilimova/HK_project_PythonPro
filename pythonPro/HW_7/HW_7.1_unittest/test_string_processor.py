"""Напишіть тести для кожного методу, перевіряючи кілька різних сценаріїв:
• порожні рядки  • рядки з різними регістрами  • рядки з цифрами та символами.
Використовуйте декоратор @unittest.skip для пропуску тесту, який тестує метод reverse_string з порожнім рядком,
оскільки це відома проблема, яку ви плануєте вирішити пізніше."""

import unittest
from string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):
    '''Define a class that inherits from unittest.TestCase to use unittest's built-in methods for testing.'''
    def setUp(self):
        """Initialise an instance of the class."""
        self.processor = StringProcessor()

# reverse_string() method testing

    @unittest.skip("Known issue with empty string")
    def test_reverse_string_empty(self):
        """Test for an empty string (skipped)"""
        self.assertEqual(self.processor.reverse_string(""), "")  # Empty strings.

    def test_reverse_string(self):
        """Test the string flip."""
        self.assertEqual(self.processor.reverse_string("Hello"), "olleH")  # Strings with different cases.
        self.assertEqual(self.processor.reverse_string("123hello!@#"), "#@!olleh321")  # Strings with numbers and symbols.

# capitalize_string() method testing
    def test_capitalize_string(self):
        """Test the capitalisation of a string."""
        self.assertEqual(self.processor.capitalize_string(""), "")  # Empty strings.
        self.assertEqual(self.processor.capitalize_string("Hello"), "Hello")  # Strings with different cases.
        self.assertEqual(self.processor.capitalize_string("123hello!@#"), "123hello!@#")  # Strings with numbers and symbols.

# count_vowels() method testing
    def test_count_vowels(self):
        """Test vowel counting."""
        self.assertEqual(self.processor.count_vowels(""), 0)  # Empty strings.
        self.assertEqual(self.processor.count_vowels("Hello"), 2)  # Strings with different cases.
        self.assertEqual(self.processor.count_vowels("123hello!@#"), 2)  # Strings with numbers and symbols.


if __name__ == "__main__":
    unittest.main()

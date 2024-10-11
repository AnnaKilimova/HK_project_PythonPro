"""Завдання 1. Модульне тестування з використанням unittest
Напишіть простий застосунок для обробки рядків та напишіть модульні тести з використанням бібліотеки unittest.
Створіть клас StringProcessor з методами:
• reverse_string(s: str) -> str: повертає перевернутий рядок.
• capitalize_string(s: str) -> str: робить першу літеру рядка великої.
• count_vowels(s: str) -> int: повертає кількість голосних у рядку."""


class StringProcessor:
    '''For processing strings.'''
    def reverse_string(self, s: str) -> str:
        """Flips the line."""
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """Makes the first letter capital."""
        if len(s) == 0:
            return s
        return s[0].upper() + s[1:]

    def count_vowels(self, s: str) -> int:
        """Counts the number of vowels in a string."""
        vowels = "aeiouAEIOU"
        return sum(1 for char in s if char in vowels)

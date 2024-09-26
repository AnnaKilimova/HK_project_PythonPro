"""5. For built-in functions implementation
1. Реалізуйте власну версію функцій len(), sum(), та min().
   Використовуйте спеціальні методи __len__, __iter__, __getitem__, якщо необхідно.
2. Напишіть тест для кожної з реалізованих функцій."""


class MyList:
    def __init__(self, *items):
        """Initialise a new object of the MyList class"""
        self.items = items

    def my_len(self):
        """len()"""
        count = 0
        for _ in self.items:
            count += 1
        return count

    def __iter__(self):
        """Implement the __iter__() method to make the class iterable"""
        return iter(self.items)

    def my_sum(self):
        """sum()"""
        total = 0
        for item in self:
            total += item
        return total

    def __getitem__(self, index):
        """In order to be able to access the list item using a reference to the object"""
        return self.items[index]

    def my_min(self):
        """min()"""
        minimum = self[0]  # Access to the element via __getitem__ (instead of minimum = self.items[0])
        for i in range(1, len(self.items)):
            if self[i] < minimum:
                minimum = self[i]
        return minimum


my_list = MyList(1, 2, 3, 4, 5)
assert my_list.my_len() == 5, "Test failed: my_len() should return 5"
assert my_list.my_sum() == 15, "Test failed: my_sum() should return 15"
assert my_list.my_min() == 1, "Test failed: my_min() should return 1"

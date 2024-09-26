"""3. to-Compare
1. Реалізуйте клас Person із параметрами name та age.
   Додайте методи для порівняння за віком (__lt__, __eq__, __gt__).
2. Напишіть програму для сортування списку об'єктів класу Person за віком"""


class Person:
    def __init__(self, name, age):
        """Initialise a new object of the Person class"""
        self.name = name
        self.age = age

    def __lt__(self, other):
        """Comparison by age"""
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __eq__(self, other):
        """Comparison by age"""
        if isinstance(other, Person):
            return self.age == other.age
        return NotImplemented

    def __gt__(self, other):
        """Comparison by age"""
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __str__(self):
        """Representing as a string"""
        return f"Person(name = {self.name}, age = {self.age})"


# Create a list of Person objects
people = [Person("Jason", 44), Person("Michael", 65), Person("Hanna", 39)]

print(f"{people[0].name} == {people[1].name}: {people[0] == people[1]}")  # Comparison by age
print(f"{people[0].name} > {people[1].name}: {people[0] > people[1]}")  # Comparison by age
print(    f"{people[0].name} < {people[1].name}: {people[0] < people[1]}")  # Comparison by age

# Sort a list of people by age
sorted_people = sorted(people)

# Display a sorted list
print("Sorted people by age:")
for person in sorted_people:
    print(person)

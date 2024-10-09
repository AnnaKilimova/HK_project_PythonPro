"""Завдання 3: Робота з CSV файлами
1. Створи CSV-файл з даними про студентів, де кожен рядок містить:
• Ім'я студента  • Вік  • Оцінку
2. Напиши програму, яка:
• Читає дані з CSV-файлу  • Виводить середню оцінку студентів  • Додає нового студента до файлу."""

import csv


# Create a CSV file with student data.
with open("data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Mark"])
    writer.writerow(["Alice", 30, 90])
    writer.writerow(["Bob", 25, 80])

file_path = "data.csv"


def calculate_average_grade(file_path):
    """Function for calculating the average grade of students."""
    total_grade = 0
    student_count = 0

    # Read data from a CSV file.
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_grade += int(row["Mark"])  # Add the mark to the total amount.
            student_count += 1  # Count the number of students.

    # Calculate the average score.
    if student_count > 0:
        average_grade = total_grade / student_count
        print(f"Average student mark: {average_grade:.2f}")
    else:
        print("There are no students in the file to calculate the average grade.")


def add_student(file_path, name, age, mark):
    """
    Function to add a new student to a CSV file
    :param file_path: file_path.
    :param name: str.
    :param age: int.
    :param mark: int.
    """

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, mark])
    print(f"Student {name} was successfully added.")


calculate_average_grade(file_path)

# Add a new student.
name = input("Enter the name of the new student: ")
age = input("Enter the age of the new student: ")
mark = input("Enter the mark of the new student: ")

add_student(file_path, name, age, mark)

# Check the average grade after adding a new student.
calculate_average_grade(file_path)

# Reading data from a CSV file.
with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

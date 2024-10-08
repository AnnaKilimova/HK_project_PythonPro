'''Робота з JSON
Створи JSON-файл з інформацією про книги, кожна книга повинна мати:
• Назву • Автора • Рік видання • Наявність (True або False)
Напиши програму, яка:
• Завантажує JSON-файл. • Виводить список доступних книг (наявність True). • Додає нову книгу в цей файл.'''

import json


# Uploading a JSON file
def load_books(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} is not found!")
        return []
    except json.JSONDecodeError:
        print("JSON decoding error!")
        return []


# Print the list of available books (availability = True)
def list_available_books(books):
    available_books = [book for book in books if book["availability"]]
    if available_books:
        print("Available books:")
        for book in available_books:
            print(f"- {book['name']} (Author: {book['author']}, Year: {book['year']})")
    else:
        print("No available books.")


# Adding a new book to a JSON file
def add_book(file_path, new_book):
    books = load_books(file_path)
    books.append(new_book)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

    print(f"The '{new_book['name']}' book successfully has been added to the file.")


# Main programme
if __name__ == "__main__":
    file_path = "books.json"

    # Download books from a file
    books = load_books(file_path)

    # Displaying available books
    list_available_books(books)

    # Get information about a new book
    new_book_title = input("Enter the name of new book: ")
    new_book_author = input("Enter the author of the book: ")
    new_book_year = int(input("Enter the year of the book: "))
    new_book_availability = input("Is the book in stock?? (yes/no): ").lower() == 'yes'

    new_book = {
        "name": new_book_title,
        "author": new_book_author,
        "year": new_book_year,
        "availability": new_book_availability
    }

    # Add a new book to a file
    add_book(file_path, new_book)

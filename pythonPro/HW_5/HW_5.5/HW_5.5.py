'''5. Генератор для створення нескінченної послідовності
Створіть генератор, який генерує нескінченну послідовність парних чисел.
Використайте менеджер контексту для обмеження кількості генерованих чисел до 100 і збереження їх у файл.'''

def even_generator():
    """Generator of an infinite sequence of even numbers."""

    n = 0
    while True:
        yield n
        n += 2


# Context manager for writing numbers to a file
with open("test", "w", encoding="utf-8") as file:
    gen_init = even_generator()  # Ініціалізація генератора
    count = 0

    # Write down the first 100 even numbers
    while count < 100:
        number = next(gen_init)
        file.write(f"{number}\n")
        count += 1

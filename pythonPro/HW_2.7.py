"""Завдання 7: Трекер витрат
Розробити програму для трекінгу витрат, яка використовує глобальні змінні
для зберігання загальної суми витрат.
1. Створити глобальну змінну total_expense і функцію add_expense, яка
   приймає суму витрат і додає її до загальної суми.
2. Додати функцію get_expense, яка повертає загальну суму витрат.
3. Створити інтерфейс (консольний), щоб користувач міг додавати витрати і
   переглядати загальну суму."""

total_expense = 0


def add_expense(amount):
    global total_expense
    total_expense += amount
    return f"AN EXPENSE OF {amount} HAS BEEN ADDED"


def get_expense():
    return f"TOTAL AMOUNT OF EXPENSES IS: {total_expense}"


def interface():
    while True:
        print(
            """Select one of the actions:
        1. Add expense
        2. Show expenses
        3. Exit"""
        )

        choice = input("Make your choice(1||2||3): ")

        if choice == "1":
            try:
                add_expense(float(input("Enter the amount of expenses: ")))
            except ValueError:
                print("Enter the correct number!")

        elif choice == "2":
            print(get_expense())

        elif choice == "3":
            print("PROGRAMME COMPLETE")
            break

        else:
            print("INCORRECT CHOICE. TRY AGAIN")


interface()

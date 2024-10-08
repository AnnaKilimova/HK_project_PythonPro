'''Завдання 10: Створення товарів для онлайн-магазину
Розробити програму для управління товарами в онлайн-магазині,
використовучи карирувані функції.
1. Написати функцію create_product, яка приймає назву, ціну та кількість товару.
2. Використати замикання для створення функції, яка дозволяє змінювати ціну товару.'''


def create_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }

    def change_price(new_price):
        nonlocal product
        product['price'] = new_price
        return f"The price of '{product['name']}' was changed to {product['price']}£"

    return product, change_price

set_product, set_price = create_product('IPad', 800, 100)
print(f"Name: {set_product['name']}, Price: {set_product['price']}£, Quantity: {set_product['quantity']}")
print(set_price(700))
print(f"Name: {set_product['name']}, Price: {set_product['price']}£, Quantity: {set_product['quantity']}")

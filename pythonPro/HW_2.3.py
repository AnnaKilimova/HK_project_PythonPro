"""Завдання 3: Магазин замовлень з акційними знижками
Написати програму, яка імітує систему замовлення з акціями, де знижки
зберігаються у глобальній області, а нарахування знижки відбувається
локально для кожного клієнта.
1. Створити глобальну змінну discount = 0.1 (10% знижка).
2. Створити функцію create_order, яка приймає ціну товару як аргумент
   і всередині:
   • обчислює кінцеву ціну з урахуванням знижки, що визначена глобальною.
   • створює вкладену функцію apply_additional_discount, яка додає додаткову
     знижку (наприклад, для VIP-клієнтів) і змінює фінальну ціну.
3. Використати ключове слово nonlocal, щоб функція могла змінювати кінцеву
   ціну у вкладеній області видимості.
4. Після застосування всіх знижок вивести фінальну ціну."""

discount = 0.1


def create_order(price):
    final_price = price - (price * discount)

    def apply_additional_discount(clienType):
        nonlocal final_price
        if clienType == 'VIP':
            final_price /= 2
            return final_price
        return final_price

    return apply_additional_discount


print(create_order(1000)('Usual'))
print(create_order(1000)('VIP'))

"""Завдання 2: Менеджер підписки на розсилку
Створити програму, яка імітує менеджер підписки на розсилку, демонструючи
роботу з локальними, глобальними та вкладеними областями видимості.
1. На глобальному рівні створити змінну subscribers = [] —
   це список для збереження імен підписників.
2. Створити функцію subscribe, яка приймає ім'я підписника як аргумент
   і додає його до списку підписників.
3. В середині функції subscribe створити вкладену функцію
   confirm_subscription, яка повертає повідомлення:
   "Підписка підтверджена для <ім'я>".
4. Створити функцію unsubscribe, яка приймає ім'я та видаляє його зі списку
   підписників. Якщо таке ім'я не знайдено, повертає відповідне повідомлення.
5. Використати програму для додавання кількох підписників, підтвердження
   підписки та відписки."""

subscribers = []


def subscribe(name):
    subscribers.append(name)

    def confirm_subscription():
        return f"Підписка підтверджена для {name}"

    return confirm_subscription()


def unsubscribe(name):
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} успішно відписаний"
    else:
        return f"Iм'я {name} не знайдено,"


print(subscribe("Олена"))
print(subscribe("Ігор"))
print(unsubscribe("Ігор"))
print(unsubscribe("Вася"))
print(f"Підписники: {subscribers}")

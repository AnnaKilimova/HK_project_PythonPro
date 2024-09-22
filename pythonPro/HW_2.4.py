"""Завдання 4: Таймер для тренування
Розробити програму, яка симулює таймер для тренувань із вбудованою
функцією, що дозволяє змінювати час тренування на кожному кроці.
1. Створити глобальну змінну default_time = 60, яка задає стандартний
   час на кожне тренування (у хвилинах).
2. Створити функцію training_session, яка:
   • приймає кількість раундів тренування.
   • використовує змінну time_per_round, що відповідає за час на раунд, і
     локально змінює її для кожного тренування.
   • в середині функції створити вкладену функцію adjust_time, яка
     дозволяє налаштовувати час для кожного окремого раунду
     (через неявне використання nonlocal).
3. Програма повинна виводити тривалість кожного раунду тренування."""

default_time = 60


def training_session(number):
    time_per_round = default_time

    def adjust_time():
        nonlocal time_per_round
        if number > 1:
            for _ in range(1, number):
                time_per_round -= 5
        print(f"Раунд {number}: {time_per_round} хвилин")

    return adjust_time()


training_session(1)
training_session(2)
training_session(3)
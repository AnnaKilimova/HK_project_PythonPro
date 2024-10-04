# 2. Ітератор для генерації унікальних ідентифікаторів
# Створіть ітератор, який генерує унікальні ідентифікатори (наприклад, на основі UUID або хеш-функції).
# Ідентифікатори повинні генеруватися один за одним при кожній ітерації, і бути унікальними.

import uuid

def unique_id_iterator():
    '''Iterator for generating unique identifiers.'''

    while True:
        # The uuid module implements universal unique identifiers
        # The uuid.uuid1() function may violate privacy because it creates an identifier containing
        # the network address of the computer, so use uuid.uuid4() creates a random UUID.
        yield uuid.uuid4()

# Select the number of unique identifiers we need to generate and use 'next' to get them.
for _ in range(3):
    print(next(unique_id_iterator()))


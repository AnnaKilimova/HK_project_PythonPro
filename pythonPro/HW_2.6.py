'''Завдання 6: Калькулятор з використанням замикань
Створити калькулятор, який використовує замикання для створення функцій
додавання, віднімання, множення та ділення.
1. Написати функцію create_calculator, яка приймає оператор (наприклад,
   '+', '-', '*', '/') та повертає функцію для виконання обчислень.
2. Використати цю функцію, щоб створити калькулятор для кількох операцій,
   і протестувати його.'''


def create_calculator(operator, number_1=4, number_2=2):
    def add():
        return number_1 + number_2

    def subtract():
        return number_1 - number_2

    def multiply():
        return number_1 * number_2

    def divide():
        return number_1 / number_2

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()


print(create_calculator('+'))
print(create_calculator('-'))
print(create_calculator('*'))
print(create_calculator('/', 14, 2))

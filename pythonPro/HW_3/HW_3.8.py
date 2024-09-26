'''8. Price class discussion before the PaymentGateway implementation
1. Реалізуйте клас Price, що представляє ціну товару з можливістю заокруглення до двох
   десяткових знаків. Додайте методи для додавання, віднімання та порівняння цін.
2. Поміркуйте, як клас Price може бути використаний в майбутньому класі
   PaymentGateway для обробки фінансових транзакцій.'''

class Price:
    def __init__(self, amount):
        '''Rounding to two decimal places'''
        self.amount = round(float(amount), 2)

    def __add__(self, other):
        '''Add'''
        if isinstance(other, Price):
            return Price(self.amount + other.amount)
        raise TypeError("Only add Price to Price")

    def __sub__(self, other):
        '''Sub'''
        if isinstance(other, Price):
            return Price(self.amount - other.amount)
        raise TypeError("Only subtract Price from Price")

    def __lt__(self, other):
        '''Comparison of prices (less)'''
        if isinstance(other, Price):
            return self.amount < other.amount
        raise TypeError("Only compare Price with Price")

    def __eq__(self, other):
        '''Comparison of prices (equal)'''
        if isinstance(other, Price):
            return self.amount == other.amount
        return False

    def __str__(self):
        return f"{self.amount:.2f} £"

price_1 = Price(10.999)
price_2 = Price(4.459)

print(f"Add: {price_1} + {price_2} = {price_1 + price_2}")
print(f"Sub: {price_1} - {price_2} = {price_1 - price_2}")

print(f"{price_1} < {price_2}: {price_1 < price_2}")
print(f"{price_1} == {price_2}: {price_1 == price_2}")

# The Price class can be used in the future PaymentGateway class as follows:
# Counting Price objects to get the total amount of the order
# Subtraction in case of returning goods
# Checking that the payment corresponds to the price
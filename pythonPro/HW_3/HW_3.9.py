'''9. Порівняння сеттерів/геттерів, декоратора @property та дескрипторів
Реалізуйте клас Product, який представляє товар з наступними атрибутами:
1. name – назва товару (рядок). 2.	price – ціна товару (число з плаваючою комою).
Вам потрібно реалізувати три варіанти роботи з атрибутом price:
1. Сеттери/геттери: реалізуйте методи get_price() і set_price(), які будуть дозволяти
   отримувати та встановлювати значення атрибута price. Додайте перевірку, що ціна не може
   бути від'ємною. Якщо ціна менше 0, викиньте виняток ValueError.
2. Декоратор @property: використайте декоратор @property для створення властивості price.
   Також реалізуйте перевірку на від'ємне значення ціни.
3. Дескриптори: створіть окремий клас дескриптора PriceDescriptor, який буде контролювати встановлення
   та отримання ціни. Додайте до класу Product атрибут price, що використовує дескриптор для перевірки ціни.
Завдання:
1. Реалізуйте всі три класи: ProductWithGetSet, ProductWithProperty та ProductWithDescriptor.
2. Напишіть тестову програму, яка створює об'єкти кожного з цих класів та намагається:
   • Отримати та змінити ціну товару.
   • Встановити від'ємне значення ціни та впевнитись, що воно правильно обробляється (викидання ValueError).
3. Порівняйте переваги та недоліки кожного з підходів (сеттери/геттери, @property, дескриптори).
   Напишіть висновок, який підхід більш зручний у вашому випадку та чому.
Додаткове завдання (опціонально):
4. Для класу з дескриптором додайте можливість встановлення значень ціни в євро або доларах (через додатковий атрибут валюти), використовуючи ще один дескриптор для конвертації валют.'''

class ProductWithGetSet:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price_value):
        if price_value < 0:
            raise ValueError("The price cannot be negative")
        self._price = price_value

    def __repr__(self):
        return f"ProductWithGetSet(name={self.name}, price={self._price})"


class ProductWithProperty:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def my_price(self):
        return self._price

    @my_price.setter
    def my_price(self, value):
        if value < 0:
            raise ValueError("The price cannot be negative")
        self._price = value

    def __repr__(self):
        return f"ProductWithProperty(name={self.name}, price={self._price})"


class PriceDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("The price cannot be negative")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class CurrencyDescriptor:
    exchange_rates = {"USD": 1, "GBP": 0.74}  # Base currency and Conversion rate

    def __init__(self, price_descriptor):
        self.price_descriptor = price_descriptor

    def __get__(self, instance, owner):
        price_in_usd = self.price_descriptor.__get__(instance, owner)
        currency = instance.currency
        return price_in_usd * self.exchange_rates[currency]

    def __set__(self, instance, value):
        currency = instance.currency
        if value < 0:
            raise ValueError("The price cannot be negative")
        price_in_usd = value / self.exchange_rates[currency]
        self.price_descriptor.__set__(instance, price_in_usd)

    def __set_name__(self, owner, name):
        self.name = name


class ProductWithDescriptor:
    price = PriceDescriptor()  # Descriptor for the price
    price_in_currency = CurrencyDescriptor(price)  # Descriptor for conversion

    def __init__(self, name, price, currency="USD"):
        self.name = name
        self.price = price
        self.currency = currency  # The currency can be USD or GBP

    def __repr__(self):
        return f"Product: name={self.name}, price={self.price_in_currency:.2f}"


def test_product_classes():
    # Testing ProductWithGetSet
    try:
        product_with_get_set = ProductWithGetSet("Ipad", 800)
        print(product_with_get_set)
        product_with_get_set.set_price(750)
        print(f"Updated price: {product_with_get_set.get_price()}")
        product_with_get_set.set_price(-500)  # May cause ValueError
    except ValueError as e:
        print(f"ProductWithGetSet error: {e}")

    # Testing ProductWithProperty
    try:
        product_with_property = ProductWithProperty("IPhone", 1100)
        print(product_with_property)
        product_with_property.price = 900
        print(f"Updated price: {product_with_property.price}")
        product_with_property.price = -500  # May cause ValueError
    except ValueError as e:
        print(f"ProductWithProperty error: {e}")

    # Testing ProductWithDescriptor
    try:
        product_with_descriptor = ProductWithDescriptor("MacBook", 1500)
        print(product_with_descriptor, product_with_descriptor.currency)
        product_with_descriptor.price = 1000
        product_with_descriptor.currency = "GBP"
        print(f"Updated price: {product_with_descriptor.price}{product_with_descriptor.currency}")
        product_with_descriptor.price = -500  # May cause ValueError
    except ValueError as e:
        print(f"ProductWithDescriptor error: {e}")


# Running tests
test_product_classes()


# Висновок.
# Дескриптори це найзручний підхід, бо вони дозволяють гнучко керувати встановленням і отриманням значень атрибутів.
# Легше можно налаштувати додаткову логіку.
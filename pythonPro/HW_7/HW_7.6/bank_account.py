"""Завдання 6. Приклад комплексного тестування
Розробіть програму для роботи з банківськими транзакціями та протестуйте її за допомогою фікстур, моків, скіпів
та параметризації. Напишіть клас BankAccount, який реалізує методи:
• deposit(amount: float): поповнення рахунку;
• withdraw(amount: float): зняття коштів (якщо достатньо коштів на рахунку).
• get_balance() -> float: повертає поточний баланс."""


class BankAccount:
    """Work with banking transactions."""

    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        """Account top-up."""
        if amount <= 0:
            raise ValueError("The deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: float):
        """Withdrawal of funds (if there are enough funds on the account)."""
        if amount <= 0:
            raise ValueError("The withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds in the account.")
        self.balance -= amount

    def get_balance(self) -> float:
        """Returning the current balance"""
        return self.balance

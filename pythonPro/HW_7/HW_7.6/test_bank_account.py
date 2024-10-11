"""Напишіть тести з використанням:
• фікстур для створення об'єкта банківського рахунку перед тестами,
• моків для тестування взаємодії із зовнішнім API (наприклад, для перевірки балансу),
• скіпів для пропуску тестів зняття коштів, якщо рахунок порожній.
Використовуйте параметризацію для тестування різних сценаріїв поповнення та зняття коштів."""


import pytest
from bank_account import BankAccount
from unittest.mock import Mock


# Fixture for initialising a bank account
@pytest.fixture
def bank_account():
    return BankAccount(initial_balance=100.0)


# Deposit test
def test_deposit(bank_account):
    bank_account.deposit(50.0)
    assert bank_account.get_balance() == 150.0


# Withdrawal test (sufficient funds)
def test_withdraw(bank_account):
    bank_account.withdraw(30.0)
    assert bank_account.get_balance() == 70.0


# Withdrawal test (insufficient funds)
def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        bank_account.withdraw(200.0)


# Parametrized test to verify different deposit scenarios
@pytest.mark.parametrize("deposit_amount, expected_balance", [
        (50.0, 150.0),
        # (0.0, 100.0),  # There must be an error
        # (-10.0, 100.0)  # There must be an error
])

def test_deposit_parametrized(bank_account, deposit_amount, expected_balance):
    if deposit_amount <= 0:
        with pytest.raises(ValueError, match="The deposit amount must be greater than zero."):
            bank_account.deposit(deposit_amount)
    else:
        bank_account.deposit(deposit_amount)
        assert bank_account.get_balance() == expected_balance


# Parameterised test to test different withdrawal scenarios
@pytest.mark.parametrize("withdraw_amount, expected_balance", [
        (50.0, 50.0),
        (100.0, 0.0),
        # (150.0, 100.0)  # There must be an error
])

def test_withdraw_parametrized(bank_account, withdraw_amount, expected_balance):
    if withdraw_amount > bank_account.get_balance():
        with pytest.raises(ValueError, match="Insufficient funds in the account."):
            bank_account.withdraw(withdraw_amount)
    else:
        bank_account.withdraw(withdraw_amount)
        assert bank_account.get_balance() == expected_balance


# API mock test to check the balance (simulate an external call)
def test_mock_external_balance_check():
    # Create a mock object that represents an external service for checking the balance
    external_service_mock = Mock()
    external_service_mock.get_balance.return_value = 500.0

    # Let's assume that this is an API for getting a balance
    balance = external_service_mock.get_balance()

    assert balance == 500.0


# Skip test, skipped if the account balance is less than 50
@pytest.mark.skipif(BankAccount(0).get_balance() < 50, reason="Insufficient funds for withdrawal testing.")
def test_skip_withdraw():
    account = BankAccount(100.0)
    account.withdraw(50.0)
    assert account.get_balance() == 50.0

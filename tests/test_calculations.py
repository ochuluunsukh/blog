import pytest
from app.calculations import add, BankAccount


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (5, 7, 12)])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

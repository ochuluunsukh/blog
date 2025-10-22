def add(num1: int, num2: int) -> int:
    return num1 + num2


class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance = 1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance (self):
        new_balance = self.account.get_balance()
        assert new_balance == 1000

    def test_transfer(self):
        other_account = BankAccount(balance = 500)
        new_balance, other_balance = self.account.transfer(800, other_account)
        assert new_balance == 700
        assert other_balance == 800

    def test_transfer_insufficient_funds(self):
        other_account = BankAccount(balance = 500)
        with self.assertRaises(ValueError):
            self.account.transfer(1200, other_account)
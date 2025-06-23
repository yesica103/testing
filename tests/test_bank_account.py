import unittest 
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    def setUp(self) -> None:
        import os
        self.account = BankAccount(balance = 1000, log_file = 'transaction_log.txt')
    
    def tearDown(self) -> None:
        import os
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    def _count_lines(self, filename):
        with open(filename, 'r') as r:
            return len(r.readlines())

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
        assert new_balance == 200
        assert other_balance == 1300

    def test_transfer_insufficient_funds(self):
        other_account = BankAccount(balance = 500)
        with self.assertRaises(ValueError):
            self.account.transfer(1200, other_account)

    def test_transaction_log(self):
        import os
        self.account.deposit(500)
        assert os.path.exists(self.account.log_file)

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

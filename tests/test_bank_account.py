import unittest 
import requests
from src.bank_account import BankAccount

def api_is_available():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/COP"
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False


class BankAccountTests(unittest.TestCase):
    def setUp(self) -> None:
        import os
        self.account = BankAccount(balance = 1000, log_file = 'transaction_log.txt')
        self.account2 = BankAccount(balance = 10000000, log_file = 'transaction_log.txt')
    
    def tearDown(self) -> None:
        import os
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
    
    def _count_lines(self, filename):
        with open(filename, 'r') as r:
            return len(r.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        #assert new_balance == 1500
        self.assertEqual(new_balance, 1500, 'El balance no es igual')

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        #assert new_balance == 800
        self.assertEqual(new_balance, 800, 'El balance no es igual')

    def test_get_balance (self):
        new_balance = self.account.get_balance()
        #assert new_balance == 1000
        self.assertEqual(new_balance, 1000, 'El balance no es igual')
    
    def test_transfer(self):
        other_account = BankAccount(balance = 500)
        new_balance, other_balance = self.account.transfer(800, other_account)
        #assert new_balance == 200
        #assert other_balance == 1300
        self.assertEqual(new_balance, 200, 'El balance no es igual')
        self.assertEqual(other_balance, 1300, 'El balance no es igual')

    def test_transfer_insufficient_funds(self):
        other_account = BankAccount(balance = 500)
        with self.assertRaises(ValueError):
            self.account.transfer(1200, other_account)

    def test_transaction_log(self):
        import os
        self.account.deposit(500)
        #assert os.path.exists(self.account.log_file)
        self.assertTrue(os.path.exists(self.account.log_file), 'El archivo de log no existe')

    @unittest.skipUnless(api_is_available(), "La API de tipo de cambio no está disponible.")
    def test_transferencia_exitosa_usd(self):
        resultado = self.account2.transfer_foreign_currency(100, "USD")  # Transferir 100 USD
        self.assertTrue(resultado, "La transferencia en USD debería ser exitosa con suficiente saldo.")
    
    @unittest.skipUnless(api_is_available(), "La API de tipo de cambio no está disponible.")
    def test_transferencia_exitosa_eur(self):
        resultado = self.account2.transfer_foreign_currency(100, "EUR")  # Transferir 100 EUR
        self.assertTrue(resultado, "La transferencia en EUR debería ser exitosa con suficiente saldo.")

    @unittest.skipUnless(api_is_available(), "La API de tipo de cambio no está disponible.")
    def test_transferencia_fondos_insuficientes(self):
        resultado = self.account2.transfer_foreign_currency(10000000000000000, "USD")  # Intentar transferir 500 USD
        self.assertFalse(resultado, "La transferencia debería fallar por fondos insuficientes.")

    @unittest.skipUnless(api_is_available(), "La API de tipo de cambio no está disponible.")
    def test_moneda_inexistente(self):
        resultado = self.account2.transfer_foreign_currency(1000000000000000000000, "XYZ")  # Moneda que no existe
        self.assertFalse(resultado, "La transferencia debería fallar con moneda inexistente.")

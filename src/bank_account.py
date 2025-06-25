import requests
class BankAccount:
    def __init__(self, balance = 0, log_file = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f'{message}\n')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'Fueron despositados {amount}. El nuevo saldo es {self.balance}')
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f'Fueron retirados {amount}. El nuevo saldo es {self.balance}')
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f'Saldo consultado. El saldo actual es {self.balance}')
        return self.balance

    def transfer(self, amount, other_account):
        if amount > 0 and self.balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)
            self._log_transaction(f'Transferencia de {amount} realizada. El nuevo saldo es {self.balance}')
            self._log_transaction(f'Transferencia recibida de {amount}. El nuevo saldo es {other_account.get_balance()}')
        else:
            self._log_transaction(f'Saldo insuficiente para la transferencia de {amount}. El saldo actual es {self.balance}')
            raise ValueError("Insufficient funds or invalid amount")
        
        return self.balance, other_account.get_balance()
    '''
    Metodo que se encarga de acceder a una API para obtener el tipo de cambio de una moneda en especifico (USD, EUR, GBP, etc.)
    '''
    def get_exchange_rate(self, currency_api):
        try:
            url_api = f'https://api.exchangerate-api.com/v4/latest/{currency_api}'
            response = requests.get(url_api, timeout=5)
            if response.status_code == 200:
                data = response.json()
                rate = data ["rates"].get(currency_api)
                if rate:
                    return rate
                else:
                    self._log_transaction(f'No se pudo obtener la tasa de cambio para {currency_api}')
                return None
        except Exception as e:
            self._log_transaction(f'Error al obtener la tasa de cambio: {str(e)}')
            return None 

"""
Realiza una transferencia en la moneda deseada, descontando el equivalente en COP.
"""
def transfer_foreign_currency(self, amount_target_currency, currency_api="USD"):
        
        rate = self.get_exchange_rate(currency_api)
        if rate is None:
            self._log_transaction(f"No se pudo obtener la tasa para {currency_api}. Transferencia cancelada.")
            return False

        required_cop = amount_target_currency / rate

        if self.balance >= required_cop:
            self.balance -= required_cop
            self._log_transaction(f"Transferencia exitosa: {amount_target_currency} {currency_api} ({required_cop:.2f} COP descontados).")
            return True
        else:
            self._log_transaction(f"Fondos insuficientes para transferir {amount_target_currency} {currency_api}. Saldo: {self.balance:.2f} COP")
            return False
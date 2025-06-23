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
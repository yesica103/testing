class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_account):
        if amount > 0 and self.balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)
        else:
            raise ValueError("Insufficient funds or invalid amount")
        return self.balance, other_account.get_balance()
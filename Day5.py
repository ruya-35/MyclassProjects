
class Account:

    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_number = account_num
        self._balance = balance  

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("No negative value")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Balance not sufficient")
        elif amount <= 0:
            raise ValueError("No negative value")
        else:
            self._balance -= amount

    def statement(self):
        print(f"Account --- {self.owner}--- Acc num: {self.account_number} --- Balance:{self._balance} ETB")


class SavingsAccount(Account):

    def __init__(self, owner, account_num, balance=0, rate=0.05):
        super().__init__(owner, account_num, balance)
        self.rate = rate

    def add_interest(self):
        interest = self._balance * self.rate
        self.deposit(interest)

    def statement(self):
        print(f"Savings Account --- {self.owner} --- Acc num: {self.account_number} --- Balance: {self._balance} ETB --- Rate: {self.rate}"
        )


class CurrentAccount(Account):

    def __init__(self, owner, account_num, balance=0, overdraft=10000):
        super().__init__(owner, account_num, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft:
            raise ValueError("Over limit")
        self._balance -= amount

    def statement(self):
        print(f"Current Account --- {self.owner} --- Acc num: {self.account_number} --- Balance: {self._balance}ETB --- Overdraft: {self.overdraft}"
        )


accounts = [
    SavingsAccount("Almaz", "SA-101", 1500, 0.05),
    CurrentAccount("Dawit", "CA-202", 800, 1000),
    SavingsAccount("Selam", "SA-104", 7000, 0.05),
    CurrentAccount("Biruk", "CA-206", 8000, 100),
]

for acc in accounts:
    acc.statement()  
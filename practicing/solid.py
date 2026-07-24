class Account:
    def __init__(self, account_owner, account_number, balance=0):
        self.account_owner = account_owner
        self.account_num = account_number
        self._balance = balance
        self._observers = []  

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)


    def deposit(self, amount):
        self._balance += amount
        self._notify(f"{self.account_owner} deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount
        self._notify(f"{self.account_owner} withdrew {amount}. New balance: {self._balance}")

    def statement(self):
        print(f"Account Name: {self.account_owner}\nAccount Number: {self.account_num}\nBalance: {self._balance}")


class SavingsAccount(Account):
    def __init__(self, account_owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_owner, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._notify(f"Interest added: {interest}. New balance: {self.balance}")

    def statement(self):
        super().statement()
        print(f"Interest Rate: {self.interest_rate}")


class CurrentAccount(Account):
    def __init__(self, account_owner, account_number, balance=0, overdraft_limit=10000):
        super().__init__(account_owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Transaction declined: Exceeds overdraft limit.")
        else:
            self.balance -= amount
        self._notify(f"{self.account_owner} withdrew {amount} (using overdraft). New balance: {self.balance}")

    def statement(self):
        super().statement()
        print(f"Overdraft Limit: {self.overdraft_limit}")



class AccountFactory:
    @staticmethod           #cant be changed
    def create(kind, owner, number, balance=0):
        kind = kind.lower()
        if kind == "savings":
            return SavingsAccount(owner, number, balance, interest_rate=0.05)
        elif kind == "current":
            return CurrentAccount(owner, number, balance, overdraft_limit=10000)
        else:
            raise ValueError(f"Unknown account type: {kind}")


class SMSAlert:
    def update(self, event):
        print(f"[TeleBirr SMS] {event}")

class AuditLog:
    def update(self, event):
        print(f"[Log] {event}")



DW = AccountFactory.create("current", "Dawit", "CBE-2", balance=10000)
DW.subscribe(SMSAlert())
DW.subscribe(AuditLog())
DW.deposit(3000)


SC= AccountFactory.create("savings", "Selam", "CBE-4", balance=7000)
SC.subscribe(SMSAlert())
SC.subscribe(AuditLog())
SC.withdraw(2000)
class Account:

    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_number = account_num
        self._balance = balance  
        self._observers = []

    @property
    def balance(self):
        return self._balance
    
    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, event): 
        for observer in self._observers:
            observer.update(event)

    def deposit(self, amount):
        if amount <= 0: 
            raise ValueError("No negative value")
        self._balance += amount
        self._notify(f"Deposited {amount} ETB to {self.account_number}") 

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Balance not sufficient")
        elif amount <= 0:
            raise ValueError("No negative value")
        else:
            self._balance -= amount
            self._notify(f"Withdrew {amount} ETB from {self.account_number}") 

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
        elif amount <= 0: 
            raise ValueError("No negative value")
        else:
            self._balance -= amount
            self._notify(f"Withdrew {amount} ETB from {self.account_number}")

    def statement(self):
        print(f"Current Account --- {self.owner} --- Acc num: {self.account_number} --- Balance: {self._balance}ETB --- Overdraft: {self.overdraft}"
        )

class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown type: {kind}")


class SMSAlert:
    def update(self, event):
        print(f"[TeleBirr SMS] {event}")

class AuditLog:
    def update(self, event):
        print(f"[Log] {event}")


acc1 = AccountFactory.create("current", "Dawit", "CBE-2")
acc1.subscribe(SMSAlert())
acc1.subscribe(AuditLog())
acc1.withdraw(5000)
acc1.statement()



acc2 = AccountFactory.create("savings", "Alem", "CBE-3", balance=2000)
acc2.subscribe(SMSAlert())
acc2.subscribe(AuditLog())
acc2.deposit(1000)       
acc2.add_interest()      
acc2.statement()



acc3 = AccountFactory.create("current", "Selam", "CBE-4", balance=500)
acc3.subscribe(SMSAlert())
acc3.subscribe(AuditLog())
acc3.withdraw(200)      
acc3.statement()
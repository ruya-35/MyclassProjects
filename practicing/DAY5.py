#Inheritance

# class Account:
#     def __init__(self, owner, balance):
#         self.owner=owner
#         self.balance=balance
#     def deposite(self, amount):
#         self.balance+=amount

# class SavingAccount(Account):
#     pass

# s=SavingAccount("Alem", 2000)
# s.deposite(500)
# print(s.balance)


#Using super


# class SavingAccount(Account):
#     def __init__(self, owner, balance, rate):
#         super().__init__(owner, balance)
#         self.rate=rate
#     def add_interest(self):
#         interest = self.balance * (self.rate / 100)
#         self.deposite(interest)             #reusing parent method

# s=SavingAccount("Alem", 5000, 10)
# s.add_interest()
# s.deposite(500)
# print(s.balance)



#Method Overriding


# class Account:
#     def __init__(self, owner, balance):
#         self.owner=owner
#         self.balance=balance
#     def statment(self):
#         print(f"{self.owner} : {self.balance}")

# class CurrentAccount(Account):
#     def statment(self):
#         print(f"[current] {self.owner}: "
#                 f"{self.balance} ETB")
        
# s=CurrentAccount("Selam Alemu", 5000)
# s.statment()





#Polymorphism


# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# class Duck:
#     def speak(self):
#         return "Quack!"

# animals = [Dog(), Cat(), Duck()]

# for animal in animals:
#     print(animal.speak())





#Abstarction


# from abc import ABC, abstractmethod
# class Account(ABC):

#     @abstractmethod
#     def calculate_interest(self):
#         pass

# class SavingsAccount(Account):

#     def __init__(self, balance):
#         self.balance = balance

#     def calculate_interest(self):
#         return self.balance * 0.5

# class CurrentAccount(Account):

#     def __init__(self, balance):
#         self.balance = balance

#     def calculate_interest(self):
#         return 0
    
# savings = SavingsAccount(1000)
# current = CurrentAccount(1000)

# print(savings.calculate_interest())
# print(current.calculate_interest())





#Composition



# class Account:
#     def _init_(self):
#         self.history = ( TransactionHistory())




class Account:

    def __init__(self, owner, number, _balance=0):
        self.owner = owner
        self.number = number
        self._balance = _balance

    def deposit(self, amount):
        self._balance += amount

    def statement(self):
        print(f"Owner: {self.owner} --- Balance: {self._balance} ETB")


class SavingsAccount(Account):

    def __init__(self, owner, num, balance=0, rate=0.05):
        super().__init__(owner, num, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self._balance * self.rate)


class CurrentAccount(Account):

    def __init__(self, owner, num, balance=0, od=1000):
        super().__init__(owner, num, balance)
        self.overdraft = od

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft:
            raise ValueError("Over limit")
        self._balance -= amount


bank = [
    SavingsAccount("Almaz", "CBE-1", 1500),
    CurrentAccount("Dawit", "CBE-2", 800),
]

for acc in bank:
    acc.deposit(100)  
    acc.statement()  
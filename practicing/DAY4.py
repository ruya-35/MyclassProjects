#class and objcect + Encapsulation


# class Account:
#     def __init__(self, owner, bal):    
#         self.owner=owner
#         self.balance=bal
    
#     def deposite(self, amount):
#         self.balance+=amount

# a = Account("Almaz", 1500)
# a.deposite(500)
# print(a.balance)





#class and object

# class Account:
#     def __init__(self, owner,bal):
#         self.owner=owner
#         self.balance=bal
#     def deposite(self, amount):
#         self.balance+=amount
#     def withdraw(self, amount):
#         self.balance-=amount
#     def statement(self):
#         print(f"{self.owner} : {self.balance}")

# a=Account("Selam", 5000)
# # a.deposite(500)
# a.withdraw(700)

# b=Account("Bruik", 1000)
# b.deposite(500)

# print(a.statement())

# print(b.statement())






#encapsulation with getter
# class Account:
#     def __init__(self, balance):
#         self.__balance=balance
#     def get_balance(self):
#         return self.__balance
#     def withdraw(self, amount):
#         if amount>self.__balance:
#             print("Balance not sufficent")
#         else:
#             self.__balance -= amount

# a=Account(5000)
# a.withdraw(1000)
# print(a.get_balance())  






#encapsulation with @property
# class Account:
#     def __init__(self, balance):
#         self.__balance=balance
#     @property
#     def balance(self):
#         return self.__balance
#     @balance.setter
#     def balance(self, value):
#         if value<0:
#             raise ValueError("No Negative values")
#         else:
#             self.__balance=value

# a=Account(5000)
# a.balance=100
# b=Account(7000)
# b.balance=10

# print(a.balance)
# print(b.balance)


#encapsulation with @property
class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def deposite(self, amount):
        if amount<=0:
            raise ValueError("No negative value")
        self.__balance+=amount

a=Account("Selam", 5000)
a.deposite=700
print(a.balance)


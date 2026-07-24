
class Account:
    def __init__(self, owner, account_num, balance):
        self.owner=owner
        self.account_number=account_num
        self.__balance=balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def deposite(self, amount):
        if amount<=0:
            raise ValueError("No negative value")
        else:
            self.__balance+=amount
        
    def withdraw(self, amount):
        if amount>self.__balance:
            print("Balance not suffiencent")
        elif amount<=0:
            raise ValueError("No negative value")
        else:
            self.__balance-=amount
    
    def statment(self):
        print(f"{self.owner}---- Account number: {self.account_number}  Current balance : {self.__balance}")


alem=Account("Alem zenebe", "CBE-110", 500)
alem.deposite=100
alem.statment()

selam=Account("Selam Alemu", "CBE-111", 7000)
selam.withdraw(1000) 
selam.statment()
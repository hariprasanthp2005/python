class bank():
    def __init__(self, balance):
        self.balance = balance

    def deposite(self,amount):    
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

acc1=bank(5000)

acc1.deposite(2000) 
print(acc1.balance)  

acc1.withdraw(1500)
print(acc1.balance)




class Account:
    min_balance = 500
    Branch = "SBI Marathalli"

    def __init__(self,id,name,amount):
        self.acc_id= id
        self.acc_name= name
        self.acc_bal= amount

    def deposite(self,balance):    
        self.acc_bal += balance

    def withdraw(self,balance):
        self.acc_bal -= balance

    def get_bal(self):
        return  self.acc_bal-self.min_balance
    
    @classmethod
    def update(cls):
        cls.min_balance=700

    @staticmethod
    def intrest():
        roi=10
        return roi
    
a1=Account(101,"hp",90000)
a2=Account(102,"vk",80000)

print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)

a1.deposite(70000)
a2.withdraw(30000)

print(a1.acc_bal)
print(a2.acc_bal)

print(a1.get_bal())
print(a2.get_bal())

Account.update()

print(a1.get_bal())
print(a2.get_bal())



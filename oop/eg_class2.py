class account:
    min_bal=500

    def open_acc(self):
        print("account oppened succesfully")
    
    def deposit(self):
        print("amount deposited")    

    def withdraw(self):
        print("low balance")   
    
    def get_bal(self):
        print("server too busy") 
    
    def close_acc(self):
        print("account closed succesfully")    

a1=account() 
a2=account()

print(account.__dict__)
print(a1.__dict__)
print(a2.__dict__)


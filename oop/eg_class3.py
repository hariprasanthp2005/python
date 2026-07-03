class account:
    min_bal=500 #static variable
    

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

a1.open_acc()
a1.deposit()
a1.withdraw()
a1.get_bal()
a1.close_acc()




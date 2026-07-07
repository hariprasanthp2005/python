class Account:

    def __init__(self, acc_id, acc_name, acc_bal):
        self.acc_id = acc_id
        self.acc_name = acc_name
        self.acc_bal = acc_bal

    def deposit(self, amount):
        self.acc_bal += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.acc_bal:
            print("Insufficient Balance")
        else:
            self.acc_bal -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print("Account ID :", self.acc_id)
        print("Name       :", self.acc_name)
        print("Balance    :", self.acc_bal)


# Creating Objects
a1 = Account(101, "hp", 90000)
a2 = Account(102, "vk", 80000)

print(a1.__dict__)
print(a2.__dict__)

print("\nAfter Deposit")
a1.deposit(70000)
print(a1.__dict__)

print("\nAfter Withdrawal")
a2.withdraw(30000)
print(a2.__dict__)

print("\nAccount Details")
a1.display()
print()
a2.display()
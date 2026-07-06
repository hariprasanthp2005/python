class Account():
    
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print("construct method")

a1=Account(101,"hp")
a2=Account(102,"vk")

print(a1.__dict__)
print(a2.__dict__)


class account():
    def __init__(self,name,id,amount):
        self.name=name
        self.id=id
        self.amount=amount

a1=account("hp",1,200000)  
a2=account("vk",2,100000)

print(a1.__dict__)
print(a2.__dict__)
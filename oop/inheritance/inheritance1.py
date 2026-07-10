class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Developer(employee):
    def code(self):
        print(self.name ,"is coding")

class Hr(employee):
    def recruit(self):
        print(self.name , "is recruiting")


dev=Developer("hp",1000000)
hr=Hr("vk",200000)  

dev.code()
hr.recruit()


                
class Employee:
    def __init__(self,name,work,salary):
        self.name=name
        self.work=work
        self.salary=salary

    def details(self):
        print("name:",self.name)  
        print("work:",self.work)  
        print("salary:",self.salary)

emp1=Employee("hp","developer",100000000)
emp2=Employee("vk","analyst",50000000)        
emp3=Employee("ab","hr",50000000)
emp4=Employee("cg","analyst",1000000)
emp5=Employee("sg","analyst",1000000)
emp6=Employee("dk","hr",900000)
emp7=Employee("rp","developer",9000000)

emp1.details()
emp2.details()
emp3.details()

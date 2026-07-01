class employees:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def value(self):
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)

emp1=employees("hp","21","male")  
emp2=employees("vk","37","male") 
emp3=employees("sm","28","female") 


emp1.value()
emp2.value()
emp3.value()
        

        
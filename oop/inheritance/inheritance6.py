class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age) 
        self.roll_no=roll_no

class Teacher(Person):
    pass

s1=Student('hari',21,21)
s2=Student('virat',22,37)
s3=Student('abd',23,39)

t1=Teacher('cheeku',39,)
t2=Teacher('veeru',40,)

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(t1.__dict__)
print(t2.__dict__)


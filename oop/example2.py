class Test:
    a=100    #static or class variable

    def m1(self):
        self.b=200
        self.c=300


t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)
print("After calling m1 method id instance method")
t1.m1()

print(t1.__dict__)
print(t2.__dict__)
print(Test.__dict__)
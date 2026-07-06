class test:
    a=50

    def m1(self):
        self.b=100
        self.c=50
    
    @classmethod
    def m2(cls):
        test.d=70
        test.e=90

t1=test()
t1.m1()

t2=test()
t2.m2()
t2.a=150

print(t1.b+t1.c+t2.e)
print(t2.a+t2.d)


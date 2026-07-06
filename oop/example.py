class test:
    a=100

    def m1(self,b,c):
        self.b=200
        self.c=300
    @classmethod
    def m2(cls):
        test.d=400
        
        
t1=test()
t2=test()

t1.m1()
t2.m2()



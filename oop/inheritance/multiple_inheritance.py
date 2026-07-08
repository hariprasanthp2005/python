class p1:
    def m1(self):
        print("parent-1 class-1")

    def m2(self):
        print("parent-1 class-2")

class p2:
    def m2(self):
        print("parent-2 class-1")

class child(p2,p1):
    pass

a=child()

a.m1()
a.m2()


  

        

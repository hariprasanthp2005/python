class GP:
    def m1(self):
        print("parent class m1 method")

class Parent(GP):
    def m2(self):
        print("parent class m2 method")

class Child(Parent):
     def m3(self):
        print("parent class m3 method")

a=Child()

a.m3()
a.m2()
a.m1()



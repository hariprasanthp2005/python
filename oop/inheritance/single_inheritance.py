class Parent:
    def m1(self):
        print("parent class m1 method")

    def m2(self):
        print("parent class m2 method")

    def m3(self):
        print("parent class m3 method")

class Child(Parent):
    pass

a=Parent()

a.m2()
a.m1()
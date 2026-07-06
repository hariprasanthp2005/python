class test:
                       #special method to initilize object value
    def __init__(self):#constructor will execute automatically at the time of object creation only once.
        print("special method")

    def m1(self):
        print("instance method")
    
    @classmethod
    def m2(cls):
        print("cls method")

    @classmethod
    def m3(cls):
        print("class method 2")  

test()                 
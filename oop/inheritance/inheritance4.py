class Employee:

    def __init__(self):
        print("Employee Constructor")


class Developer(Employee):

    def __init__(self):
        super().__init__() 
        print("Developer Constructor")

a1=Developer()        
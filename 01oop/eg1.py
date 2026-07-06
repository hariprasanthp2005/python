class Student:

    def __init__(self, name):
        self.name = name
        name = "Rahul"

hari = Student("Hari")

print(hari.name)

'''
The local variable name initially stores "Hari". Then self.name = name copies that value into the object. Later, even if the local variable changes to "Rahul", the object's attribute self.name is not affected because the copy has already been made.

'''
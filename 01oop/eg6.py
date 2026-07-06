class Student:
    def __init__(self, name):
        self.name = name

hari = Student("Hari")
arun = hari

arun.name = "Ravi"

print(hari.name)
print(arun.name)
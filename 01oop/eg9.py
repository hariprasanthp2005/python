class Student:

    college = "PSG"

    def __init__(self, name):
        self.name = name


hari = Student("Hari")
arun = Student("Arun")

Student.college = "MIT"

print(hari.college)
print(arun.college)
print(Student.college)
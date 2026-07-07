class Student:
    def __init__(self, name):
        self.name = name

hari = Student("Hari")
arun = Student("Arun")

friend = hari

friend.name = "Kumar"

print(hari.name)
print(arun.name)
print(friend.name)
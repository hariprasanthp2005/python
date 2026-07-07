class Student:
    def __init__(self, name):
        self.name = name

hari = Student("Hari")

friend = hari

friend = Student("Kumar")

print(hari.name)
print(friend.name)
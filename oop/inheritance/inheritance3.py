class Employee:

    def __init__(self):
        print("Employee Constructor")


class Developer(Employee):

    def __init__(self):
        print("Developer Constructor")


d = Developer()
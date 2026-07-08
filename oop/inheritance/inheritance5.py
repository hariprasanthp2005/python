class employee:
    def work(self):
        print("working")

    def login(self):
        print("login success")

class developer(employee):
    def write_code(self):
        print("writing code")

class manager(developer):
    def conduct_meeting(self):
        print("conduct meeting")

a1=developer()

a1.login()
a1.work()

b1=manager()

b1.login()

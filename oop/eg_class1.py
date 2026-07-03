class account:
    def __init__(self,account,id):
        self.account=account
        self.id=id

    def value(self):
        print("account:",self.account)
        print("id:",self.id)

a1=account("ab","01")
a2=account("bc","02")
a3=account("cd","03") 

a1.value()
a2.value()
a3.value()

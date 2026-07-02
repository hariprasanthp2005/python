class UPI:
    def pay(self):
        print("payment through UPI")

class CARD:
    def pay(self):
        print("payment through CARD")

class NETBANKING:
    def pay(self):
        print("payment through NETBANKING")

for payment in ([UPI(),CARD(),NETBANKING()]):
    payment.pay()

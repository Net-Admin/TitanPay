# This stores the MailPayment info
from src.Accounting.paymentmethod import PaymentMethod

class MailPayment(PaymentMethod):

    def __init__(self, pay, address):
        PaymentMethod.__init__(self)
        self.pay = pay
        self.address = address

    def pay(self, pay, address):
        return ("Mailing a check for $",self.pay," to ",self.address)

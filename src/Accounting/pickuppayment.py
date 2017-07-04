# This stores the PickupPayment info
from src.Accounting.paymentmethod import PaymentMethod

class PickUpPayment(PaymentMethod):

    def __init__(self, amt):
        PaymentMethod.__init__(self)
        self.amt = amt

    def pay(self, amt):
        return ("A Check for ", self.amt, " is waiting for you at the PostMaster.")

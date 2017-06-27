# This stores the PickupPayment info

class PickUpPayment(PaymentMethod):

    def __init__(self):
        PaymentMethod.__init__()

    def pay(self, pay, Address):
        return ("A Check for ", amt, " is waiting for ", self, " at the PostMaster."

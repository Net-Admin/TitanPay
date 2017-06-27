# This stores the MailPayment info

class MailPayment(PaymentMethod):

    def __init__(self):
        PaymentMethod.__init__()

    def pay(self):self, pay, Address):
        return ("Mailing a check to ",self," for $",pay," to ",Address)

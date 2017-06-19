# This stores the MailPayment info

class MailPayment(PaymentMethod):

    def __init__(self):

    def mail_payment(self, pay, Address):
        return ("Mailing a check to ",self," for $",pay," to ",Address)

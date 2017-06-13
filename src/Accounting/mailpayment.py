# This stores the MailPayment info

class MailPayment(PaymentMethod):

    def __init__(self):
        pass
    
    def mail_payment(self,pay, Address):
        print ("Mailing a check to ",self," for $",pay," to ",Address)

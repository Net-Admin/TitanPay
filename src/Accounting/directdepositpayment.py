import PaymentMethod

class DirectDepositPayment(PaymentMethod):

    def __init__(self):
        PaymentMethod.__init__()

   def pay(self, amt):
        return ("Depositing $", amt, " in", bank_name, " Account Number ", account_id, " Using Routing Number: ", routing_number)

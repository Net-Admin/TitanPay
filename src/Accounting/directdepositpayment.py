# This stores the DirectDeposit info

class DirectDepositPayment(PaymentMethod):

   def pay(self, amt):
        return ("Depositing $", amt, " in", bank_name, " Account Number ", account_id, " Using Routing Number: ", routing_number)

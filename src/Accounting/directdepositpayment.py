from src.Accounting import PaymentMethod

class DirectDepositPayment(PaymentMethod):

    def __init__(self, bank_name, account_id, routing_number):
        PaymentMethod.__init__(self)
        self.bank_name = bank_name
        self.account_id = account_id
        self.routing_number = routing_number

    def pay(self, amt):
        return ("Depositing $", amt, " in", self.bank_name, " Account Number ", self.account_id, " Using Routing Number: ", self.routing_number)

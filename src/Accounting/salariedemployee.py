# This stores the SalaridEmployee information
from datetime import datetime
from src.Accounting.paymentmethod import PaymentMethod
from src.Accounting.employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payment_method)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipts = []
        
    def makeSale(self, double_amt):
        receipt = Receipt(self, transaction_amt)
        self.__receipt_history.append(receipt)
       
    def calculate_pay__(self, start_dt, end_dt):
        commission = 0
        start_dt = 0
        total_pay = 0
        end_dt = start_dt + 28
        for receipts in self.__Receipts:
            if reciepts.get_date() <=start_dt and receipts.get_date() >= end_dt
                total += (self._commission_rate * receipt.get_sale_amount()):
        total -= self.get_union_dues()
        if total <= 0:
            total = 0
        return self.get_payment_method().pay("%s %s" % (self.get_first_name(), self.get_last_name()), total)


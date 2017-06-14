# This stores the SalaridEmployee information

class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, receipts, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        Receipt.__init__(self, employee_id, first_name, last_name, receipt_amt)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipts = []
        
    def makeSale(self, double_amt):
        reciept = receipt(self, transaction_amt)
        self.__receipt_history.append(receipt)
    
    def calculate_pay(self, receipt, commission):
        pay = receipt * commission


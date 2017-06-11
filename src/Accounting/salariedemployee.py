# This stores the SalaridEmployee information

class SalariedEmployee (Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        Receipt.__init__(self, employee_id, first_name, last_name, reciept_amt)
        self.__salary = salary
        self.__commission_rate = commission_rate
        
    def __makeSale(double_amt):
        reciept = Receipt(self, transaction_amt)
        self.__reciept_history.append(Receipt)

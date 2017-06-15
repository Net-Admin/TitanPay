# This stores the SalaridEmployee information

class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        Receipt.__init__(self, employee_id, first_name, last_name, receipt_amt)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipts = []
        
    def makeSale(self, double_amt):
        reciept = receipt(self, transaction_amt)
        self.__receipt_history.append(receipt)
    
    def calculate_pay(self):
        pay = receipt * commission
    
    def calculate_pay__(self, start_dt, end_dt):
        commission = 0
        start_dt = 0
        total_pay = 0
        end_dt = start_dt + 28
        for receipts in self.__Receipts:
            if reciepts.get_date() <=start_dt and receipts.get_date() >= end_dt
                total += receipts.calculate_daily_pay(self.__commission_rate):
        #iterate over the timecards
        # test if date of the timecard is between start_dt & end_dt
        # if yes then call tc.calculate_pay(self, hourly_rate) & add result to total
        pay = total_pay


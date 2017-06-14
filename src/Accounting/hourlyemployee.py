from datetime import datetime
from datetime import timedelta

class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__hourly_rate = hourly_rate
        self.__timecards = []
        self.__payment_method = pay_method
        
    def __date_time(self,datetime):
        now = datetime.datetime.now()
        
    def clockIn(self):
        tc = TimeCard(datetime.now(), datetime.now().time())
        self.__time_cards.append(tc)

    def clockOut(self):
        self.clock_out = datetime.strftime('%m/%d/%Y %H:%M:%S')
        for tc in self.__timecards:
            if tc.get_date() >= current_dt:
                tc.clockOut()

    def calculate_pay__(self, start_dt, end_dt):
        #iterate over the timecards
        # test if date of the timecard is between start_dt & end_dt
        # if yes then call tc.calculate_pay(self, hourly_rate) & add result to total
        pay = time_card * hourly_rate
        time_card = 0

        self.__payment_method.pay(result)
        
        

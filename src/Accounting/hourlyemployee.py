from datetime import datetime
from datetime import timedelta

class HourlyEmployee(Employee, TimeCard):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, clockin, clockout, timecards):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        TimeCard.__init__(self, date, start_time, end_time)
        self.__hourly_rate = hourly_rate
        self.__clockin = clockIn
        self.__clockout = clockOut
        self.__timecards = []
        
    def __date_time(self,datetime):
        now = datetime.datetime.now()
        
    def clockIn(self):
        self.__clock_in = datetime.strftime('%m/%d/%Y %H:%M:%S')
        tc = TimeCard()
        self.__time_cards.append(tc)

    def clockOut(self):
        self.clock_out = datetime.strftime('%m/%d/%Y %H:%M:%S')
        = str(datetime.strftime('%m/%d/%Y %H:%M:%S')) - timedelta(clockin)
        for tc in self.__timecards:
            if tc.get_date() == current_dt:
                tc.clockOut()

    def __calculate_pay__(self, time_card, hourly_rate):
        pay = time_card * hourly_rate
        time_card = 0
        
        

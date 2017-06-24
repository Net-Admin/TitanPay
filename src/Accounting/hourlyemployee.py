from datetime import datetime

class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__hourly_rate = hourly_rate
        self.__payment_method = payment_method
        self.__timecards = []

    def __date_time(self,datetime):
        now = datetime.datetime.now()
        
    def clockIn(self):
        tc = TimeCard(datetime.now(), datetime.now().time())
        self.__time_cards.append(tc)

    def clockOut(self):
         for tc in self.__timecards:
         if tc.get_date() >= current_dt:
                tc.clockOut()

    def calculate_pay__(self, start_dt, end_dt):
        time_cards = 0
        start_dt = 0
        total_pay = 0
        end_dt = start_dt + 14
        for time_cards in self.__time_cards:
            if time_card.get_date() <=start_dt and time_cards.get_date() >= end_dt
                total += time_cards.calculate_daily_pay(self.__hourly_rate):
                pay = time_card * hourly_rate
            total -= self.get_union_dues
            if total <= 0:
                total = 0
        return self.get__payment_method().pay("$s %s" % (self.get_first_name(), self.get_last_name()), total):

        
        

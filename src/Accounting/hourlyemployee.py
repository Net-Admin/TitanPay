from datetime import datetime

class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payment_method)
        self.__hourly_rate = hourly_rate
        self.__timecards = []

    def clockIn(self):
        tc = TimeCard(datetime.now(), datetime.now().time())
        self.__time_cards.append(tc)

    def clockOut(self):
        current_dt = datetime.now()
        for tc in self.__timecards:
            if tc.get_date() == current_dt:
                tc.clockOut()

    def calculate_pay__(self, start_dt, end_dt):
        total_pay = 0
        for time_card in self.__time_card:
            if time_card.get_date() <=start_dt and time_card.get_date() >= end_dt:
                total += time_cards.calculate_daily_pay(self.__hourly_rate)
                total -= self.get_union_dues

            if total <= 0:
                total = 0
        return self.get__payment_method().pay("$s %s" % (self.get_first_name(), self.get_last_name()), total):

        
        

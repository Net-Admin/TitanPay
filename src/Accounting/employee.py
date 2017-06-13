# This stores the Employee information

    from datetime import datetime
    from datetime import timedelta

class Employee :

    def __init__(self, employee_id, first_name, last_name, weekly_dues, clock_in, clock_out, time_cards):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues
        self.__clock_in = clockIn
        self.__clock_out = clockOut
        self.__time_cards = []


    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return self.__last_name + " ," + self.__first_name

    def clockIn(self):
        self.__clock_in = datetime.strftime('%m/%d/%Y %H:%M:%S')
        tc = TimeCard()
        self.__time_cards.append(tc)

    def clockOut(self):
        self.clock_out = datetime.strftime('%m/%d/%Y %H:%M:%S')
        = str(datetime.strftime('%m/%d/%Y %H:%M:%S')) - timedelta(clockin)
        for tc in self.__time_cards:
            if tc.get_date() == current_dt:
                tc.clockOut()


# This stores the TimeCard information

class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def calculate_daily_pay(self, rate):
        hours_worked = end_time - start_time
        if hours_worked > 8:
            pay = (1.5 * rate * (hours_worked - 8)) + 8 * rate
        else:
            rate * hours_worked

        return pay()      

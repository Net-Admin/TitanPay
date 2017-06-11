class HourlyEmployee(Employee, TimeCard):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues, clockIn, clockOut):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        TimeCard.__init__(self, date, start_time, end_time)
        self.__hourly_rate = hourly_rate
        self.__clockIn = ClockIn
        self.__clockOut = ClockOut
        
    def __clockin__(self, TimeCard):
        time_card = TimeCard(self, date, time)
        self.__timecard_history.append(time_card)
        
    def __clockout__(self, TimeCard):
        get (TimeCard)
        time_card = TimeCard(self, date, time)
        
        

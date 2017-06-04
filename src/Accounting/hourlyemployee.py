class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__hourly_rate = hourly_rate

    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return self.__last_name + "," + self.__first_name

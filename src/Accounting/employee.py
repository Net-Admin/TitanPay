# This stores the Employee information

class Employee :

    def __init__(self, employee_id, first_name, last_name, hourly_rate, weekly_dues):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hourly_rate = hourly_rate
        self.__weekly_dues = weekly_dues

    def get_employee_id(self):
        return self.__employee_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_hourly_rate(self):
        return self.__hourly_rate

    def get_weekly_dues(self):
        return self.__weekly_dues
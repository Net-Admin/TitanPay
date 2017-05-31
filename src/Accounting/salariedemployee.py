# This stores the SalaridEmployee information

class SalariedEmployee:

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__weekly_dues = weekly_dues

   def get_employee_id(self):
        return self.__employee_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_salary(self):
        return self.__salary

    def get_commission_rate (self):
        return self.__commission_rate

    def get_weekly_dues(self):
        return self.__weekly_dues
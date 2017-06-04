# This stores the SalaridEmployee information

class SalariedEmployee (Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__salary = salary
        self.__commission_rate = commission_rate

   def get_employee_id(self):
        return self.__salary = salary


   def get_full_name(self):
        return self.__last_name + "," + self.__first_name
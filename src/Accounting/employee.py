# This stores the Employee information
from datetime import date
from datetime import datetime
from datetime import timedelta
from receipt import Receipt
from timecard import TimeCard

class Employee :

    def __init__(self, employee_id, first_name, last_name, weekly_dues):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues
        #self.__payment_method = payment_method

    def get_employee_id(self):
        return self.__employee_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_full_name(self):
        return "%s, %s" % (self.__last_name + " ," + self.__first_name)

    def get_union_dues(self):
        return self.__weekly_dues

    #def get_payment_method(self):
        #return self.__payment_Method

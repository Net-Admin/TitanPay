# This stores the TimeCard information

class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def set_date(self, date):
        self.__date = date

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def set_end_time(self, end_time):
        self.__end_time = end_time

    def get_date(self, date):
        self.__date = date

    def get_start_time(self, start_time):
        self.__start_time = start_time

    def get_end_time(self, end_time):
        self.__end_time = end_time

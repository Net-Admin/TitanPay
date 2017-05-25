# This stores the employee address information

class Address:

    def __init__(self, street_address, city, state, zip):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip

    def set_street_address(self, street_address):
        self.__street_address = street_address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip(self, zip):
        return self.__zip

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip
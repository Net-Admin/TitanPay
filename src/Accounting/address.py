# This stores the Address information

class Address:
    def __init__(self, street_address, city, state, zip):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

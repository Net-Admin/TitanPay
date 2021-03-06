# This stores the Address information

class Address:

    def __init__(self, street_address, city, state, zip):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip

    def get_address(self):
        full_address = self.__street_address + " " + self.__city + " ," + self.__state + " " + self.__zip
        return full_address

# This stores the BankAccount information

class BankAccount:

    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = bank_name()
        self.__routing_nmber = routing_number()
        self.__account_id = account_id()

    def set_bank_name(self, bank_name):
        self.__bank_name = bank_name()

    def set_start_time(self, routing_number):
        self.__routing_nmber = routing_number()

    def set_account_id(self, account_id):
        self.__account_id = account_id()

    def get_bank_name(self, bank_name):
        self.__bank_name = bank_name()

    def get_start_time(self, routing_number):
        self.__routing_nmber = routing_number()

    def get_account_id(self, account_id):
        self.__account_id = account_id()
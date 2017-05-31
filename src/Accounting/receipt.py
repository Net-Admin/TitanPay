# This stores the Receipt information

class Receipt:

    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = sale_amt
        
    def get_date(self):
        return self.__date
    
    def get_sale_amt(self):
        return self.__sale_amt

    

# This stores the Receipt information
import csv

class Receipt:

    def read_receipts(self):

        with open('../Data/receipts.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None) #Skip the header

            for row in header:
                id = row[0]
                first_name = row[1]
                item = row[2]
                unitcost = float(row[3])
                total = float(row[4])

    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = sale_amt
        
    def commission__(self,commission_rate):
        self.__receipt = receipt
        self.__calculate_commission = receipt * commission_rate
        return commission
    

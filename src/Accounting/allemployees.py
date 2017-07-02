import csv
import sys
import pprint

#function to convert a csv file to a list of dictionaries.
#Takes in variable - "all_employees"
def csv_dict_list(all_employees):

    reader = csv.DictReader(open('D://Users/medic/PycharmProjects/TitanPay/src/Accounting/Data/all_employees.csv'), delimiter = ',')
    result = {}
    for row in reader:
        #for column, value in row.items():
            #result.setdefault(column, []).append(line)
        result[row[0]]=row[1:]

    pprint.pprint(result)
import sys
import os
import csv
import datetime
from src.DataBaseFiles.dbcreator import DBCreator
from src.Accounting.hourlyemployee import HourlyEmployee
from src.Accounting.salariedemployee import SalariedEmployee
from src.Accounting.timecard import TimeCard
from src.Accounting.directdepositpayment import DirectDepositPayment
from src.Accounting.mailpayment import MailPayment
from src.Accounting.pickuppayment import PickUpPayment

class Payroll:

    def __init__(self):
        self.__dbcreator = DBCreator()
        self.employees = []

    # looks at hourly_employees
    def read_hourly_employees(self):

        with open('../Data/hourly_employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None) #Skip the header

            for row in reader:
                id = row[0]
                last_name = row[1]
                first_name = row[2]
                hourly_rate = float(row[3])
                try:
                    union_dues = float(row[4])
                except:
                    union_dues = 0.00
                abbr_pay_method = row[5].rstrip(' ').lstrip(' ')

                if abbr_pay_method == 'DD':
                    payment_method = DirectDepositPayment("Generic", 0, 0)
                elif abbr_pay_method == 'PU':
                    payment_method = PickUpPayment()
                elif abbr_pay_method == 'MA':
                    payment_method = MailPayment()

                emp = HourlyEmployee(id, first_name, last_name, hourly_rate, union_dues, payment_method)
                self.employees.append(emp)


    # looks at salaried_employees
    def read_salaried_employees(self):
        with open('../Data/salaried_employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header

            for row in reader:
                id = row[0]
                last_name = row[1]
                first_name = row[2]
                salary = float(row[3])
                commissionrate = float(row[4])
                union_dues = float(row[5])
                abbr_pay_method = row[5].rstrip(' ').lstrip(' ')

                if abbr_pay_method == 'DD':
                    payment_method = DirectDepositPayment("Generic", 0, 0)
                elif abbr_pay_method == 'PU':
                    payment_method = PickUpPayment
                elif abbr_pay_method == 'MA':
                    payment_method = MailPayment

                emp = SalariedEmployee(id, first_name, last_name, salary, commissionrate, union_dues, payment_method)
                self.employees.append(emp)


    # looks at timecards
    def read_timecard(self):

        with open('..src/Accounting/Data/timecards.csv', newline=' ') as csvfile:
            treader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in treader:
                id = row['EmployeeId']
                clock_in = row['In']
                clock_out = row['Out']
                start_dt = row['Date']

    # looks at receipts
    def read_receipts(self):
        with open('.../src/Accounting/Data/receipts.csv', newline=' ') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            #reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:

                id = row['EmployeeId']

                total = float(row['Total'])
                for emp in self.employees:
                    if emp.get_id() == id:
                        emp.make_sale(total)


    def process_payroll(self, label):
        self.read_hourly_employees
        self.read_salaried_employees
        self.read_timcard
        self.read_receipts

        message = ''
        start_dt = datetime.datetime.strptime('5/01/2016', '%m/%d/%Y').date()
        end_dt = datetime.datetime.strptime('5/25/2016', '%m/%d/%Y').date()

        for emp in self._employees:
            message += emp.get_full_name() + '' + emp.calculate_pay(start_dt, end_dt) + '\n'
        label.config(text=message)


        #pay = HourlyEmployees.get(self, pay)
    
        #tkinter.messagebox.showinfo('Response', 'self.payment_method')
                     
#payroll = Payroll()
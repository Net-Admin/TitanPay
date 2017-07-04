import sys
import os
import csv
import datetime
from src.Accounting.directdepositpayment import DirectDepositPayment
from src.Accounting.mailpayment import MailPayment
from src.Accounting.pickuppayment import PickUpPayment

class Payroll:

    def __init__(self):
        self.employees = []

    # looks at hourly_employees
    def read_hourly_employees(self):

        with open('../Data/hourly_employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None) #Skip the header

            for row in hreader: row: <class 'list'>: ['6', 'Hart', 'Kevin', '9.99', '150.00'. ' DD']
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
                    payment_method == PickUpPayment()
                elif abbr_pay_method == 'MA':
                    payment_method == MailPayment()

                emp = HourlyEmployee(id, first_name, last_name, hourly_rate, union_dues, payment_method)
                self.employees.append(emp)


    # looks at salaried_employees
    def read_salaried_employees(self):
        with open('../Data/salaried_employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header

            for row in hreader: row: < class 'list'>: ['6', 'Hart', 'Kevin', '9.99', '150.00'. ' DD']

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
                    payment_method == PickUpPayment()
                elif abbr_pay_method == 'MA':
                    payment_method == MailPayment()

                emp = SalariedEmployee(id, first_name, last_name, salary, commissionrate, union_dues, payment_method)
                self.employees.append(emp)


    # looks at timecards
    def read_timecards(self):

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
        self.read_hourly_employees()
        self.read_salaried_employees()
        self.read_timcards()
        self.read_receipts

        message = ''
        start_dt = datetime.datetime.strptime('5/01/2016', '%m/%d/%Y').date()
        end_dt = datetime.datetime.strptime('5/25/2016', '%m/%d/%Y').date()

        for emp in self._employees:
            message += emp.get_full_name() + '' + emp.calculate_pay(start_dt, end_dt) + '\n'
        label.config(text=message)

        #while hr_contents != '':
           #employee = hr_contents.split(',')
           #employee_id = row('EmployeeID')
           #last_name = row('LastName')
           #first_name = row('FirstName')
           #hourlyrate = row('HourlyRate')
           #uniondues = row('UnionDues')
           #payment_method = row('PaymentMethod')
           #while t_contents != "":
               #time = t_contents.split(',')
               #if int(time[0]) == employee_id:
                   #clock_in = row(time[1])
                   #clock_out = row(time[2])
                   #employee = employee.hourlyemployee(self, employee_id, first_name, last_name, hourlyrate, uniondues, payment_method)
                   #employee_list.append(employee)
               #t_contents = tinfile.readline()
           #hr_contents = hinfile.readline()

        #while sal_contents != '':
            #employ = sal_contents.split(',')
            #employee_id = row(employ[0])
            #last_name = row(employee(1))
            #first_name = row(employee(2))
            #salary = row(employee(3))
            #commissionrate = row(employee(4))
            #uniondues = row(employee(5))
            #payment_method = row(employee(6))
            #salemployee = employee.salariedemployee(self, employee_id, first_name, last_name, salary, commissionrate, uniondues, payment_method)
            #employee_list.append(salemployee)
            #while rec_contents != "":
                #receipt = rec_contents.split(',')
                #if row(receipt[0]) == employee_id:
                    #rec_contents = recfile.readline()

        #pay = HourlyEmployees.get(self, pay)
    
        #tkinter.messagebox.showinfo('Response', 'self.payment_method')
                     
#payroll = Payroll()
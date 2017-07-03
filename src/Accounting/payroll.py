import sys
import os
import csv
import datetime
import src.Accounting.Data
from employee import HourlyEmployee, SalariedEmployee
from paymentmethod import MailPayment, PickUpPayment, DirectDepositPayment

class Payroll:

    def __init__(self):
        self.employees = []

    #def run(self):
        #self.my_button2 = tkinter.Button(self.new_window, text='Run Payroll', command=self.run)
        #self.quit_button2 = tkinter.Button(self.new_window, text='QUIT', command=self.new_window.destroy)
                
        #self.my_button2.pack()
        #self.quit_button2.pack()

    # looks at hourly_employees
    def read_hourly_employees(self):

        with open('.../src/Accounting/Data/hourly_employees.csv', newline=' ') as csvfile:
            hreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in hreader:
                id = row['EmployeeId']
                last_name = row['LastName']
                first_name = row['FirstName']
                hourly_rate = row['HourlyRate']
                union_dues = row['UnionDues']
                abbr_pay_method = row['PaymentMethod']
                payment_method = lambda: None

                try:
                    union_dues = float(row['UnionDues'])
                except ValueError:
                    union_dues = 0.0

                if abbr_pay_method == 'DD':
                    payment_method = DirectDepositPayment("Generic", 0, 0)
                elif abbr_pay_method == 'PU':
                    payment_method == PickUpPayment()
                elif abbr_pay_method == 'MA':
                    payment_method == MailPayment('Generic', 'Generic', 'Generic', 'Generic')

    # looks at salaried_employees
    def read_salaried_employees(self):
            with open('...src/Accounting/Data/salaried_employees.csv', newline=' ') as csvfile:
                sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in sreader:
                id = row['EmployeeId']
                last_name = row['LastName']
                first_name = row['FirstName']
                salary = row['Salary']
                commissionrate = row['CommissionRate']
                union_dues = row['UnionDues']
                abbr_pay_method = row['PaymentMethod']
                payment_method = lambda: None

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
                total = atof(row['Total'])
                for emp_row in self._employee:
                    if emp_row.get_id() == id:
                        emp_row.make_sale(total)
                #first_name = row['FirstName']
                #item = row['Item']
                #unitcost = row['Unit Cost']
                #rtotal = row['Total']
    def process_payroll(self, label):
        self.__read_hourly_employees()
        self.__read_salaried_employees()
        self.__read_timcards()
        self.__read_receipts

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
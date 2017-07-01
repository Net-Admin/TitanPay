#from hourly_employees import HourlyEmployee
#from salariedemployee import SalariedEmployee
import sys
import os
import csv
import datetime

class Payroll:

    def __init__(self):
        self.employees = []

    def run(self):
        self.my_button2 = tkinter.Button(self.new_window, text='Run Payroll', command=self.run)
        self.quit_button2 = tkinter.Button(self.new_window, text='QUIT', command=self.new_window.destroy)
                
        self.my_button2.pack()
        self.quit_button2.pack()
                            
    def run(self):
        #looks at hourly_employees
        with open('hourly_employees.csv', newline=' ') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                return(', '.join(row))

        #looks at timecards
        with open('timecards.csv', newline=' ') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                return(', '.join(row))

        #looks at salaried_employees
        with open('salaried_employees.csv', newline=' ') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                return(', '.join(row))

        #looks at receipts
        with open('receipts.csv', newline=' ') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                return(', '.join(row))


        while hr_contents != '':
           employee = hr_contents.split(',')
           employee_id = row(EmployeeID)
           last_name = row(LastName)
           first_name = row(FirstName)
           hourlyrate = row(HourlyRate)
           uniondues = row(UnionDues)
           payment_method = row(PaymentMethod)
           while t_contents != "":
               time = t_contents.split(',')
               if int(time[0]) == employee_id:
                   clock_in = row(time[1])
                   clock_out = row(time[2])
                   employee = employee.hourlyemployee(self, employee_id, first_name, last_name, hourlyrate, uniondues, payment_method)
                   employee_list.append(employee)
               t_contents = tinfile.readline()
           hr_contents = hinfile.readline()

        while sal_contents != '':
            employ = sal_contents.split(',')
            employee_id = row(employ[0])
            last_name = row(employee(1))
            first_name = row(employee(2))
            salary = row(employee(3))
            commissionrate = row(employee(4))
            uniondues = row(employee(5))
            payment_method = row(employee(6))
            salemployee = employee.salariedemployee(self, employee_id, first_name, last_name, salary, commissionrate, uniondues, payment_method)
            employee_list.append(salemployee)
            while rec_contents != "":
                receipt = rec_contents.split(',')
                if row(receipt[0]) == employee_id:
                    rec_contents = recfile.readline()

        pay = HourlyEmployees.get(self, pay)
    
        tkinter.messagebox.showinfo('Response', 'self.payment_method')
                     
# create an instance of Running Payroll
payroll = RunningPayroll()
import tkinter
from tkinter import messagebox

class RunningPayroll:

    def __init__(self, employee):
        self.main_window = tkinter.Tk()
        self.new_window = tkinter.Tk()
        self.employee = employee

    def run_payroll(self):
        self.my_button2 = tkinter.Button(self.new_window, text='Run Payroll', command=self.run)
        self.quit_button2 = tkinter.Button(self.new_window, text='QUIT', command=self.new_window.destroy)
                
        self.my_button2.pack()
        self.quit_button2.pack()
                            
    def run(self):
        employee_list = []
        hinfile = open('hourly_employees.csv', 'r')
        hr_contents = hinfile.readline()
        hr_contents = hinfile.readline()
        tinfile = open('timecards.csv', 'r')
        t_contents = tinfile.readline()
        t_contents = tinfile.readline()
        sinfile = open('salaried_employees.csv', 'r')
        sal_contents = sinfile.readline()
        sal_contents = sinfile.readline()
        recfile = open('receipts.csv', 'r')
        rec_contents = recfile.readline()
        rec_contents = recfile.readline()
        
        while hr_contents != '':
           employ = hr_contents.split(',')
           employee_id = int(employ[0])
           first_name = int(employ(2))
           last_name = int(employ(1))
           hourlyrate = int(employ(3))
           uniondues = int(employ(4))
           payment_method = int(employ(5))
           while t_contents != "":
               time = t_contents.split(',')
               if int(time[0]) == employee_id:
                   clock_in = int(time[1])
                   clock_out = int(time[2])
                   employee = employee.hourlyemployee(self, employee_id, first_name, last_name, hourlyrate, uniondues, payment_method)
                   employee_list.append(employee)
               t_contents = tinfile.readline()
           hr_contents = hinfile.readline()

        while sal_contents != '':
            employ = sal_contents.split(',')
            employee_id = int(employ[0])
            first_name = int(employ(2))
            last_name = int(employ(1))
            salary = int(employ(3))
            commissionrate = int(employ(4))
            uniondues = int(employ(5))
            payment_method = int(employ(6))
            salemployee = employee.salariedemployee(self, employee_id, first_name, last_name, salary, commissionrate, uniondues, payment_method)
            employee_list.append(salemployee)
            while rec_contents != "":
                receipt = rec_contents.split(',')
                if int(receipt[0]) == employee_id:
                    rec_contents = recfile.readline()

        return employee_list
    
        pay = HourlyEmployees.get(self, pay)
    
        tkinter.messagebox.showinfo('Response', 'self.payment_method')
                     
# create an instance of Running Payroll
runpayroll = RunningPayroll()
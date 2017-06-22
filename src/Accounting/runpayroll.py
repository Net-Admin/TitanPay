import tkinter
from tkinter import messagebox

class RunningPayroll:

    def __init__(self, employee):
        self.employee = employee
        self.main_window = tkinter.Tk()
        self.new_window = tkinter.Tk()

    def run_payroll(self):
        self.my_button2 = tkinter.Button(self.new_window, text='Run Payroll', command=self.run)
        self.quit_button2 = tkinter.Button(self.new_window, text='QUIT', command=self.new_window.destroy)
                
        self.my_button2.pack()
        self.quit_button2.pack()
                            
    def run(self):
        employee_list = []
        infile = open(r'D:\Users\medic\PycharmProjects\TitanPay\src\Accounting\compiled_employees.txt', 'r')
        file_contents = infile.read()
        infile = open(r'D:\Users\medic\PycharmProjects\TitanPay\src\Accounting\timecards.txt', 'r')
        file_contents = infile.read()
        
        for count in range(1,5):
           global employee
           employee = employee+1
           employee = employee.Employee(self, employee_id, clock_in, clock_out)
           employee_list.append(employee)
        return employee_list
    
        pay = HourlyEmployees.get(self, pay)
    
        tkinter.messagebox.showinfo('Response', 'self.payment_method')
                     
# create an instance of Running Payroll
runpayroll = RunningPayroll()

# self.my_button1 = tkinter.Button(self.main_window, text='Process Payroll', command=self.run_payroll)
# self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)

# self.my_button1.pack()
# self.quit_button.pack()


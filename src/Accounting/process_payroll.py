import tkinter

class ProcessingPayroll:

    def __init__(self, employee):
        self.main_window =tkinter.Tk()
        self.employee = employee

        self.my_button1 = tkinter.Button(self.main_window, text='Processing Payroll')
        self.my_button2 = tkinter.Button(self.main_window, text='View/Add Employees.')
        self.my_button3 = tkinter.Button(self.main_window, text='View All Time Cards')
        self.my_button4 = tkinter.Button(self.main_window, text='View Pay Rate/Salary For Employee')
        self.my_button5 = tkinter.Button(self.main_window, text='View Sales For Employee')
        self.my_button6 = tkinter.Button(self.main_window, text='Change Payroll Payment Method')
        self.my_button7 = tkinter.Button(self.main_window, text='Run Payroll', command=self.run)
        self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)

        self.my_button1.pack()
        self.my_button2.pack()
        self.my_button3.pack()
        self.my_button4.pack()
        self.my_button5.pack()
        self.my_button6.pack()
        self.my_button7.pack()
        self.quit_button.pack()

        timesheet_file = open('timecards.txt', 'r')

    def run(self):
            employee_list = []
            infile = open(r'D:\Users\medic\PycharmProjects\TitanPay\src\Accounting\compiled_employees.txt', 'r')
            file_contents = infile.read()
            infile = open(r'D:\Users\medic\PycharmProjects\TitanPay\src\Accounting\timecards.txt', 'r')
            file_contents = infile.read()

            for count in range(1, 5):
                global employee
                employee = employee + 1
                employee = employee.Employee(self, employee_id, clock_in, clock_out)
                employee_list.append(employee)
            return employee_list

            pay = HourlyEmployees.get(self, pay)

            tkinter.messagebox.showinfo('Response', 'self.payment_method')
    # def do_something(self):
            tkinter.mainloop()

    # create an instance of Process Payroll
process_payroll = ProcessingPayroll()
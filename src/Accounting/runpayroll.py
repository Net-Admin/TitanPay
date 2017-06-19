import tkinter
import tkinter.messagebox

class RunningPayroll:

    def __init__(self):
        self.main_window =tkinter.Tk()
        self.new_window = tkinter.Tk()

        self.my_button1 = tkinter.Button(self.main_window, text='Process Payroll', command=self.run_payroll)
        self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)
        

        self.my_button1.pack()
        self.quit_button.pack()

        
        timesheet_file = open('timecards.csv', 'r')
        

        tkinter.mainloop()

    # def do_something(self):
    def run_payroll(self):
        self.my_button2 = tkinter.Button(self.new_window, text='Run Payroll', command=self.run)
        self.quit_button2 = tkinter.Button(self.new_window, text='QUIT', command=self.new_window.destroy)
                
        self.my_button2.pack()
        self.quit_button2.pack()
                            
    def run(self):
        employees_list = []
        infile = open('hourly_employees.csv', 'r')
        file_contents = infile.read()
        infile = open('timecards.csv', 'r')
        file_contents - infile.read()
        
        for count in range(employees_list):
           employees = employees.Employees(self, employee_id, clock_in, clock_out)
           employees_list.append(employees)
        return employees_list
    
        pay = HourlyEmployees.get(self, pay)
    
        tkinter.messagebox.showinfo('Response', 'self.payment_method')
                     
    # create an instance of Running Payroll
run_payroll = RunningPayroll()

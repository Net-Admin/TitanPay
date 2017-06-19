import tkinter
import tkinter.messagebox

class RunningPayroll:

    def __init__(self):
        self.main_window =tkinter.Tk()

        self.my_button1 = tkinter.Button(self.main_window, text='Run Payroll', command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)

        self.my_button1.pack()
        self.quit_button.pack()

        employee_file = open(r'c:\users\medic24\desktop\spc\cop3035\files\compiled_employees.txt', 'a')
        timesheet_file = open(r'c:\users\medic24\desktop\spc\cop3035\files\timesheet.txt', 'a')
        payment_file = open(r'c:\users\medic24\desktop\spc\cop3035\files\.txt', 'a')

        tkinter.mainloop()

    # def do_something(self):
    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thank You')
    # create an instance of Running Payroll
run_payroll = RunningPayroll()

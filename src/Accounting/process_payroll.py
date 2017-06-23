import sys
import os
import tkinter

def payroll():
    os.system('python runpayroll.py')

class ProcessingPayroll:

    def __init__(self):
        self.main_window =tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text='Processing Payroll')
        self.my_button2 = tkinter.Button(self.main_window, text='View/Add Employees.')
        self.my_button3 = tkinter.Button(self.main_window, text='View All Time Cards For Given Employees')
        self.my_button4 = tkinter.Button(self.main_window, text='View Pay Rate/Salary Information For A Given Employee')
        self.my_button5 = tkinter.Button(self.main_window, text='View Sales For Salaried Employee')
        self.my_button6 = tkinter.Button(self.main_window, text='Change A Given Employees Payroll Payment Method', command=payroll)
        self.my_button7 = tkinter.Button(self.main_window, text='Run Payroll And View Results')
        self.quit_button = tkinter.Button(self.main_window, text='QUIT', command=self.main_window.destroy)

        self.label1.pack()
        self.my_button2.pack()
        self.my_button3.pack()
        self.my_button4.pack()
        self.my_button5.pack()
        self.my_button6.pack()
        self.my_button7.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    # def do_something(self):

    # create an instance of Process Payroll
process_payroll = ProcessingPayroll()
import sys
import os
import tkinter
import csv
import sqlite3
from tkinter import *
from src.Accounting.payroll import Payroll
from src.DataBaseFiles.dbcreator import DBCreator
from src.DataBaseFiles.employee_db import EmployeeDataBase
from src.DataBaseFiles.timecard_db import TimeCardDb

def payroll():
    os.system('python payroll.py')

class Menu:
    def __init__(self):

        self.main_window = Tk()

        self.radio_var1 = IntVar()
        self.radio_var1.set(1)
        self.radio_var2 = IntVar()
        self.radio_var2.set(1)

        self.row1 = tkinter.Frame(self.main_window)
        self.row1.pack(padx=2, pady=2)

        self.first_name = tkinter.LabelFrame(self.row1, text="          First Name", bd=0, padx=2)
        self.first_name_entry = tkinter.Entry(self.first_name, width=15)
        self.first_name.pack(side='left', padx=2, pady=2)
        self.first_name_entry.pack(padx=2, pady=2)

        self.last_name = tkinter.LabelFrame(self.row1, text="          Last Name", bd=0, padx=2)
        self.last_name_entry = tkinter.Entry(self.last_name, width=15)
        self.last_name.pack(side='left', padx=2, pady=2)
        self.last_name_entry.pack(padx=2, pady=2)

        self.employee_id = tkinter.LabelFrame(self.row1, text="          Employee ID", bd=0, padx=2)
        self.employee_id_entry = tkinter.Entry(self.employee_id, width=10)
        self.employee_id.pack(side='left', padx=2, pady=2)
        self.employee_id_entry.pack(padx=2, pady=2)

        self.row2 = tkinter.Frame(self.main_window)
        self.row2.pack(padx=2, pady=2)

        self.street_address = tkinter.LabelFrame(self.row2, text='       Street Address', bd=0, padx=2)
        self.street_address_entry = tkinter.Entry(self.street_address, width=20)
        self.street_address.pack(side='left', padx=2, pady=2)
        self.street_address_entry.pack(padx=2, pady=2)

        self.city = tkinter.LabelFrame(self.row2, text='         City', bd=0, padx=2)
        self.city_entry = tkinter.Entry(self.city, width=25)
        self.city.pack(side='left', padx=2, pady=2)
        self.city_entry.pack(padx=2, pady=2)

        self.state = tkinter.LabelFrame(self.row2, text='State', bd=0, padx=2)
        self.state_entry = tkinter.Entry(self.state, width=2)
        self.state.pack(side='left', padx=2, pady=2)
        self.state_entry.pack(padx=2, pady=2)

        self.zip_code = tkinter.LabelFrame(self.row2, text='Zip Code', bd=0, padx=2)
        self.zip_code_entry = tkinter.Entry(self.zip_code, width=5)
        self.zip_code.pack(side='left', padx=2, pady=2)
        self.zip_code_entry.pack(padx=2, pady=2)

        self.row3 = tkinter.Frame(self.main_window)
        self.row3.pack(padx=2, pady=2)

        self.account_number = tkinter.LabelFrame(self.row3, text='        Bank Routing Number', bd=0, padx=2)
        self.account_number_entry = tkinter.Entry(self.account_number, width=25)
        self.account_number.pack(side='left', padx=2, pady=2)
        self.account_number_entry.pack(padx=2, pady=2)

        self.routing_number = tkinter.LabelFrame(self.row3, text='          Account Number', bd=0, padx=2)
        self.routing_number_entry = tkinter.Entry(self.routing_number, width=25)
        self.routing_number.pack(side='left', padx=2, pady=2)
        self.routing_number_entry.pack(padx=2, pady=2)

        self.row4 = tkinter.Frame(self.main_window)
        self.row4.pack(padx=2, pady=2)

        self.payment_method_label = tkinter.Label(self.row4, text='Payment Method: ')
        self.payment_method_label.pack(side='left', padx=2, pady=2)

        self.mail_rbutton = tkinter.Radiobutton(self.row4, text='Mail', variable=self.radio_var2, value=1)
        self.mail_rbutton.pack(side='left', padx=2, pady=2)

        self.pickup_rbutton = tkinter.Radiobutton(self.row4, text='Pick Up', variable=self.radio_var2, value=2)
        self.pickup_rbutton.pack(side='left', padx=2, pady=2)

        self.deposit_rbutton = tkinter.Radiobutton(self.row4, text='Direct Deposit', variable=self.radio_var2, value=3)
        self.deposit_rbutton.pack(side='left', padx=2, pady=2)

        #self.employee_type_label = tkinter.Label(self.row4, text="Employee Type: ")
        #self.employee_type_label.pack(side='left', padx=2, pady=2)

        #self.hourly_rbutton = tkinter.Radiobutton(self.row4, text='Hourly', variable=self.radio_var1, value=1)
        #self.hourly_rbutton.pack(side='left', padx=2, pady=2)
        #self.salary_rbutton = tkinter.Radiobutton(self.row4, text='Salary', variable=self.radio_var1, value=2)
        #self.salary_rbutton.pack(side='left', padx=2, pady=2)

        self.row5 = tkinter.Frame(self.main_window)
        self.row5.pack()

        self.display_timecards = tkinter.Button(self.row5, text="Display Time Cards", height=2)
        self.display_timecards.pack(side='left', padx=2, pady=2)

        #self.hourly_rate = tkinter.LabelFrame(self.row5, text="     Hourly Rate", bd=0, padx=2)
        #self.hourly_rate_entry = tkinter.Entry(self.hourly_rate, width=15)
        #self.hourly_rate.pack(side='left', padx=2, pady=2)
        #self.hourly_rate_entry.pack(padx=2, pady=2)

        #self.salary = tkinter.LabelFrame(self.row5, text="         Salary", bd=0, padx=2)
        #self.salary_entry = tkinter.Entry(self.salary, width=15)
        #self.salary.pack(side='left', padx=2, pady=2)
        #self.salary_entry.pack(padx=2, pady=2)

        #self.union_dues = tkinter.LabelFrame(self.row5, text=" Union Dues: ", bd=0, padx=2)
        #self.union_dues_entry = tkinter.Entry(self.union_dues, width=10)
        #self.union_dues.pack(side='left', padx=2, pady=2)
        #self.union_dues_entry.pack(side='left', padx=2, pady=2)

        self.row6 = tkinter.Frame(self.main_window)
        self.row6.pack()

        #self.display_timecards = tkinter.Button(self.row6, text="Display Time Cards", height=2)
        #self.display_timecards.pack(side='left', padx=2, pady=2)

        self.display_sales = tkinter.Button(self.row6, text="View Sales", height=2)
        self.display_sales.pack(side='left', padx=2, pady=2)

        self.row7 = tkinter.Frame(self.main_window)
        self.row7.pack(padx=2, pady=2)

        self.create_save_employee_button = tkinter.Button(self.row7, text='Create & Save Employee Record')
        self.create_save_employee_button.pack(side='left', padx=2, pady=2)

        #self.payment_method_label = tkinter.Label(self.row7, text='Payment Method: ')
        #self.payment_method_label.pack(side='left', padx=2, pady=2)

        #self.mail_rbutton = tkinter.Radiobutton(self.row7, text='Mail', variable=self.radio_var2, value=1)
        #self.mail_rbutton.pack(side='left', padx=2, pady=2)

        #self.pickup_rbutton = tkinter.Radiobutton(self.row7, text='Pick Up', variable=self.radio_var2, value=2)
        #self.pickup_rbutton.pack(side='left', padx=2, pady=2)

        #self.deposit_rbutton = tkinter.Radiobutton(self.row7, text='Direct Deposit', variable=self.radio_var2, value=3)
        #self.deposit_rbutton.pack(side='left', padx=2, pady=2)

        self.row8 = tkinter.Frame(self.main_window)
        self.row8.pack(padx=2, pady=2)

        #self.create_save_employee_button = tkinter.Button(self.row8, text='Create & Save Employee Record')
        #self.create_save_employee_button.pack(side='left', padx=2, pady=2)

        self.edit_employee_button = tkinter.Button(self.row8, text='Modify Employee Record')
        self.edit_employee_button.pack(side='left', padx=2, pady=2)

        self.row9 = tkinter.Frame(self.main_window)
        self.row9.pack(padx=2, pady=2)
        
        self.Import_Employees_button = tkinter.Button(self.row9, text='Import Employees', command=self.employee_db)
        self.Import_Employees_button.pack(side='left', padx=2, pady=2)

        self.row10 = tkinter.Frame(self.main_window)
        self.row10.pack(padx=2, pady=2)
        
        #self.Import_Employees_button = tkinter.Button(self.row10, text='Import Receipts', command=self.receipts_db)
        #self.Import_Employees_button.pack(side='left', padx=2, pady=2)

        self.row11 = tkinter.Frame(self.main_window)
        self.row11.pack(padx=2, pady=2)
        
        self.Import_Employees_button = tkinter.Button(self.row11, text='Import TimeCards', command=self.timecard_db)
        self.Import_Employees_button.pack(side='left', padx=2, pady=2)

        self.row12 = tkinter.Frame(self.main_window)
        self.row12.pack(padx=2, pady=2)

        self.process_payroll_button = tkinter.Button(self.row12, text='Process Payroll', command=self.show_run)
        self.process_payroll_button.pack(side='left', padx=2, pady=2)

        self.row13 = tkinter.Frame(self.main_window)
        self.row13.pack(padx=2, pady=2)
       
        self.quit_button = tkinter.Button(self.row13, text='QUIT', command=self.main_window.destroy)
        self.quit_button.pack(side='right', padx=2, pady=2)

        tkinter.mainloop()

    def employee_db(self):
        conn = sqlite3.connect(employee_db)
        conn.execute('''Create table Employees(last_name, first_name, employee_id, hourly_rate, union_dues);''')
        conn.commit
        conn.close()
    
    def receipts_db(self):
        conn = sqlite3.connect(receipts_db)
        conn.execute('''Create table Receipts(last_name, first_name, employee_id, hourly_rate, union_dues);''')
        conn.commit
        conn.close()
        
    def timecard_db(self):
        conn = sqlite3.connect(timecard_db)
        conn.execute('''Create table TimeCards(last_name, first_name, employee_id, hourly_rate, union_dues);''')
        conn.commit
        conn.close()
        
    def show_run(self):
        payroll = Payroll()

        self.sub_window = tkinter.Tk()

        self.run_payroll_button = tkinter.Button(self.sub_window, text='Run Payroll', command=lambda: payroll.process_payroll(self.payroll_message))
        self.run_payroll_button.pack(padx=2, pady=2)

        self.payroll_message = tkinter.Label(self.sub_window, text="Employee Payroll", bd=0, padx=2)
        self.payroll_message.pack()

test_gui = Menu()

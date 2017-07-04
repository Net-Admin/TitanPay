import sqlite3
import csv

class EmployeeDataBase:
    def __init__(self):
        pass

    def import_hourlyemployee(self):
        sqlite_file = 'employeedatabase.sqlite'
        id_column = 'Employee_ID'

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        hourlyemployeefile = open('hourly_employees.csv', 'r')
        line = hourlyemployeefile.readline()
        line = hourlyemployeefile.readline()

        while line != "":
            employ = line.split(',')
            id = int(employ[0])
            lastname = employ[1]
            firstname = employ[2]
            hourlyrate = employ[3]
            uniondues = employ[4]
            paymentmethod = employ[5]

            if '-' in employ[4]:
                try:
                    params = (id, lastname, firstname, hourlyrate, 0, paymentmethod)
                    c.execute("INSERT INTO Hourly_Employees VALUES (?, ?, ?, ?, ?, ?)", params)

                except sqlite3.IntegrityError:
                    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

                else:
                    try:
                        params = (id, lastname, firstname, hourlyrate, uniondues, paymentmethod)
                        c.execute("INSERT INTO Hourly_Employees VALUES (?, ?, ?, ?, ?, ?)", params)
                    except sqlite3.IntegrityError:
                        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

                line = hourlyemployeefile.readline()
            conn.commit()
            conn.close()
            hourlyemployeefile.close()

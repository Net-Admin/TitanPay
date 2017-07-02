import sqlite3

def import_timecards():
    conn = sqlite3.connect('timecard_db')
    cd = conn.cursor()
    cd.execute('Drop Table time_cards')
    cd.execute('Create Table timecards (employeeid TEXT NOT Null, ')
import sqlite3

class TimeCardDb:
    def __init__(self):

        def import_timecards():
            conn = sqlite3.connect('timecard_db')
            cd = conn.cursor()
            cd.execute('Drop Table time_cards')
            cd.execute('Create Table timecards (employeeid TEXT NOT Null, ')

            tc_hand = open('timecards.csv', 'r')
            count = 0
            for card in tc_hand:
                if count != 0:
                    tc = card.split(',')
                    tc[3] = tc[3].strip()
                    cd.execute('INSERT INTO t_cards(emp_id, time_in, time_out, tc_date) VALUES (?, ?, ?, ?)', (tc[0], tc[1], tc[2], tc[3]))

            count += 1

            tc_hand.close()
            conn.commit()
            conn.close()

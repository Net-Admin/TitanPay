from unittest import TestCase
from src.Accounting.hourlyemployee import HourlyEmployee
from src.Accounting.pickuppayment import PaymentMethod
from src.Accounting.receipt import Receipt
from src.Accounting.timecard import TimeCard
import datetime

class TestHourlyEmployee(TestCase):

    def test_new_employee_has_no_time_cards(self):
        # arrange
        emp = HourlyEmployee('employeeid', 'last_name', 'first_name', 'hourly_rate', 'weekly_dues', 'payment_method')

        # assert
        cnt = emp.get_timecard_count()
        self.assertEqual(cnt, 0)

    def test_clockIn(self):
        #arrange
        emp = HourlyEmployee('employeeid', 'last_name', 'first_name', 'hourly_rate', 'weekly_dues', 'payment_method')

        #act
        emp.clockIn()

        #assert
        count = emp.get_time_count()
        self.assertEquals(count, 1)

    def test_clockOut(self):
        #arrange
        emp = HourlyEmployee('employeeid', 'last_name', 'first_name', 'hourly_rate', 'weekly_dues', 'payment_method')

        #act
        emp.start_time(datetime.datetime.strptime('5/25/2016 0800', '%m/%d/%Y %H%M')
        result = emp.end_time(datetime.datetime.strptime('5/25/2016 1700', '%m/%d/%Y %H%M')

        # assert
        self.assertTrue(result)

    def test_calculate_pay__(self):
        # arrange
        emp = HourlyEmployee('employeeid', 'last_name', 'first_name', 'hourly_rate', 'weekly_dues', 'payment_method')
        start_date = datetime.datetime.strptime('5/25/2016 0800', '%m/%d/%Y').date()
        end_date = datetime.datetime.strptime('5/25/2016', '%m/%d/%Y').date()
        start_time = '0800'
        end_time = '1700'

        # act
        for i in range(1, 6):
            date = '5/%d/2016' % (i)
            start_time_str = '%s %s' % (date, start_time)
            end_time_str = '%s %s' % (date, end_time)

            emp.clock_in(datetime.datetime.strptime(start_time_str, '%m/%d/%Y %H%M'))
            emp.clock_out(datetime.datetime.strptime(end_time_str, '%m/%d/%Y %H%M'))

        # assert
        emp.calculate_pay(start_date, end_date)
        pay = emp.get_last_pay_amount()
        self.assertGreater(pay, 0)
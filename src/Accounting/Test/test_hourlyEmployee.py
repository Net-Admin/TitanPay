from unittest import TestCase

class TestHourlyEmployee(TestCase):
    def __init__(self):
        self.__timecards

       def test_clockIn(self):
        hourly = HourlyEmployee('10', 'Chris', 'Platt', '999', '150', 'DD')
        hourly.clock_in()
        timecard = hourly.get_time_card()
        self.assertIsInstance(timecard, TimeCard)

    def test_clockOut(self):
        hourly = HourlyEmployee('10', 'Chris', 'Platt', '999', '150', 'DD')
        hourly.clock_in()
        hourly.clock_out()
        time = TimeCard.calculate_daily_pay()
        self.assertTrue(time >= 1)

    def test_calculate_pay__(self):
        hourly = HourlyEmployee('10', 'Chris', 'Platt', '999', '150', 'DD')
        hourly.clock_in()
        hourly.clock_out()
        time = TimeCard.calculate_daily_pay()
        self.assertTrue(time >= 1)


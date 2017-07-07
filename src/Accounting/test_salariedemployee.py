from unittest import TestCase
from src.Accounting.salariedemployee import SalariedEmployee
from src.Accounting.paymentmethod import PaymentMethod

class TestSalariedEmployee(TestCase):

    def test_new_employee_has_no_receipts(self):
        # arrange
        emp = SalariedEmployee('employeeid', 'last_name', 'first_name', 'salary', 'commission_rate', 'union_dues', 'payment_method')

        # assert
        count = emp.get_receipt_count()
        self.assertEqual(count, 0)
    def test_makeSale(self):
        # arrange
        emp = SalariedEmployee('employeeid', 'last_name', 'first_name', 'salary', 'commission_rate', 'union_dues', 'payment_method')

        # act
        emp.make_sale(100)

        # assert
        count = emp.get_receipt_count()
        self.assertEqual(count, 1)

    def test_calculate_pay__(self):
        # arrange
        emp = SalariedEmployee('employeeid', 'last_name', 'first_name', 'salary', 'commission_rate', 'union_dues', 'payment_method')

        # act
        for i in range(1, 6):
            amount = 100 * i
            emp.make_sale(amount)

        # assert
        emp.calculate_pay("", "")
        pay = emp.get_last_pay_amount()
        self.assertGreater(pay, 0)

import unittest

from employee1103 import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('mrs','li',70000)
    def test_give_default_raise(self):
        self.assertEqual(self.employee.name,'Mrs Li')
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,75000)
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.name,'Mrs Li')
        self.assertEqual(self.employee.salary,80000)
unittest.main()
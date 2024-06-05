import unittest

from city_country1102 import *

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country01 = city_country('santiago','chile')
        self.assertEqual(city_country01,'Santiago,Chile')
    def test_city_country(self):
        city_country01 = city_country('santiago','chile',5000000)
        self.assertEqual(city_country01,'Santiago,Chile-5000000')

unittest.main()
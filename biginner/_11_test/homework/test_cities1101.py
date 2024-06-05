import unittest

from city_country1101 import *

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country01 = city_country('santiago','chile')
        self.assertEqual(city_country01,'Santiago,Chile')

unittest.main()
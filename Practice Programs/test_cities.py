# test_cities.py

import unittest
from city_functions import cico

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = cico('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

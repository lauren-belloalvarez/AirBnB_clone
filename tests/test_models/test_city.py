#!/usr/bin/python3
"""
Test Module of city
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def testing_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main() 

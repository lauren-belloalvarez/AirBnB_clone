#!/usr/bin/python3
"""
The Amenity Module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_defaults(self):
        # Test default Amenity
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_str_representation(self):
        # Testing Amenity String Representation
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_amenity_to_dict_method(self):
        # Testing Amenity to dict method
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

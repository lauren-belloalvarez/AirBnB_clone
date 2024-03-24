#!/usr/bin/python3
"""
Unittest for base module
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import engine
from models import storage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Initialize the storage engine before each test
        engine.storage = storage

    def test_str_method(self):
        # Test if the __str__ method returns
        # the expected string representation
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        # Test if the save method updates the 'updated_at'
        # attribute and calls storage.save()
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        # self.assertTrue(model.save())

    def test_to_dict_method(self):
        # Test if the to_dict method returns a dictionary
        # with expected key-value pairs
        model = BaseModel()
        Model_dict = model.to_dict()
        self.assertIsInstance(Model_dict, dict)
        self.assertEqual(Model_dict["__class__"], "BaseModel")
        self.assertEqual(Model_dict["id"], model.id)
        self.assertEqual(Model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(Model_dict["updated_at"], model.updated_at.isoformat())

    if __name__ == '__main__':
        unittest.main()

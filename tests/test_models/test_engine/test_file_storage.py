#!usr/bin/python3
"""
Test FileStorage Module
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Set up a FileStorage instance before each test
        self.file_storage = FileStorage()

    def tearDown(self):
        # Clean up the created file after each test
        if os.path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all_method(self):
        # Test if the all method returns the __objects dictionary
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {})

    def test_new_method(self):
        # Test if the new method adds an object to __objects with the correct key
        model = BaseModel()
        self.file_storage.new(model)
        key = model.__class__.__name__ + "." + str(model.id)
        self.assertIn(key, self.file_storage.all())

    def test_save_method(self):
        # Test if the save method creates a valid JSON file with the correct content
        model1 = BaseModel()
        model2 = User()
        self.file_storage.new(model1)
        self.file_storage.new(model2)
        self.file_storage.save()

        # Check if the file exists
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))

        # Check if the content of the file is valid JSON
        with open(self.file_storage._FileStorage__file_path, 'r') as f:
            content = f.read()
            self.assertIsInstance(content, str)
            self.assertGreater(len(content), 0)
            self.assertTrue(content.startswith('{'))
            self.assertTrue(content.endswith('}'))

    def test_reload_method(self):
        # Test if the reload method deserializes the JSON file correctly
        model = BaseModel()
        self.file_storage.new(model)
        self.file_storage.save()

        # Clear the current __objects to simulate a fresh instance
        self.file_storage._FileStorage__objects = {}

        # Reload and check if the object is present in __objects
        self.file_storage.reload()
        key = model.__class__.__name__ + "." + str(model.id)
        self.assertIn(key, self.file_storage.all())


if __name__ == '__main__':
    unittest.main()

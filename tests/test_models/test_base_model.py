import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.test_instance = BaseModel()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init_new_instance(self):
        self.assertIsInstance(self.test_instance, BaseModel)
        self.assertTrue(hasattr(self.test_instance, 'id'))
        self.assertTrue(hasattr(self.test_instance, 'created_at'))
        self.assertTrue(hasattr(self.test_instance, 'updated_at'))
        self.assertTrue(hasattr(self.test_instance, 'save'))
        self.assertTrue(hasattr(self.test_instance, 'to_dict'))

    def test_init_existing_instance(self):
        existing_instance = BaseModel(id="123", created_at=datetime.now(), updated_at=datetime.now())
        self.assertIsInstance(existing_instance, BaseModel)
        self.assertEqual(existing_instance.id, "123")
        self.assertTrue(existing_instance.created_at < datetime.now())
        self.assertTrue(existing_instance.updated_at < datetime.now())

    def test_save(self):
        initial_updated_at = self.test_instance.updated_at
        self.test_instance.save()
        self.assertNotEqual(initial_updated_at, self.test_instance.updated_at)

    def test_to_dict(self):
        dict_representation = self.test_instance.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(dict_representation['__class__'], 'BaseModel')
        self.assertIn('id', dict_representation)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)

    def test_new(self):
        new_instance = BaseModel()
        self.assertIn('BaseModel.{}'.format(new_instance.id), storage.all())

    def test_reload(self):
        self.test_instance.save()
        loaded_instance = BaseModel()
        loaded_instance_id = loaded_instance.id
        storage.save()
        storage.reload()
        reloaded_instance = BaseModel()
        self.assertEqual(loaded_instance_id, reloaded_instance.id)

if __name__ == '__main__':
    unittest.main()


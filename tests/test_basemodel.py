#!/usr/bin/python3

import unittest
from datetime import datetime
from unittest.mock import patch

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    @patch("models.base_model.datetime")
    def test_save_updates_updated_at(self, mock_datetime):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_contains_class_name(self):
        model_dict = self.base_model.to_dict()
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_contains_created_at_and_updated_at_as_isoformat(self):
        model_dict = self.base_model.to_dict()
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertEqual(
            model_dict["created_at"], self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict["updated_at"], self.base_model.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()

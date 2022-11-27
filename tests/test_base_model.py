#!/usr/bin/python3
"""BaseModel unittests"""
import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """class TestBaseModel"""

    def test_base_model_atrr_type(self):
        """test BaseModel attributes"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id), 36)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_base_model_save_metho(self):
        """test BaseModel save method"""
        base = BaseModel()
        time.sleep(0.0001)
        base.save()
        self.assertNotEqual(base.updated_at, base.created_at)

    def test_base_model_to_dict_method(self):
        """test BaseModel to_dict method to create dictionary"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['__class__'], type(base).__name__)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_base_model_to_dict_to_instance_with_kwargs(self):
        """test BaseModel can instantaite new object wiht dictionary"""
        base = BaseModel()
        base.name = "Betty"
        base.number = 972
        base_dict = base.to_dict()
        new_base = BaseModel(**base_dict)
        new_base_dict = new_base.to_dict()
        self.assertFalse(new_base is base)
        self.assertDictEqual(new_base_dict, base_dict)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Test cases for the Base claws
"""

import unittest
import datetime
import os
import json
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage


class TestBase_1(unittest.TestCase):
    """
    Base class testingf.
    """
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_init_1(self):
        """
        Tests when a BaseModel object is initilia with kwargs and when not.
        """
        my_model_dict = self.my_model.to_dict_1()
        derived_model = BaseModel(**my_model_dict)
        test_model = BaseModel()
        test_model.id = str(21)
        self.assertEqual(test_model.id, '21')
        self.assertIs(self.my_model.__class__.__name__, 'BaseModel')
        self.assertEqual(derived_model.name, self.my_model.name)
        self.assertEqual(derived_model.my_number, self.my_model.my_number)
        self.assertIsNot(derived_model, self.my_model)
        self.assertIs(type(derived_model.created_at), datetime.datetime)
        self.assertIs(type(derived_model.updated_at), datetime.datetime)
        self.assertNotIn('__class__', derived_model.__dict__)
        self.assertIs(type(self.my_model.id), str)
        self.assertIs(type(derived_model.id), str)
        self.assertIs(storage.all()[f"BaseModel.{self.my_model.id}"],
                      self.my_model)
        self.assertIsNot(storage.all()[f"BaseModel.{derived_model.id}"],
                         derived_model)

    def test_str_1(self):
        """
        Tests the __str__functions.
        """
        str_text1 = f"[{self.my_model.__class__.__name__}] "
        str_text2 = f"({self.my_model.id}) {self.my_model.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.my_model)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save_1(self):
        """
        Tests the save function.
        """
        new_model = BaseModel()
        initial_time = self.my_model.updated_at
        self.assertIn(f"BaseModel.{new_model.id}", storage.all())
        self.assertIn(f"BaseModel.{self.my_model.id}", storage.all())
        self.my_model.save()
        storage.reload()
        self.assertIn(f"BaseModel.{self.my_model.id}", storage.all())
        # new_model will be saved even though we didn't cALL
        # the method save on i
        # It's because it's in the storage.all()
        # befo my_model.save() was called
        # and it was saved a result of that.
        self.assertIn(f"BaseModel.{new_model.id}", storage.all())
        self.assertIsNot(new_model, storage.all()[f"BaseModel.{new_model.id}"])
        self.assertIsNot(self.my_model,
                         storage.all()[f"BaseModel.{self.my_model.id}"])
        self.assertNotEqual(initial_time, self.my_model.updated_at)
        self.assertTrue(os.path.isfile('file.json'), True)
        # Demonstrating that if we don't call that save() function at all
        # the object will still be in the storage.all() but as the same object.
        # This is because it's still the same program
        # The only way to find whether it has been saved
        # is to run ANOTHER program
        another_model = BaseModel()
        self.assertIn(f"BaseModel.{another_model.id}", storage.all())
        storage.reload()
        self.assertIn(f"BaseModel.{another_model.id}", storage.all())
        # The test below shows its the same object in the storage.all()
        self.assertIs(another_model,
                      storage.all()[f"BaseModel.{another_model.id}"])
        # The test below shows anther_model wasn't reloaded from the json file
        # hence not saved unlike de others.
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_dict = json.load(file)
            self.assertNotIn(f"BaseModel.{another_model.id}", saved_dict)
            self.assertIn(f"BaseModel.{new_model.id}", saved_dict)
            self.assertIn(f"BaseModel.{self.my_model.id}", storage.all())

    def test_to_dict_1(self):
        """
        Tests the to_dict function.
        """
        self.assertNotEqual(self.my_model.__dict__, self.my_model.to_dict_1())
        self.assertIn('__class__', self.my_model.to_dict_1())
        self.assertNotIn('__class__', self.my_model.__dict__)
        self.assertIs(type(self.my_model.to_dict_1()['created_at']), str)
        self.assertIs(type(self.my_model.to_dict_1()['updated_at']), str)

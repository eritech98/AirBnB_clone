#!/usr/bin/python3
"""
Has tests for the FileStorage clas
"""

import unittest
import json
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage_1(unittest.TestCase):
    """
    Tests the FileStorage class.
    """
    def setUp(self):
        self.new_model = BaseModel()

    def test_class_attributes_1(self):
        """
        Tests the class attribtes.
        """
        self.assertEqual(storage.all(), FileStorage._FileStorage__objects_1)
        self.assertEqual(FileStorage._FileStorage__file_path_1, "file.json")

    def test_all_1(self):
        """
        Tests tall method.
        """
        self.assertIn(f"BaseModel.{self.new_model.id_1}", storage.all())
        self.assertIs(type(storage.all()), dict)

    def test_new_1(self):
        """
        Tests the New method.
        """
        derived_model = BaseModel(**(self.new_model.to_dict_1()))
        self.assertIn(f"BaseModel.{self.new_model.id_1}", storage.all())
        self.assertIn(f"BaseModel.{derived_model.id_1}", storage.all())
        # Since save and reload haven't been called
        # the object in storage.all() will be the new one.
        self.assertIs(storage.all()[f"BaseModel.{self.new_model.id_1}"],
                      self.new_model)
        self.assertIsNot(storage.all()[f"BaseModel.{derived_model.id_1}"],
                         derived_model)

    def test_save_1(self):
        """
        Tests the Save method.
        """
        another_model = BaseModel()
        self.assertIs(storage.all()[f"BaseModel.{self.new_model.id_1}"],
                      self.new_model)
        self.assertIs(storage.all()[f"BaseModel.{another_model.id_1}"],
                      another_model)
        # If we call save in one of the models, both models will be saved
        # because the save function will save
        # the current state of storage.all().
        self.new_model.save()
        self.assertTrue(os.path.isfile('file.json'), True)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            another_model_key = f"BaseModel.{another_model.id_1}"
            new_model_key = f"BaseModel.{self.new_model.id_1}"
            self.assertIn(another_model_key, saved_objects)
            self.assertIn(new_model_key, saved_objects)
            self.assertEqual(saved_objects[another_model_key],
                             another_model.to_dict_1())
            self.assertEqual(saved_objects[new_model_key],
                             self.new_model.to_dict_1())

    def test_reload_1(self):
        """
        Tests the reloading method.
        """
        try:
            if os.path.isfile('file.json') is False:
                storage.reload()
        except FileNotFoundError as error:
            self.assertTrue(error)

        new_model_key = f"BaseModel.{self.new_model.id_1}"
        self.new_model.save()
        reloaded_objects = storage.all()
        self.assertIs(reloaded_objects[new_model_key], self.new_model)
        storage.reload()
        self.assertIsNot(reloaded_objects[new_model_key], self.new_model)
        self.assertEqual(reloaded_objects[new_model_key].to_dict_1(),
                         self.new_model.to_dict_1())

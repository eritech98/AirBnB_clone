#!/usr/bin/python3

"""
Has tests for the amnity class
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.amenity import Amenity
from models import storage


class TestAmenity_1(unittest.TestCase):
    """
    Tests the Amenity class and the attributes.
    """

    def setUp(self):
        self.amenity = Amenity()
        self.amenity_key = f"Amenity.{self.amenity.id}"

    def test_public_class_attributes_1(self):
        """
        Tests the public class attributes.
        """
        self.assertIs(Amenity.name, "")
        self.assertNotIn('name', self.amenity.__dict__)
        self.amenity.name = "Private Beach"
        self.assertIs(self.amenity.name, 'Private Beach')
        self.amenity.name = 12
        self.assertIs(self.amenity.name, 12)
        self.amenity.name = ["Private Beach"]
        self.assertEqual(self.amenity.name, ['Private Beach'])
        self.amenity.name = {"Private Beach"}
        self.assertEqual(self.amenity.name, {'Private Beach'})
        self.amenity.name = ("Private Beach", "Fun Park")
        self.assertEqual(self.amenity.name, ('Private Beach', "Fun Park"))
        self.amenity.name = {'name': "Private Beach"}
        self.assertEqual(self.amenity.name, {'name': 'Private Beach'})
        self.amenity.name = True
        self.assertIs(self.amenity.name, True)

    def test_init_1(self):
        """
        Tests the init methd.
        """
        self.assertIs(self.amenity.__class__.__name__, 'Amenity')
        self.assertIn('created_at', self.amenity.__dict__)
        self.assertIn('updated_at', self.amenity.__dict__)
        self.assertIn('id', self.amenity.__dict__)
        self.assertIs(type(self.amenity.__dict__['id']), str)
        self.assertIs(type(self.amenity.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.amenity.__dict__['updated_at']),
                      datetime.datetime)

    def test_str_1(self):
        """
        Tests the string method.
        """
        str_text1 = f"[{self.amenity.__class__.__name__}] "
        str_text2 = f"({self.amenity.id}) {self.amenity.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.amenity)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save_1(self):
        """
        Tests the save metho
        """
        first_update = self.amenity.updated_at
        self.assertIn(self.amenity_key, storage.all())
        self.assertIs(storage.all()[self.amenity_key], self.amenity)
        self.amenity.save()
        self.assertNotEqual(first_update, self.amenity.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.amenity_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.amenity_key], self.amenity)
        self.assertEqual(storage.all()[self.amenity_key].to_dict_1(),
                         self.amenity.to_dict_1())

    def test_to_dict_1(self):
        """
        Tests the to_dict method.
        """
        self.assertNotEqual(self.amenity.__dict__,
                            self.amenity.to_dict_1())
        self.assertIn('__class__', self.amenity.to_dict_1())
        self.assertNotIn('__class__', self.amenity.__dict__)
        self.assertIs(type(self.amenity.to_dict_1()['created_at']), str)
        self.assertIs(type(self.amenity.to_dict_1()['updated_at']), str)

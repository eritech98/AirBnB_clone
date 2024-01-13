#!/usr/bin/python3

"""
Has tests for the Sttes class.
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.state import State
from models import storage


class TestState_1(unittest.TestCase):
    """
    Tests for The State class and attributes.
    """
    def setUp(self):
        self.my_state = State()
        self.my_state_key = f"State.{self.my_state.id_1}"

    def test_public_class_attributes_1(self):
        """
        Tests the public class attributEs.
        """
        self.assertIs(State.name, "")
        self.assertNotIn('name', self.my_state.__dict__)
        self.my_state.name = 'NAIROBI'
        self.assertIs(self.my_state.name, "NAIROBI")
        self.assertIn('name', self.my_state.__dict__)
        self.my_state.name = ['Makueni', 'COAST', 'Kisumu']
        self.assertEqual(self.my_state.name, ['Makueni', 'COAST', 'Kisumu'])
        self.my_state.name = 12
        self.assertIs(self.my_state.name, 12)
        self.my_state.name = {'state': 'NAIROBI'}
        self.assertEqual(self.my_state.name, {'state': 'NAIROBI'})
        self.my_state.name = True
        self.assertIs(self.my_state.name, True)
        self.my_state.name = {'KITUI'}
        self.assertEqual(self.my_state.name, {'KITUI'})
        self.my_state.name = ('Rift Valley', 'KITALE')
        self.assertEqual(self.my_state.name, ('Rift Valley', 'KITALE'))

    def test_init_1(self):
        """
        Tests the Init method.
        """
        self.assertIs(self.my_state.__class__.__name__, 'State')
        self.assertIn('created_at', self.my_state.__dict__)
        self.assertIn('updated_at', self.my_state.__dict__)
        self.assertIn('id_1', self.my_state.__dict__)
        self.assertIs(type(self.my_state.__dict__['id_1']), str)
        self.assertIs(type(self.my_state.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.my_state.__dict__['updated_at']),
                      datetime.datetime)

    def test_str_1(self):
        """
        Tests the string method.
        """
        str_text1 = f"[{self.my_state.__class__.__name__}] "
        str_text2 = f"({self.my_state.id_1}) {self.my_state.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.my_state)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save_1(self):
        """
        Tests the savE method.
        """
        first_update = self.my_state.updated_at
        self.assertIn(self.my_state_key, storage.all())
        self.assertIs(storage.all()[self.my_state_key], self.my_state)
        self.my_state.save()
        self.assertNotEqual(first_update, self.my_state.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.my_state_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.my_state_key], self.my_state)
        self.assertEqual(storage.all()[self.my_state_key].to_dict_1(),
                         self.my_state.to_dict_1())

    def test_to_dict_1(self):
        """
        Tests the to_dict mEthod.
        """
        self.assertNotEqual(self.my_state.__dict__,
                            self.my_state.to_dict_1())
        self.assertIn('__class__', self.my_state.to_dict_1())
        self.assertNotIn('__class__', self.my_state.__dict__)
        self.assertIs(type(self.my_state.to_dict_1()['created_at']), str)
        self.assertIs(type(self.my_state.to_dict_1()['updated_at']), str)

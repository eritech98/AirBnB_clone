#!/usr/bin/python3

"""
Has tests for the user clas.
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.user import User
from models import storage


class TestUser_1(unittest.TestCase):
    """
    Tests for the User class And attributes.
    """

    def setUp(self):
        self.first_user = User()
        self.first_user_key = f"User.{self.first_user.id}"

    def test_public_class_attributes_1(self):
        """
        Tests the public class attribtes.
        """
        self.assertIs(User.email, "")
        self.assertIs(User.first_name, "")
        self.assertIs(User.last_name, "")
        self.assertIs(User.password, "")
        self.assertNotIn('email', self.first_user.__dict__)
        self.assertNotIn('first_name', self.first_user.__dict__)
        self.assertNotIn('last_name', self.first_user.__dict__)
        self.assertNotIn('password', self.first_user.__dict__)
        self.first_user.email = "mitten.mars@mia.pets"
        self.first_user.first_name = "Mitten"
        self.first_user.password = "TedShmosbY"
        self.assertIn('email', self.first_user.__dict__)
        self.assertIs(self.first_user.__dict__['email'],
                      "mitten.mars@mia.pets")
        self.assertIn('first_name', self.first_user.__dict__)
        self.assertIs(self.first_user.__dict__['first_name'], "Mitten")
        self.assertIn('password', self.first_user.__dict__)
        self.assertIs(self.first_user.__dict__['password'], "TedShmosbY")
        self.first_user.email = 14
        self.first_user.first_name = 15
        self.first_user.last_name = 16
        self.first_user.password = 17
        self.assertIs(self.first_user.__dict__['email'], 14)
        self.assertIs(self.first_user.__dict__['first_name'], 15)
        self.assertIs(self.first_user.__dict__['last_name'], 16)
        self.assertIs(self.first_user.__dict__['password'], 17)
        self.first_user.email = ['me@you.us']
        self.first_user.first_name = ['me']
        self.first_user.last_name = ['we']
        self.first_user.password = ['meweyou']
        self.assertEqual(self.first_user.__dict__['email'], ['me@you.us'])
        self.assertEqual(self.first_user.__dict__['first_name'], ['me'])
        self.assertEqual(self.first_user.__dict__['last_name'], ['we'])
        self.assertEqual(self.first_user.__dict__['password'], ['meweyou'])
        self.first_user.email = {'email': "mitten.mars@mia.pets"}
        self.first_user.first_name = {'first_name': 'Mitten'}
        self.first_user.last_name = {'last_name': 'Mars'}
        self.first_user.password = {'password': "TedShmosbY"}
        self.assertEqual(self.first_user.__dict__['email'],
                         {'email': "mitten.mars@mia.pets"})
        self.assertEqual(self.first_user.__dict__['first_name'],
                         {'first_name': 'Mitten'})
        self.assertEqual(self.first_user.__dict__['last_name'],
                         {'last_name': 'Mars'})
        self.assertEqual(self.first_user.__dict__['password'],
                         {'password': "TedShmosbY"})
        self.first_user.email = ("mitten.mars@mia.pets",
                                 "nala.pumba@garfield.pets")
        self.first_user.first_name = ('Pumba', 'Nala')
        self.first_user.last_name = ('Garfield', 'Garfield')
        self.first_user.password = ('CleopatraLittle', 'OrangeFriendly')
        self.assertEqual(self.first_user.__dict__['email'],
                         ("mitten.mars@mia.pets", "nala.pumba@garfield.pets"))
        self.assertEqual(self.first_user.__dict__['first_name'],
                         ('Pumba', 'Nala'))
        self.assertEqual(self.first_user.__dict__['last_name'],
                         ('Garfield', 'Garfield'))
        self.assertEqual(self.first_user.__dict__['password'],
                         ('CleopatraLittle', 'OrangeFriendly'))
        self.first_user.email = {'max.milliano@queen.pets'}
        self.first_user.first_name = {'max'}
        self.first_user.last_name = {'Queen'}
        self.first_user.password = {'IamtheOGA'}
        self.assertEqual(self.first_user.__dict__['email'],
                         {'max.milliano@queen.pets'})
        self.assertEqual(self.first_user.__dict__['first_name'], {'max'})
        self.assertEqual(self.first_user.__dict__['last_name'], {'Queen'})
        self.assertEqual(self.first_user.__dict__['password'], {'IamtheOGA'})
        self.first_user.email = True
        self.first_user.first_name = True
        self.first_user.last_name = False
        self.first_user.password = True
        self.assertIs(self.first_user.__dict__['email'], True)
        self.assertIs(self.first_user.__dict__['first_name'], True)
        self.assertIs(self.first_user.__dict__['last_name'], False)
        self.assertIs(self.first_user.__dict__['password'], True)

    def test_init_1(self):
        """
        Tests the _init__ method.
        """
        self.assertIs(self.first_user.__class__.__name__, 'User')
        self.assertIn('created_at', self.first_user.__dict__)
        self.assertIn('updated_at', self.first_user.__dict__)
        self.assertIn('id', self.first_user.__dict__)
        self.assertIs(type(self.first_user.__dict__['id']), str)
        self.assertIs(type(self.first_user.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.first_user.__dict__['updated_at']),
                      datetime.datetime)

    def test_str_1(self):
        """
        Tests the string method.
        """
        str_text1 = f"[{self.first_user.__class__.__name__}] "
        str_text2 = f"({self.first_user.id}) {self.first_user.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.first_user)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save_1(self):
        """
        Tests the save meThod.
        """
        first_update = self.first_user.updated_at
        self.assertIn(self.first_user_key, storage.all())
        self.assertIs(storage.all()[self.first_user_key], self.first_user)
        self.first_user.save()
        self.assertNotEqual(first_update, self.first_user.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.first_user_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.first_user_key], self.first_user)
        self.assertEqual(storage.all()[self.first_user_key].to_dict_1(),
                         self.first_user.to_dict_1())

    def test_to_dict_1(self):
        """
        Tests the to_dict mEthod.
        """
        self.assertNotEqual(self.first_user.__dict__,
                            self.first_user.to_dict_1())
        self.assertIn('__class__', self.first_user.to_dict_1())
        self.assertNotIn('__class__', self.first_user.__dict__)
        self.assertIs(type(self.first_user.to_dict_1()['created_at']), str)
        self.assertIs(type(self.first_user.to_dict_1()['updated_at']), str)

#!/usr/bin/python3

"""
Has the tests for the place clAss.
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from models import storage


class TestPlace_1(unittest.TestCase):
    """
    Tests the Place class and its attributes.
    """

    def setUp(self):
        self.my_user = User()
        self.my_city = City()
        self.amenity = Amenity()
        self.my_place = Place()
        self.my_place_key = f"Place.{self.my_place.id}"

    def test_public_class_attributes_1(self):
        """
        Tests the public class attributes.
        """
        self.assertIs(self.my_place.city_id, "")
        self.assertIs(self.my_place.user_id, "")
        self.assertIs(self.my_place.name, "")
        self.assertIs(self.my_place.description, "")
        self.assertIs(self.my_place.number_bathrooms, 0)
        self.assertIs(self.my_place.number_rooms, 0)
        self.assertIs(self.my_place.max_guest, 0)
        self.assertIs(self.my_place.price_by_night, 0)
        self.assertEqual(self.my_place.latitude, 0.0)
        self.assertEqual(self.my_place.longitude, 0.0)
        self.assertEqual(self.my_place.amenity_ids, [])
        self.assertNotIn('city_id', self.my_place.__dict__)
        self.assertNotIn('user_id', self.my_place.__dict__)
        self.assertNotIn('name', self.my_place.__dict__)
        self.assertNotIn('description', self.my_place.__dict__)
        self.assertNotIn('number_rooms', self.my_place.__dict__)
        self.assertNotIn('number_bathrooms', self.my_place.__dict__)
        self.assertNotIn('max_guest', self.my_place.__dict__)
        self.assertNotIn('price_by_night', self.my_place.__dict__)
        self.assertNotIn('latitude', self.my_place.__dict__)
        self.assertNotIn('longitude', self.my_place.__dict__)
        self.assertNotIn('amenity_ids', self.my_place.__dict__)
        self.my_place.city_id = self.my_city.id
        self.my_place.user_id = self.my_user.id
        self.my_place.name = "Sun N Sands"
        self.my_place.description = "Eat all you can."
        self.my_place.number_rooms = "Lemme count."
        self.my_place.number_bathrooms = "Plenty"
        self.my_place.max_guest = "Come all"
        self.my_place.price_by_night = "We will agree."
        self.my_place.latitude = "Equator"
        self.my_place.longitude = "We have forgotten"
        self.my_place.amenity_ids = self.amenity.id
        self.assertEqual(self.my_place.city_id, self.my_city.id)
        self.assertEqual(self.my_place.user_id, self.my_user.id)
        self.assertIs(self.my_place.name, "Sun N Sands")
        self.assertIs(self.my_place.description, "Eat all you can.")
        self.assertIs(self.my_place.number_rooms, "Lemme count.")
        self.assertIs(self.my_place.number_bathrooms, "Plenty")
        self.assertIs(self.my_place.max_guest, "Come all")
        self.assertIs(self.my_place.price_by_night, "We will agree.")
        self.assertIs(self.my_place.latitude, "Equator")
        self.assertIs(self.my_place.longitude, "We have forgotten")
        self.assertEqual(self.my_place.amenity_ids, self.amenity.id)
        self.my_place.city_id = [self.my_city.id]
        self.my_place.user_id = [self.my_user.id]
        self.my_place.name = ["Sun N Sands"]
        self.my_place.description = ["Eat all you can."]
        self.my_place.number_rooms = ["Lemme count."]
        self.my_place.number_bathrooms = ["Plenty"]
        self.my_place.max_guest = ["Come all"]
        self.my_place.price_by_night = ["We will agree."]
        self.my_place.latitude = ["Equator"]
        self.my_place.longitude = ["We have forgotten"]
        self.my_place.amenity_ids = [self.amenity.id]
        self.assertEqual(self.my_place.city_id, [self.my_city.id])
        self.assertEqual(self.my_place.user_id, [self.my_user.id])
        self.assertEqual(self.my_place.name, ["Sun N Sands"])
        self.assertEqual(self.my_place.description, ["Eat all you can."])
        self.assertEqual(self.my_place.number_rooms, ["Lemme count."])
        self.assertEqual(self.my_place.number_bathrooms, ["Plenty"])
        self.assertEqual(self.my_place.max_guest, ["Come all"])
        self.assertEqual(self.my_place.price_by_night, ["We will agree."])
        self.assertEqual(self.my_place.latitude, ["Equator"])
        self.assertEqual(self.my_place.longitude, ["We have forgotten"])
        self.assertEqual(self.my_place.amenity_ids, [self.amenity.id])
        self.my_place.city_id = {self.my_city.id}
        self.my_place.user_id = {self.my_user.id}
        self.my_place.name = {"Sun N Sands"}
        self.my_place.description = {"Eat all you can."}
        self.my_place.number_rooms = {"Lemme count."}
        self.my_place.number_bathrooms = {"Plenty"}
        self.my_place.max_guest = {"Come all"}
        self.my_place.price_by_night = {"We will agree."}
        self.my_place.latitude = {"Equator"}
        self.my_place.longitude = {"We have forgotten"}
        self.my_place.amenity_ids = {self.amenity.id}
        self.assertEqual(self.my_place.city_id, {self.my_city.id})
        self.assertEqual(self.my_place.user_id, {self.my_user.id})
        self.assertEqual(self.my_place.name, {"Sun N Sands"})
        self.assertEqual(self.my_place.description, {"Eat all you can."})
        self.assertEqual(self.my_place.number_rooms, {"Lemme count."})
        self.assertEqual(self.my_place.number_bathrooms, {"Plenty"})
        self.assertEqual(self.my_place.max_guest, {"Come all"})
        self.assertEqual(self.my_place.price_by_night, {"We will agree."})
        self.assertEqual(self.my_place.latitude, {"Equator"})
        self.assertEqual(self.my_place.longitude, {"We have forgotten"})
        self.assertEqual(self.my_place.amenity_ids, {self.amenity.id})
        self.my_place.city_id = {'city_id': self.my_city.id}
        self.my_place.user_id = {'user_id': self.my_user.id}
        self.my_place.name = {'name': "Sun N Sands"}
        self.my_place.description = {'description': "Eat all you can."}
        self.my_place.number_rooms = {'number_rooms': "Come count."}
        self.my_place.number_bathrooms = {'number_bathrooms': "Plenty"}
        self.my_place.max_guest = {'max_guest': "Come all"}
        self.my_place.price_by_night = {'price_by_night': "We will agree."}
        self.my_place.latitude = {'latitude': "Equator"}
        self.my_place.longitude = {'longitude': "We have forgotten"}
        self.my_place.amenity_ids = {'amenity_ids': self.amenity.id}
        self.assertEqual(self.my_place.city_id, {'city_id': self.my_city.id})
        self.assertEqual(self.my_place.user_id, {'user_id': self.my_user.id})
        self.assertEqual(self.my_place.name, {'name': "Sun N Sands"})
        self.assertEqual(self.my_place.description,
                         {'description': "Eat all you can."})
        self.assertEqual(self.my_place.number_rooms,
                         {'number_rooms': "Come count."})
        self.assertEqual(self.my_place.number_bathrooms,
                         {'number_bathrooms': "Plenty"})
        self.assertEqual(self.my_place.max_guest, {'max_guest': "Come all"})
        self.assertEqual(self.my_place.price_by_night,
                         {'price_by_night': "We will agree."})
        self.assertEqual(self.my_place.latitude, {'latitude': "Equator"})
        self.assertEqual(self.my_place.longitude,
                         {'longitude': "We have forgotten"})
        self.assertEqual(self.my_place.amenity_ids,
                         {'amenity_ids': self.amenity.id})
        self.my_place.city_id = 11
        self.my_place.user_id = 12
        self.my_place.name = 13
        self.my_place.description = 14
        self.my_place.number_rooms = 300
        self.my_place.number_bathrooms = 300
        self.my_place.max_guest = 50
        self.my_place.price_by_night = 18500
        self.my_place.latitude = 19.9808
        self.my_place.longitude = 20.8776
        self.my_place.amenity_ids = 15
        self.assertIs(self.my_place.city_id, 11)
        self.assertIs(self.my_place.user_id, 12)
        self.assertIs(self.my_place.name, 13)
        self.assertIs(self.my_place.description, 14)
        self.assertIs(self.my_place.number_rooms, 300)
        self.assertIs(self.my_place.number_bathrooms, 300)
        self.assertIs(self.my_place.max_guest, 50)
        self.assertIs(self.my_place.price_by_night, 18500)
        self.assertIs(self.my_place.latitude, 19.9808)
        self.assertIs(self.my_place.longitude, 20.8776)
        self.assertIs(self.my_place.amenity_ids, 15)

    def test_init_1(self):
        """
        Tests the Init method.
        """
        self.assertIs(self.my_place.__class__.__name__, 'Place')
        self.assertIn('created_at', self.my_place.__dict__)
        self.assertIn('updated_at', self.my_place.__dict__)
        self.assertIn('id', self.my_place.__dict__)
        self.assertIs(type(self.my_place.__dict__['id']), str)
        self.assertIs(type(self.my_place.__dict__['created_at']),
                      datetime.datetime)
        self.assertIs(type(self.my_place.__dict__['updated_at']),
                      datetime.datetime)

    def test_str_1(self):
        """
        Tests the string method.
        """
        str_text1 = f"[{self.my_place.__class__.__name__}] "
        str_text2 = f"({self.my_place.id}) {self.my_place.__dict__}\n"
        str_text = str_text1 + str_text2
        with patch('sys.stdout', new=StringIO()) as mock_print:
            print(self.my_place)
            self.assertEqual(mock_print.getvalue(), str_text)

    def test_save_1(self):
        """
        Tests the save method.
        """
        first_update = self.my_place.updated_at
        self.assertIn(self.my_place_key, storage.all())
        self.assertIs(storage.all()[self.my_place_key], self.my_place)
        self.my_place.save()
        self.assertNotEqual(first_update, self.my_place.updated_at)
        with open('file.json', 'r', encoding='utf-8') as file:
            saved_objects = json.load(file)
            self.assertIn(self.my_place_key, saved_objects)
        storage.reload()
        self.assertIsNot(storage.all()[self.my_place_key], self.my_place)
        self.assertEqual(storage.all()[self.my_place_key].to_dict_1(),
                         self.my_place.to_dict_1())

    def test_to_dict_1(self):
        """
        Tests the to_dIct method.
        """
        self.assertNotEqual(self.my_place.__dict__,
                            self.my_place.to_dict_1())
        self.assertIn('__class__', self.my_place.to_dict_1())
        self.assertNotIn('__class__', self.my_place.__dict__)
        self.assertIs(type(self.my_place.to_dict_1()['created_at']), str)
        self.assertIs(type(self.my_place.to_dict_1()['updated_at']), str)

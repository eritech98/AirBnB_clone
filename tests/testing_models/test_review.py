#!/usr/bin/python3

"""
Has tests for The class Review.
"""

import unittest
import datetime
import json
from io import StringIO
from unittest.mock import patch
from models.review import Review
from models.place import Place
from models.user import User
from models import storage


class TestReview_1(unittest.TestCase):
    """
    Tests the Revew class and its attributes
    """

    def setUp(self):
        self.my_review = Review()
        self.my_review_key = f"Review.{self.my_review.id_1}"
        self.my_place = Place()
        self.my_user = User()

    def test_public_class_attributes_1(self):
        """
        Tests the public class attribUtes.
        """
        self.assertIs(Review.place_id, "")
        self.assertIs(Review.user_id, "")
        self.assertIs(Review.text, "")
        self.assertNotIn('place_id', self.my_review.__dict__)
        self.assertNotIn('user_id', self.my_review.__dict__)
        self.assertNotIn('text', self.my_review.__dict__)
        self.my_review.place_id = self.my_place.id_1
        self.my_review.user_id = self.my_user.id_1
        self.my_review.text = "I liked the beach and the swings."
        self.assertIs(self.my_review.place_id, self.my_place.id_1)
        self.assertIs(self.my_review.user_id, self.my_user.id_1)
        self.assertIs(self.my_review.text,
                      "I liked the beach and the swings.")
        self.my_review.place_id = 12
        self.my_review.user_id = 13
        self.my_review.text = 14
        self.assertIs(self.my_review.place_id, 12)
        self.assertIs(self.my_review.user_id, 13)
        self.assertIs(self.my_review.text, 14)
        self.my_review.place_id = [self.my_place.id_1]
        self.my_review.user_id = [self.my_user.id_1]
        self.my_review.text = ["I liked the beach and the swings."]
        self.assertEqual(self.my_review.place_id, [self.my_place.id_1])
        self.assertEqual(self.my_review.user_id, [self.my_user.id_1])
        self.assertEqual(self.my_review.text,
                         ["I liked the beach and the swings."])
        self.my_review.place_id = {self.my_place.id_1}
        self.my_review.user_id = {self.my_user.id_1}
        self.my_review.text = {"I liked the beach and the swings."}
        self.assertEqual(self.my_review.place_id, {self.my_place.id_1})
        self.assertEqual(self.my_review.user_id, {self.my_user.id_1})
        self.assertEqual(self.my_review.text,
                         {"I liked the beach and the swings."})
        self.my_review.place_id = {'place_id': self.my_place.id_1}
        self.my_review.user_id = {'user_id': self.my_user.id_1}
        self.my_review.text = {'text': "I liked the beach and the swings."}
        self.assertEqual(self.my_review.place_id,
                         {'place_id': self.my_place.id_1})
        self.assertEqual(self.my_review.user_id, {'user_id': self.my_user.id_1})
        self.assertEqual(self.my_review.text,
                         {'text': "I liked the beach and the swings."})
        self.my_review.place_id = (self.my_place.id_1, '897')
        self.my_review.user_id = (self.my_user.id_1, 908)
        self.my_review.text = ("I liked the beach and the swings.", 9)
        self.assertEqual(self.my_review.place_id, (self.my_place.id_1, '897'))
        self.assertEqual(self.my_review.user_id, (self.my_user.id_1, 908))
        self.assertEqual(self.my_review.text,
                         ("I liked the beach and the swings.", 9))
        self.my_review.place_id = True
        self.my_review.user_id = True
        self.my_review.text = True
        self.assertEqual(self.my_review.place_id, True)
        self.assertEqual(self.my_review.user_id, True)
        self.assertEqual(self.my_review.text, True)

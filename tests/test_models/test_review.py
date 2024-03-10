#!/usr/bin/python3
"""Unitteset for review.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.review import Review


class TestReview_instantiate(unittest.TestCase):
    """Test Review."""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_text_is_public_attribute(self):
        self.assertEqual(str, type(Review.text))

    def test_user_id_is_public_attribute(self):
        self.assertEqual(str, type(Review.user_id))

    def test_place_id_is_public_attribute(self):
        self.assertEqual(str, type(Review.place_id))

    def test_unique_ids(self):
        id1 = Review()
        id2 = Review()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = Review()
        id2 = Review()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = Review()
        id2 = Review()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(created_at=None)

    def test_instantiate_kwargs(self):
        one = Review(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = Review("12")
        self.assertNotIn("12", one.__dict__)


class TestReview_save(unittest.TestCase):
    """Test saving of Review cass."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_once(self):
        one = Review()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = Review()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = Review()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = Review()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestReview_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = Review()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = Review()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = Review()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = Review()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = Review()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

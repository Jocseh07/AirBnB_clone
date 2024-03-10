#!/usr/bin/python3
"""Unitteset for amenity.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.amenity import Amenity


class TestAmenity_instantiate(unittest.TestCase):
    """Test Amenity."""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_attribute(self):
        one = Amenity()
        self.assertEqual(str, type(Amenity.name))

    def test_unique_ids(self):
        id1 = Amenity()
        id2 = Amenity()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = Amenity()
        id2 = Amenity()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = Amenity()
        id2 = Amenity()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(created_at=None)

    def test_instantiate_kwargs(self):
        one = Amenity(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = Amenity("12")
        self.assertNotIn("12", one.__dict__)


class TestAmenity_save(unittest.TestCase):
    """Test saving of Amenity cass."""

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
        one = Amenity()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = Amenity()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = Amenity()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = Amenity()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestAmenity_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = Amenity()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = Amenity()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = Amenity()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = Amenity()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = Amenity()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

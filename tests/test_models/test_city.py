#!/usr/bin/python3
"""Unitteset for city.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.city import City


class TestCity_instantiate(unittest.TestCase):
    """Test City."""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored(self):
        self.assertIn(City(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public_attribute(self):
        one = City()
        self.assertEqual(str, type(City.name))

    def test_state_id_is_public_attribute(self):
        one = City()
        self.assertEqual(str, type(City.state_id))

    def test_unique_ids(self):
        id1 = City()
        id2 = City()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = City()
        id2 = City()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = City()
        id2 = City()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(created_at=None)

    def test_instantiate_kwargs(self):
        one = City(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = City("12")
        self.assertNotIn("12", one.__dict__)


class TestCity_save(unittest.TestCase):
    """Test saving of City cass."""

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
        one = City()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = City()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = City()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = City()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestCity_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = City()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = City()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = City()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = City()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = City()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

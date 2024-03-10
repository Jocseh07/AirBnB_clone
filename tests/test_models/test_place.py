#!/usr/bin/python3
"""Unitteset for place.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.place import Place


class TestPlace_instantiate(unittest.TestCase):
    """Test Place."""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored(self):
        self.assertIn(Place(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_name_is_public_attribute(self):
        one = Place()
        self.assertEqual(str, type(Place.name))

    def test_city_id_is_public_attribute(self):
        one = Place()
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_public_attribute(self):
        one = Place()
        self.assertEqual(str, type(Place.user_id))

    def test_description_is_public_attribute(self):
        one = Place()
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_public_attribute(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_public_attribute(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_public_attribute(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_public_attribute(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_public_attribute(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_public_attribute(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_public_attribute(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_unique_ids(self):
        id1 = Place()
        id2 = Place()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = Place()
        id2 = Place()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = Place()
        id2 = Place()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(created_at=None)

    def test_instantiate_kwargs(self):
        one = Place(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = Place("12")
        self.assertNotIn("12", one.__dict__)


class TestPlace_save(unittest.TestCase):
    """Test saving of Place cass."""

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
        one = Place()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = Place()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = Place()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = Place()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestPlace_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = Place()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = Place()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = Place()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = Place()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = Place()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unitteset for state.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.state import State


class TestState_instantiate(unittest.TestCase):
    """Test State."""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored(self):
        self.assertIn(State(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_attribute(self):
        one = State()
        self.assertEqual(str, type(State.name))

    def test_unique_ids(self):
        id1 = State()
        id2 = State()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = State()
        id2 = State()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = State()
        id2 = State()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(created_at=None)

    def test_instantiate_kwargs(self):
        one = State(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = State("12")
        self.assertNotIn("12", one.__dict__)


class TestState_save(unittest.TestCase):
    """Test saving of State cass."""

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
        one = State()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = State()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = State()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = State()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestState_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = State()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = State()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = State()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = State()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = State()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

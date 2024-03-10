#!/usr/bin/python3
"""Unitteset for user.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.user import User


class TestUser_instantiate(unittest.TestCase):
    """Test User."""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored(self):
        self.assertIn(User(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_attribute(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_attribute(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_attribute(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_attribute(self):
        self.assertEqual(str, type(User.first_name))

    def test_unique_ids(self):
        id1 = User()
        id2 = User()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = User()
        id2 = User()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = User()
        id2 = User()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(created_at=None)

    def test_instantiate_kwargs(self):
        one = User(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = User("12")
        self.assertNotIn("12", one.__dict__)


class TestUser_save(unittest.TestCase):
    """Test saving of User cass."""

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
        one = User()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = User()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = User()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = User()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestUser_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = User()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = User()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = User()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = User()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = User()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

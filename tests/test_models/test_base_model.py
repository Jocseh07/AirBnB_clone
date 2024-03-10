#!/usr/bin/python3
"""Unitteset for base_model.py."""

import os
import unittest
from datetime import datetime

from models import storage
from models.base_model import BaseModel


class TestBaseModel_instantiate(unittest.TestCase):
    """Test BaseModel."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_created_different_times(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertLess(id1.created_at, id2.created_at)

    def test_updated_different_times(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertLess(id1.updated_at, id2.created_at)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=None)

    def test_instantiate_kwargs(self):
        one = BaseModel(id="1")
        self.assertEqual(one.id, "1")

    def test_args(self):
        one = BaseModel("12")
        self.assertNotIn("12", one.__dict__)


class TestBaseModel_save(unittest.TestCase):
    """Test saving of BaseModel cass."""

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
        one = BaseModel()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_twice(self):
        one = BaseModel()
        first = one.updated_at
        one.save()
        second = one.updated_at
        self.assertLess(first, second)

    def test_save_with_arg(self):
        one = BaseModel()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_save_in_file(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        one = BaseModel()
        one.save()
        with open("file.json", "r") as f:
            self.assertIn(one.id, f.read())


class TestBaseModel_dict(unittest.TestCase):
    """test dict methods."""

    def test_to_dict(self):
        one = BaseModel()
        self.assertEqual(dict, type(one.to_dict()))

    def test_keys(self):
        one = BaseModel()
        self.assertIn("id", one.to_dict())

    def test_attributes(self):
        one = BaseModel()
        one.name = "alx"
        self.assertIn("name", one.to_dict())

    def test_datetime_attributes(self):
        one = BaseModel()
        onedict = one.to_dict()
        self.assertEqual(str, type(onedict["created_at"]))
        self.assertEqual(str, type(onedict["updated_at"]))

    def test_to_dict_args(self):
        one = BaseModel()
        with self.assertRaises(TypeError):
            one.to_dict(None)


if __name__ == "__main__":
    unittest.main()

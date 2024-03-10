#!/usr/bin/python3
"""Unitteset for base_model.py."""

import os
import unittest

import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage_instantiate(unittest.TestCase):
    """Test FileStorage."""

    def test_no_args(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_unique_ids(self):
        id1 = FileStorage()
        id2 = FileStorage()
        self.assertNotEqual(id1, id2)

    def test_instantiate_None_kwargs(self):
        with self.assertRaises(TypeError):
            FileStorage(created_at=None)


class TestFileStorage_save(unittest.TestCase):
    """Test saving of FileStorage cass."""

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
        one = FileStorage()
        one.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save_with_arg(self):
        one = FileStorage()
        with self.assertRaises(TypeError):
            one.save(None)

    def test_reload_with_arg(self):
        one = FileStorage()
        with self.assertRaises(TypeError):
            one.reload(None)

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        one = BaseModel()
        two = User()
        three = State()
        four = Place()
        five = City()
        six = Amenity()
        seven = Review()
        models.storage.new(one)
        models.storage.new(two)
        models.storage.new(three)
        models.storage.new(four)
        models.storage.new(five)
        models.storage.new(six)
        models.storage.new(seven)
        self.assertIn("BaseModel." + one.id, models.storage.all().keys())
        self.assertIn(one, models.storage.all().values())
        self.assertIn("User." + two.id, models.storage.all().keys())
        self.assertIn(two, models.storage.all().values())
        self.assertIn("State." + three.id, models.storage.all().keys())
        self.assertIn(three, models.storage.all().values())
        self.assertIn("Place." + four.id, models.storage.all().keys())
        self.assertIn(four, models.storage.all().values())
        self.assertIn("City." + five.id, models.storage.all().keys())
        self.assertIn(five, models.storage.all().values())
        self.assertIn("Amenity." + six.id, models.storage.all().keys())
        self.assertIn(six, models.storage.all().values())
        self.assertIn("Review." + seven.id, models.storage.all().keys())
        self.assertIn(seven, models.storage.all().values())

    def test_save(self):
        one = BaseModel()
        two = User()
        three = State()
        four = Place()
        seven = City()
        five = Amenity()
        six = Review()
        storage.new(one)
        storage.new(two)
        storage.new(three)
        storage.new(four)
        storage.new(five)
        storage.new(six)
        storage.new(seven)
        storage.save()
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + one.id, text)
            self.assertIn("User." + two.id, text)
            self.assertIn("State." + three.id, text)
            self.assertIn("Place." + four.id, text)
            self.assertIn("Amenity." + five.id, text)
            self.assertIn("Review." + six.id, text)
            self.assertIn("City." + seven.id, text)

    def test_reload(self):
        one = BaseModel()
        two = User()
        three = State()
        four = Place()
        five = Amenity()
        seven = City()
        six = Review()
        storage.new(one)
        storage.new(two)
        storage.new(three)
        storage.new(four)
        storage.new(five)
        storage.new(six)
        storage.new(seven)
        storage.save()
        storage.reload()
        f = storage.all()
        self.assertIn("BaseModel." + one.id, f)
        self.assertIn("User." + two.id, f)
        self.assertIn("State." + three.id, f)
        self.assertIn("Place." + four.id, f)
        self.assertIn("Amenity." + five.id, f)
        self.assertIn("Review." + six.id, f)
        self.assertIn("City." + seven.id, f)


if __name__ == "__main__":
    unittest.main()

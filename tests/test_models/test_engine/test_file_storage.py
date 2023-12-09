#!/usr/bin/python3
"""
these are the tests for file storage class
"""

from unittest import TestCase, main
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import os
import json


class TestFileStorage_type(TestCase):
    """
    Define TestCases of FileStorage
    """

    def test_file_storage_objects_type(self):
        """
        test file storage objects type
        """
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_file_storage_file_path_type(self):
        """
        test file storage file path type
        """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_file_storage_instance_storage(self):
        """
        test file storage instance storage
        """
        self.assertIsInstance(models.storage, FileStorage)

    def test_file_storage_instance(self):
        """
        test file storage instance
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_all(TestCase):
    """
    Define TestCase related to all method
    """

    def test_storage_new_instance(self):
        """
        test storage new instance
        """
        base = BaseModel()
        objs_keys = models.storage.all().keys()
        self.assertIn("BaseModel.{}".format(base.id), objs_keys)

    def test_storage_multiple_instances(self):
        """
        test storage multiple instances
        """
        user = User()
        place = Place()
        base = BaseModel()
        objs_keys = models.storage.all().keys()
        self.assertIn("BaseModel.{}".format(base.id), objs_keys)
        self.assertIn("Place.{}".format(place.id), objs_keys)
        self.assertIn("User.{}".format(user.id), objs_keys)

    def test_file_storage_all_with_args(self):
        """
        test file storage all with args
        """
        with self.assertRaises(TypeError):
            models.storage.all("args")


class TestFileStorage_new(TestCase):
    """
    Define TestCase related to new method
    """

    def test_storage_new_with_multiple_args(self):
        """
        test storage new with multiple args
        """
        with self.assertRaises(TypeError):
            models.storage.new(None, "args")

    def test_storage_new_no_valid_obj(self):
        """
        test storage new no valid obj
        """
        with self.assertRaises(AttributeError):
            models.storage.new("args")

    def test_storage_new_instances(self):
        """
        test storage new instances
        """
        base = BaseModel()
        user = User()
        place = Place()
        amenity = Amenity()
        review = Review()
        city = City()
        state = State()
        models.storage.new(base)
        models.storage.new(user)
        models.storage.new(place)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.new(city)
        models.storage.new(state)
        Objs = models.storage.all()
        self.assertIn("BaseModel.{}".format(base.id), Objs.keys())
        self.assertIn("User.{}".format(user.id), Objs.keys())
        self.assertIn("Place.{}".format(place.id), Objs.keys())
        self.assertIn("Amenity.{}".format(amenity.id), Objs.keys())
        self.assertIn("Review.{}".format(review.id), Objs.keys())
        self.assertIn("City.{}".format(city.id), Objs.keys())
        self.assertIn("State.{}".format(state.id), Objs.keys())


class TestFileStorage_save(TestCase):
    """
    Define TestCase related to save method
    """

    file_path = "File.json"

    def setUp(self):
        """setUp will be executed before each test case"""
        try:
            os.remove(self.file_path)
        except Exception:
            pass

    def test_file_storage_save_with_args(self):
        """
        test file storage save with args
        """
        with self.assertRaises(TypeError):
            models.storage.save("args")

    def test_file_storage_save_into_file(self):
        """
        test file storage save into file
        """
        base = BaseModel()
        user = User()
        place = Place()
        self.assertEqual(os.path.exists(self.file_path), False)
        models.storage.save()
        self.assertEqual(os.path.exists(self.file_path), True)
        with open(self.file_path, "r", encoding="utf-8") as file:
            dicts = json.load(file)
            self.assertIn("BaseModel.{}".format(base.id), dicts.keys())
            self.assertIn("Place.{}".format(place.id), dicts.keys())
            self.assertIn("User.{}".format(user.id), dicts.keys())


class TestFileStorage_reload(TestCase):
    """
    Define TestCase related to reload method
    """

    def test_file_storage_reload(self):
        """
        test file storage reload
        """
        base = BaseModel()
        user = User()
        place = Place()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        self.assertEqual(models.storage.all(), {})
        models.storage.reload()
        self.assertNotEqual(models.storage.all(), {})

    def test_file_storage_reload_check_data(self):
        """
        test file storage reload check data
        """
        base = BaseModel()
        user = User()
        place = Place()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        objs_keys = models.storage.all().keys()
        self.assertIn("BaseModel.{}".format(base.id), objs_keys)
        self.assertIn("Place.{}".format(place.id), objs_keys)
        self.assertIn("User.{}".format(user.id), objs_keys)

    def test_file_storage_reload_with_args(self):
        """
        test file storage reload with args
        """
        with self.assertRaises(TypeError):
            models.storage.reload("args")


if __name__ == "__main__":
    main()
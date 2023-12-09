#!/usr/bin/python3
"""
These are the tests for the City Class
"""

import unittest
from unittest import TestCase, main
from models.base_model import BaseModel
from models.city import City
from models.state import State
import uuid


class TestCity(TestCase):
    """
    Definition of Test Class of City
    """

    def test_city_inherits_base_model(self):
        """
        test city inherits base model
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_with_valid_id(self):
        """
        test city with valid id
        """
        city = City()
        self.assertEqual(str(uuid.UUID(city.id)), city.id)

    def test_city_check_attributes(self):
        """
        test city check attributes
        """
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_set_name(self):
        """
        test city set name
        """
        city = City()
        city.name = "Marrakech"
        self.assertEqual(city.name, "Marrakech")

    def test_city_set_state_id(self):
        """
        test city set name
        """
        city = City()
        state = State()
        city.state_id = state.id
        self.assertEqual(city.state_id, state.id)

    def test_city_to_dict(self):
        """
        test city to dict
        """
        city = City()
        city_dict = {
                "__class__": "City",
                "id": city.id,
                "created_at": city.created_at.isoformat(),
                "updated_at": city.updated_at.isoformat()
                }
        self.assertDictEqual(city_dict, city.to_dict())
        city_dict["name"] = "Marrakech"
        city.name = "Marrakech"
        self.assertDictEqual(city_dict, city.to_dict())

    def test_city_initialise_with_kwargs(self):
        """
        test initialise city with kwargs
        """
        state_id = State().id
        c_dict = {
                "id": str(uuid.uuid4()),
                "state_id": state_id,
                "name": "Miami"
                }
        city = City(**c_dict)
        self.assertEqual(c_dict["id"], city.id)
        self.assertEqual(city.name, "Miami")
        self.assertEqual(city.state_id, state_id)

    def test_city_initialise_with_args(self):
        """
        test initialise city by using args
        """
        city = City("xxxxxxxxxxxxxxxxxxx")
        self.assertNotIn("xxxxxxxxxxxxxxxxxxx", city.__dict__.values())

    def test_city_str_representation(self):
        """
        test city str representation
        """
        city = City()
        c_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(city.__str__(), c_str)

    def test_city_initialise_with_empty_kwargs(self):
        """
        test initialise city with empty kwargs
        """
        c_dict = {}
        city = City(**c_dict)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    main()

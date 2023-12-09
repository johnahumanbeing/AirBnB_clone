#!/usr/bin/python3
"""
These are the tests for the Place Class
"""
import unittest
from unittest import TestCase, main
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
import uuid


class TestPlace(TestCase):
    """
    Definition of Test Class of Place
    """

    def test_place_inherits_base_model(self):
        """
        test place inherits base model
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_with_valid_id(self):
        """
        test place with valid id
        """
        place = Place()
        self.assertEqual(str(uuid.UUID(place.id)), place.id)

    def test_place_check_attributes(self):
        """
        test place check attributes
        """
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_set_name(self):
        """
        test place set name
        """
        place = Place()
        place.name = "Hotel de france"
        self.assertEqual(place.name, "Hotel de france")

    def test_place_set_city_id(self):
        """
        test place set city id
        """
        city = City()
        place = Place()
        place.city_id = city.id
        self.assertEqual(place.city_id, city.id)

    def test_place_set_user_id(self):
        """
        test place set user id
        """
        user = User()
        place = Place()
        place.user_id = user.id
        self.assertEqual(place.user_id, user.id)

    def test_place_set_description(self):
        """
        test place set description
        """
        place = Place()
        desc = "Hotel de France est le meilleur Hotel au Marrakech"
        place.description = desc
        self.assertEqual(place.description, desc)

    def test_place_set_number_rooms(self):
        """
        test place set description
        """
        place = Place()
        place.number_rooms = 450
        self.assertEqual(place.number_rooms, 450)

    def test_place_set_number_bathrooms(self):
        """
        test place set bathrooms
        """
        place = Place()
        place.number_bathrooms = 650
        self.assertEqual(place.number_bathrooms, 650)

    def test_place_set_max_guest(self):
        """
        test place max guest"""
        place = Place()
        place.max_guest = 900

        self.assertEqual(place.max_guest, 900)

    def test_place_set_price_by_night(self):
        """
        test place price by night
        """
        place = Place()
        place.price_by_night = 1000
        self.assertEqual(place.price_by_night, 1000)

    def test_place_set_latitude(self):
        """
        test place latitude
        """
        place = Place()
        place.latitude = 145.66
        self.assertEqual(place.latitude, 145.66)

    def test_place_set_longitude(self):
        """
        test place longitude
        """
        place = Place()
        place.longitude = -45.89
        self.assertEqual(place.longitude, -45.89)

    def test_place_set_longitude(self):
        """
        test place longitude
        """
        place = Place()
        amenity_dict = [Amenity().id for i in range(3)]
        place.amenity_ids = amenity_dict
        self.assertEqual(place.amenity_ids, amenity_dict)

    def test_place_to_dict(self):
        """
        test place to dict
        """
        place = Place()
        place_dict = {
                "__class__": "Place",
                "id": place.id,
                "created_at": place.created_at.isoformat(),
                "updated_at": place.updated_at.isoformat()
                }
        self.assertDictEqual(place_dict, place.to_dict())
        place_dict["name"] = "Hotel Farah"
        place.name = "Hotel Farah"
        self.assertDictEqual(place_dict, place.to_dict())
        place_dict["latitude"] = 85.20
        place.latitude = 85.20
        self.assertDictEqual(place_dict, place.to_dict())
        place_dict["max_guest"] = 643
        place.max_guest = 643
        self.assertDictEqual(place_dict, place.to_dict())

    def test_place_str_representation(self):
        """
        test place str representation
        """
        place = Place()
        p_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(place.__str__(), p_str)

    def test_place_initialise_with_args(self):
        """
        test initialise place by using args
        """
        place = Place("xxxxxxxxxxxxxxxxxxx")
        self.assertNotIn("xxxxxxxxxxxxxxxxxxx", place.__dict__.values())

    def test_place_initialise_with_empty_kwargs(self):
        """
        test initialise user with empty kwargs
        """
        p_dict = {}
        place = Place(**p_dict)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_initialise_with_kwargs(self):
        """
        test initialise place with kwargs
        """
        p_dict = {
                "id": str(uuid.uuid4()),
                "city_id": "hhhh-hhhh-hhhh-hhhh",
                "user_id": "yyyy-yyyy-yyyy-yyyy",
                "name": "Hotel",
                "description": "Best Hotel",
                "number_rooms": 500,
                "number_bathrooms": 1000,
                "max_guest": 1500,
                "price_by_night": 750,
                "latitude": -1.286,
                "longitude": 36.817,
                }
        place = Place(**p_dict)
        self.assertEqual(place.city_id, "hhhh-hhhh-hhhh-hhhh")
        self.assertEqual(place.user_id, "yyyy-yyyy-yyyy-yyyy")
        self.assertEqual(place.name, "Hotel")
        self.assertEqual(place.description, "Best Hotel")
        self.assertEqual(place.number_rooms, 500)
        self.assertEqual(place.number_bathrooms, 1000)
        self.assertEqual(place.max_guest, 1500)
        self.assertEqual(place.price_by_night, 750)
        self.assertEqual(place.latitude, -1.286)
        self.assertEqual(place.longitude, 36.817)


if __name__ == "__main__":
    main()

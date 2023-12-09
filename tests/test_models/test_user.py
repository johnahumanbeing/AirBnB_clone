#!/usr/bin/python3
"""
These are the tests for the User Class
"""
import unittest
from unittest import TestCase, main
from models.base_model import BaseModel
from models.user import User
import uuid


class TestUser(TestCase):
    """
    Definition of Test Class of User
    """

    def test_user_inherits_base_model(self):
        """
        test user inherits base model
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_with_valid_id(self):
        """
        test user with valid id
        """
        user = User()
        self.assertEqual(str(uuid.UUID(user.id)), user.id)

    def test_user_check_attributes(self):
        """
        test user check attributes
        """
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_set_first_name(self):
        """
        test user set first name
        """
        user = User()
        user.first_name = "John"
        self.assertEqual(user.first_name, "John")

    def test_user_set_last_name(self):
        """
        test user set last name
        """
        user = User()
        user.last_name = "Ngala"
        self.assertEqual(user.last_name, "Ngala")

    def test_user_set_email(self):
        """
        test user set email
        """
        user = User()
        user.email = "Johnny@alx.com"
        self.assertEqual(user.email, "Johnny@alx.com")

    def test_user_set_password(self):
        """
        test user set password
        """
        user = User()
        user.password = "wahu@2023*$"
        self.assertEqual(user.password, "wahu@2023*$")

    def test_user_to_dict(self):
        """
        test user to dict
        """
        user = User()
        user_dict = {
                "__class__": "User",
                "id": user.id,
                "created_at": user.created_at.isoformat(),
                "updated_at": user.updated_at.isoformat()
                }
        self.assertDictEqual(user_dict, user.to_dict())
        user_dict["first_name"] = "John"
        user.first_name = "John"
        self.assertDictEqual(user_dict, user.to_dict())
        user_dict["last_name"] = "Ngala"
        user.last_name = "Ngala"
        self.assertDictEqual(user_dict, user.to_dict())

    def test_user_initialise_with_kwargs(self):
        """
        test initialise user with kwargs
        """
        u_dict = {
                "id": str(uuid.uuid4()),
                "first_name": "Ian",
                "last_name": "Njuguna"
                }
        user = User(**u_dict)
        self.assertEqual(u_dict["id"], user.id)
        self.assertEqual(user.first_name, "Ian")
        self.assertEqual(user.last_name, "Njuguna")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")

    def test_user_initialise_with_args(self):
        """
        test initialise user by using args
        """
        user = User("xxxxxxxxxxxxxxxxxxx")
        self.assertNotIn("xxxxxxxxxxxxxxxxxxx", user.__dict__.values())

    def test_user_str_representation(self):
        """
        test user str representation
        """
        user = User()
        u_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(user.__str__(), u_str)

    def test_user_initialise_with_empty_kwargs(self):
        """
        test initialise user with empty kwargs
        """
        u_dict = {}
        user = User(**u_dict)
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")


if __name__ == "__main__":
    main()
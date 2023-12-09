#!/usr/bin/python3
"""
These are the tests for the Review Class
"""
import unittest
from unittest import TestCase, main
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User
import uuid


class TestReview(TestCase):
    """
    Definition of Test Class of Review
    """

    def test_review_inherits_base_model(self):
        """
        test place inherits base model
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_with_valid_id(self):
        """
        test review with valid id
        """
        review = Review()
        self.assertEqual(str(uuid.UUID(review.id)), review.id)

    def test_review_check_attributes(self):
        """
        test review check attributes
        """
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_set_text(self):
        """
        test review set text
        """
        review = Review()
        review.text = "This is a dump review"
        self.assertEqual(review.text, "This is a dump review")

    def test_review_set_place_id(self):
        """
        test review set place id
        """
        place = Place()
        review = Review()
        review.place_id = place.id
        self.assertEqual(review.place_id, place.id)

    def test_review_set_user_id(self):
        """
        test review set user id
        """
        user = User()
        review = Review()
        review.user_id = user.id
        self.assertEqual(review.user_id, user.id)

    def test_review_to_dict(self):
        """
        test review to dict
        """
        review = Review()
        review_dict = {
                "__class__": "Review",
                "id": review.id,
                "created_at": review.created_at.isoformat(),
                "updated_at": review.updated_at.isoformat()
                }
        self.assertDictEqual(review_dict, review.to_dict())

        review_dict["text"] = "Test review"
        review.text = "Test review"
        self.assertDictEqual(review_dict, review.to_dict())

    def test_review_initialise_with_kwargs(self):
        """
        test initialise review with kwargs
        """
        place_id = Place().id
        user_id = User().id
        r_dict = {
            "id": str(uuid.uuid4()),
            "place_id": place_id,
            "user_id": user_id,
            "text": "Review test"
        }
        review = Review(**r_dict)
        self.assertEqual(r_dict["id"], review.id)
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, "Review test")

    def test_review_initialise_with_args(self):
        """
        test initialise review by using args
        """
        review = Review("xxxxxxxxxxxxxxxxxxx")
        self.assertNotIn("xxxxxxxxxxxxxxxxxxx", review.__dict__.values())

    def test_review_str_representation(self):
        """
        test review str representation
        """
        review = Review()
        r_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(review.__str__(), r_str)

    def test_review_initialise_with_empty_kwargs(self):
        """
        test initialise review with empty kwargs
        """
        r_dict = {}
        review = Review(**r_dict)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    main()

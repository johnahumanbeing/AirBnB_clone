#!/usr/bin/python3
"""
This is the test module for base_model
"""

import io
import models
from models.base_model import BaseModel
from unittest import TestCase, mock, main
import datetime
from io import StringIO

class TestBaseModel(TestCase):

    def test_unique_id(self):
        """
        testing  unique id
        """
        baseM1 = BaseModel()
        baseM2 = BaseModel()
        self.assertNotEqual(baseM1.id, baseM2.id)

    def test_created_at(self):
        mock_date = datetime.datetime.now()
        datetime_mock = mock.Mock(wraps=datetime.datetime)
        datetime_mock.now.return_value = mock_date
        with mock.patch('models.base_model.datetime', new=datetime_mock):
            base = BaseModel()
            self.assertEqual(base.created_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime.datetime.now()
        datetime_mock = mock.Mock(wraps=datetime.datetime)
        with mock.patch('models.base_model.datetime', new=datetime_mock):
            base = BaseModel()
            self.assertEqual(base.updated_at, mock_date)

    def test_2_instances_with_diff_dates(self):
        """
        test 2 instances with diff dates
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.created_at, base2.created_at)
        self.assertNotEqual(base1.updated_at, base2.updated_at)
        # self.assertNotEqual(base1.created_at, base1.updated_at)

    def test_type_attr_id(self):
        """
        testing type attr id
        """
        self.assertEqual(type(BaseModel().id), str)

    def test_type_attr_created_at(self):
        """
        test for type attr created at
        """
        self.assertEqual(type(BaseModel().created_at), datetime.datetime)

    def test_type_attr_updated_at(self):
        """
        test for type attr updated at
        """
        self.assertEqual(type(BaseModel().updated_at), datetime.datetime)


class TestBaseModel_save(TestCase):
    """
    TestBaseModel save
    """

    def test_updated_at_change(self):
        """
        test updated at change
        """
        base = BaseModel()
        updated_date = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, updated_date)

    def test_save_with_args(self):
        """
        test save with args
        """
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save("arg")

    def test_save_instance_to_storage(self):
        """
        test save instance to storage
        """
        base = BaseModel()
        self.assertIn(base, models.storage.all().values())


class TestBaseModel_to_dict(TestCase):
    """
    TestBaseModel to dict
    """

    def test_to_dict_with_args(self):
        """
        test to dict with args
        """
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict("arg")

    def test_to_dict_return_value(self):
        """
        test to dict return value
        """
        base = BaseModel()
        dict = {
            "__class__": "BaseModel",
            "id": base.id,
            "created_at": base.created_at.isoformat(),
            "updated_at": base.updated_at.isoformat()
        }
        self.assertDictEqual(base.to_dict(), dict)

    def test_to_dict_is_not__dict__(self):
        """
        test to dict is not __dict__
        """
        b = BaseModel()
        self.assertIn("__class__", b.to_dict().keys())
        self.assertNotIn("__class__", b.__dict__.keys())


class TestBaseModel_str(TestCase):
    """
    TestBaseModel str
    """

    def test_str_representation(self):
        """
        test str representation
        """
        base = BaseModel()
        base_str = "[{}] ({}) {}".format(base.__class__.__name__,
                                         base.id, base.__dict__)
        self.assertEqual(base.__str__(), base_str)

    def test_print_instance(self):
        """
        test print instance
        """
        b = BaseModel()
        clsName = b.__class__.__name__
        expectedOutput = "[{}] ({}) {}\n".format(clsName, b.id, b.__dict__)
        with mock.patch('sys.stdout', new=StringIO()) as out:
            print(b)
            self.assertEqual(out.getvalue(), expectedOutput)

    def test_str_with_arg(self):
        """
        test str with arg
        """
        with self.assertRaises(TypeError):
            BaseModel().__str__("arg")


class TestBaseModel_args(TestCase):
    """
    TestBaseModel args
    """

    def test_base_model_with_args(self):
        """
        test base model with args
        """
        arg1 = "args1"
        base = BaseModel(arg1)
        self.assertNotIn(arg1, base.__dict__.values())


class TestBaseModel_Kwargs(TestCase):
    """
    TestBaseModel Kwargs
    """

    def test_base_model_with_kwargs(self):
        """
        test base model with kwargs
        """
        base = BaseModel(first_name="Hajar", last_name="El Abdellaoui")
        self.assertIn("first_name", base.__dict__.keys())
        self.assertIn("last_name", base.__dict__.keys())
        self.assertIn("Hajar", base.__dict__.values())
        self.assertIn("El Abdellaoui", base.__dict__.values())

    def test_base_model_created_at_type_None(self):
        """
        test base model created at type None
        """
        with self.assertRaises(TypeError):
            base = BaseModel(created_at=None)

    def test_base_model_updated_at_type_None(self):
        """
        test base model updated at type None
        """
        with self.assertRaises(TypeError):
            base = BaseModel(updated_at=None)


if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
These are the tests for the whole console
"""

import unittest
from unittest import TestCase, mock, main
from console import HBNBCommand
from io import StringIO
import uuid
from models.base_model import BaseModel
import json
import models
import os
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage

class TestConsole_prompt(TestCase):
    """Test console prompt"""

    def test_console_prompt_value(self):
        """test console prompt value"""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_console_with_empty_line_or_space(self):
        """test console with empty line or space"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual("", output.getvalue().strip())

    def test_console_with_new_line(self):
        """test console with new line"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", output.getvalue().strip())


class TestConsole_help(TestCase):
    """Test case command"""

    def test_console_help_command(self):
        """test help command"""
        expected = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  create  destroy  help  quit  show  "
                    "update")
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_help_EOF(self):
        """test console help EOF"""
        expected_output = "Exit when EOF or when Press CTRL+D"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_console_help_quit(self):
        """test console help quit"""
        expected_output = "Quit to exit the program"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_console_help_create(self):
        """test console help create"""
        e = "Creates instance and save it to a JSON file Usage:create <class>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_show(self):
        """test console help show"""
        e = "Prints str representation of instance Usage:show <class> <id>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_all(self):
        """test console help all"""
        e = "Prints str repr of"
        e += " all class instances Usage:all <class>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_destroy(self):
        """test console help destroy"""
        e = "Deletes an instance Usage:destroy <class> <id>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_update(self):
        """test console help update"""
        e = "Updates an instance Usage:update <class> <id> <attr> <value>"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertEqual(e, output.getvalue().strip())

    def test_console_help_count(self):
        """test console help count"""
        e = "Returns the number of class instances"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help count")
            self.assertEqual(e, output.getvalue().strip())


class TestConsole_create(TestCase):
    """Test create command"""

    file_path = "File.json"

    def test_create_with_missing_class(self):
        """test create with missing class"""
        e = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(e, output.getvalue().strip())

    def test_create_with_non_exist_class(self):
        """test create with non exist class"""
        e = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create NonExistClass"))
            self.assertEqual(e, output.getvalue().strip())

    def test_create_base_model(self):
        """test create base model"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_user(self):
        """test create user"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create User"))
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_place(self):
        """test create place"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Place"))
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_amenity(self):
        """test create amenity"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                HBNBCommand().onecmd("create Amenity")
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_state(self):
        """test create state"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create State"))
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_city(self):
        """test create city"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create City"))
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_review(self):
        """test create review"""
        mock_id = str(uuid.uuid4())
        uuid_mock = mock.Mock(wraps=uuid.uuid4)
        uuid_mock.return_value = mock_id
        with mock.patch('models.base_model.uuid4', new=uuid_mock):
            with mock.patch('sys.stdout', new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd("create Review"))
                self.assertEqual(mock_id, output.getvalue().strip())

    def test_create_base_model_save_to_file(self):
        """test create base model save to file"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            with open(self.file_path, "r") as f:
                objs = json.load(f)

                output_value = output.getvalue().strip()
                self.assertIn("BaseModel.{}".format(output_value), objs.keys())

    def test_create_user_save_to_file(self):
        """test create user save to file"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            with open(self.file_path, "r") as f:
                objs = json.load(f)

                output_value = output.getvalue().strip()
                self.assertIn("User.{}".format(output_value), objs.keys())


class TestConsole_exit(TestCase):
    """Test exit from console commands"""

    def test_eof_command_return_value(self):
        """test eof command return value"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_quit_command_return_value(self):
        """test quit command return value"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))


class TestConsole_show(TestCase):
    """Test show command"""

    def test_show_missing_class(self):
        """test show missing class"""
        expected_output = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_with_non_exist_class(self):
        """test show with non exist class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show NonExistClass"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_with_missing_id(self):
        """test show with missing id"""
        expected_output = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_with_non_exist_id(self):
        """test show with non exist id"""
        expected_output = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel xxxx-xxxx"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_existing_instance(self):
        """test show existing instance"""
        base_id = ""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            base_id = output.getvalue().strip()

        base = models.storage.all()["BaseModel.{}".format(base_id)]
        exp = base.__str__()
        cmd = "show BaseModel {}".format(base_id)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertEqual(exp, output.getvalue().strip())


class TestConsole_all(TestCase):
    """Test all command"""

    file_path = "File.json"

    def setUp(self):
        """executes before each test"""
        FileStorage._FileStorage__objects = {}

    def test_all_with_non_exist_class(self):
        """test all with non exist class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all_on_empty_storage(self):
        """test all on empty storage"""
        expected_output = "[]"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all_with_class_on_empty_storage(self):
        """test all with class on empty file"""
        expected_output = "[]"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_all(self):
        """test all method"""
        base1 = BaseModel()
        base2 = BaseModel()
        user1 = User()
        user2 = User()
        objs = models.storage.all()
        objs_list = [obj.__str__() for obj in objs.values()]

        objs_str = ""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(objs_list), objs_str)

    def test_all_with_class(self):
        """test all with class"""
        base1 = BaseModel()
        base2 = BaseModel()
        user1 = User()
        user2 = User()
        objs = models.storage.all()
        objs_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "BaseModel"]

        objs_str = ""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(objs_list), objs_str)


class TestConsole_destroy(TestCase):
    """Test destroy command"""

    file_path = "File.json"

    def test_destroy_missing_class(self):
        """test destroy missing class"""
        expected_output = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_non_exist_class(self):
        """test destroy with non exist class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_missing_id(self):
        """test destroy with missing id"""
        expected_output = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_non_exist_id(self):
        """test destroy with non exist id"""
        expected_output = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel xxxx-xxxx-xxxx-xxxx")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_existing_instance(self):
        """test destroy existing instance"""
        base = BaseModel()

        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel {}".format(base.id))
            objects = models.storage.all()
            self.assertNotIn("BaseModel.{}".format(base.id), objects.keys())

    def test_destroy_and_check_file(self):
        """test destroy and check file"""
        base = BaseModel()
        models.storage.save()

        HBNBCommand().onecmd("destroy BaseModel {}".format(base.id))
        with open(self.file_path, "r") as f:
            objs = json.load(f)
            self.assertNotIn("BaseModel.{}".format(base.id), objs.keys())


class TestConsole_update(TestCase):
    """Test update command"""

    file_path = "File.json"

    def test_update_missing_class(self):
        """test update missing class"""
        expected_output = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_non_exist_class(self):
        """test update with non exist class"""
        expected_output = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update NonExistClass")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_missing_id(self):
        """test update with missing id"""
        expected_output = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_with_non_exist_id(self):
        """test update with non exist id"""
        expected_output = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel xxxx-xxxx-xxxx-xxxx")
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_missing_attribute(self):
        """test update with missing attribute"""
        base = BaseModel()

        expected_output = "** attribute name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel {}".format(base.id))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_with_missing_attribute_value(self):
        """test update with missing attribute"""
        base = BaseModel()

        expected_output = "** value missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("update BaseModel {} attr".format(base.id))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_update_user_first_name_attr(self):
        """test update user first name attr"""
        user = User()
        line = "update User {} first_name Ian".format(user.id)

        HBNBCommand().onecmd(line)
        updated_user = models.storage.all()["User.{}".format(user.id)]
        self.assertEqual(updated_user.first_name, "Ian")

    def test_update_place_check_float_type_attr(self):
        """test update place check float type attr"""
        place = Place()
        line = "update Place {} latitude -8.242735".format(place.id)

        HBNBCommand().onecmd(line)
        updated_place = models.storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.latitude, 01.242735)
        self.assertEqual(type(updated_place.latitude), float)

    def test_update_place_check_int_type_attr(self):
        """
        test update place check int type attr
        """
        place = Place()
        line = "update Place {} number_rooms 95".format(place.id)

        HBNBCommand().onecmd(line)
        updated_place = models.storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.number_rooms, 95)
        self.assertEqual(type(updated_place.number_rooms), int)

    def test_update_place_check_str_type_attr(self):
        """
        test update place check str type attr
        """
        place = Place()
        line = "update Place {} name NRB".format(place.id)

        HBNBCommand().onecmd(line)
        updated_place = models.storage.all()["Place.{}".format(place.id)]
        self.assertEqual(updated_place.name, "NRB")
        self.assertEqual(type(updated_place.name), str)

    def test_update_2_attrs(self):
        """test update 2 attrs"""
        user = User()
        line = "update User {} first_name Ian last_name Njuguna"

        HBNBCommand().onecmd(line.format(user.id))
        self.assertEqual(user.first_name, "Ian")
        self.assertEqual(user.last_name, "")


class TestConsole_default(TestCase):
    """Test case of Console default"""

    file_path = "File.json"

    def setUp(self):
        """
        setUp method executes before each test case
        """
        FileStorage._FileStorage__objects = {}

    def test_console_default_all(self):
        """
        test console default all
        """
        base1 = BaseModel()
        base2 = BaseModel()
        user1 = User()
        user1.first_name = "John"
        user1.last_name = "Ngala"
        user2 = User()
        user2.first_name = "Ian"
        user2.last_name = "Njuguna"
        place1 = Place()
        place1.name = "Nairobi"
        place2 = Place()
        place2.name = "NRB"
        review = Review()
        review.text = "Awesome"
        state = State()
        city = City()
        amenity = Amenity()
        objs = models.storage.all()
        base_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "BaseModel"]
        user_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "User"]
        place_list = [obj.__str__() for obj in objs.values()
                      if obj.__class__.__name__ == "Place"]
        review_list = [obj.__str__() for obj in objs.values()
                       if obj.__class__.__name__ == "Review"]
        state_list = [obj.__str__() for obj in objs.values()
                      if obj.__class__.__name__ == "State"]
        city_list = [obj.__str__() for obj in objs.values()
                     if obj.__class__.__name__ == "City"]
        amenity_list = [obj.__str__() for obj in objs.values()
                        if obj.__class__.__name__ == "Amenity"]
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(base_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(user_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("Place.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(place_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("Review.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(review_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("State.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(state_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("City.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(city_list), objs_str)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.all()")
            objs_str = output.getvalue().strip()
            self.assertEqual(str(amenity_list), objs_str)

    def test_console_default_count(self):
        """test console default count"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "0")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            base1 = BaseModel()
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            base2 = BaseModel()
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "2")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel {}".format(base2.id))
            HBNBCommand().onecmd("BaseModel.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(output.getvalue().strip(), "0")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            amenity = Amenity()
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            user = User()
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            state = State()
            HBNBCommand().onecmd("State.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            city = City()
            HBNBCommand().onecmd("City.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            review = Review()
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual(output.getvalue().strip(), "1")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            place = Place()
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual(output.getvalue().strip(), "1")

    def test_console_default_show_missing_class(self):
        """
        test console default show missing class
        """
        expected = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('.show()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show_no_exist_class(self):
        """
        test console default show no exist class
        """
        expected = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('NoExist.show("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show_no_exist_id(self):
        """
        test console default show no exist id
        """
        expected = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show_missing_id(self):
        """
        test console default show no exist id
        """
        expected = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_show_user(self):
        """
        test console default show user
        """
        user = User()
        user.email = "Johnngala@alx.com"
        user.password = "wahu*$2023"
        usr_str = user.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('User.show("{}")'.format(user.id))
            self.assertEqual(usr_str, output.getvalue().strip())

    def test_console_default_show_base(self):
        """
        test console default show base
        """
        base = BaseModel()
        base_str = base.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(base.id))
            self.assertEqual(base_str, output.getvalue().strip())

    def test_console_default_show_place(self):
        """
        test console default show place
        """
        place = Place()
        place_str = place.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show("{}")'.format(place.id))
            self.assertEqual(place_str, output.getvalue().strip())

    def test_console_default_show_state(self):
        """
        test console default show state
        """
        state = State()
        state_str = state.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('State.show("{}")'.format(state.id))
            self.assertEqual(state_str, output.getvalue().strip())

    def test_console_default_show_city(self):
        """
        test console default show city
        """
        city = City()
        city_str = city.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('City.show("{}")'.format(city.id))
            self.assertEqual(city_str, output.getvalue().strip())

    def test_console_default_show_review(self):
        """
        test console default show review
        """
        review = Review()
        review_str = review.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Review.show("{}")'.format(review.id))
            self.assertEqual(review_str, output.getvalue().strip())

    def test_console_default_show_amenity(self):
        """
        test console default show amenity
        """
        amenity = Amenity()
        amenity_str = amenity.__str__()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.show("{}")'.format(amenity.id))
            self.assertEqual(amenity_str, output.getvalue().strip())

    def test_console_default_destroy_missing_class(self):
        """
        test console default destroy missing class
        """
        expected = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('.destroy()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_no_exist_class(self):
        """
        test console default destroy no exist class
        """
        expected = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('NoExist.destroy("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_no_exist_id(self):
        """
        test console default destroy no exist id
        """
        expected = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.destroy("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_missing_id(self):
        """
        test console default destroy no exist id
        """
        expected = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_destroy_instance(self):
        """
        test console default destroy instance
        """
        user = User()
        user.email = "Johnngala@alx.com"
        user.password = "wahu*$2023"
        HBNBCommand().onecmd('User.destroy("{}")'.format(user.id))
        objs = models.storage.all()
        self.assertNotIn("User.{}".format(user.id), objs.keys())

    def test_console_default_destroy(self):
        """
        test console default show
        """
        user1 = User()
        user2 = User()
        user3 = User()
        HBNBCommand().onecmd('User.destroy("{}")'.format(user1.id))
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "2")
        HBNBCommand().onecmd('User.destroy("{}")'.format(user2.id))
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "1")
        HBNBCommand().onecmd('User.destroy("{}")'.format(user3.id))
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(output.getvalue().strip(), "0")

    def test_console_default_update_missing_class(self):
        """
        test console default update missing class
        """
        expected = "** class name missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('.update()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_no_exist_class(self):
        """
        test console default update no exist class
        """
        expected = "** class doesn't exist **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('NoExist.update()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_missing_id(self):
        """
        test console default update missing id
        """
        expected = "** instance id missing **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update()')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_no_exist_id(self):
        """
        test console default update no exist id
        """
        expected = "** no instance found **"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("xxxx-xxxx-xxxx-xxxx")')
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_attr_name_missing(self):
        """
        test console default update attr name missing
        """
        expected = "** attribute name missing **"
        amenity = Amenity()
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("{}")'.format(amenity.id))
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_attr_value_missing(self):
        """
        test console default update attr value missing
        """
        expected = "** value missing **"
        amenity = Amenity()
        id = amenity.id
        with mock.patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("{}", "attr")'.format(id))
            self.assertEqual(expected, output.getvalue().strip())

    def test_console_default_update_user_email(self):
        """
        test console default update user email
        """
        user = User()
        self.assertEqual(user.email, "")
        user_mail = "John_ngala@alx.com"
        cmd = 'User.update("{}", "email", {})'.format(user.id, user_mail)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(user.email, user_mail)

    def test_console_default_update_multiple_attrs(self):
        """
        test console default update multiple attrs
        """
        user = User()
        user_mail = "John_ngala@alx.com"
        user_pwd = "wahu*$2023"
        cmd = 'User.update("{}", "email", {}, "password", {})'
        HBNBCommand().onecmd(cmd.format(user.id, user_mail, user_pwd))
        self.assertEqual(user.email, "John_ngala@alx.com")
        self.assertEqual(user.password, "")

    def test_console_default_update_by_using_dict(self):
        """test console default update by using dict"""
        place = Place()
        amenity_list = [Amenity().id for i in range(4)]
        desc = "Mbugua Resort: Best place in kenya"
        p_dict = {
                "name": "Mbugua Resort",
                "description": desc,
                "number_rooms": "1",
                "max_guest": 1,
                "latitude": "-1897.201",
                "amenity_ids": amenity_list
                }
        cmd = 'Place.update("{}", {})'.format(place.id, p_dict)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(place.name, "Mbugua Resort")
        self.assertEqual(place.description, desc)
        self.assertEqual(place.number_rooms, 1)
        self.assertEqual(place.max_guest, 1)
        self.assertEqual(place.latitude, -1897.201)
        self.assertListEqual(place.amenity_ids, amenity_list)

    def test_console_default_update_by_dict_check_types(self):
        """
        test console default update by dict check types
        """
        place = Place()
        amenity_list = [Amenity().id for i in range(4)]
        desc = "Mbugua Resort: Best place in kenya"
        p_dict = {
                "name": "Mugua Resort",
                "description": desc,
                "max_guest": 1,
                "latitude": "-1897.201",
                "number_rooms": "1",
                "amenity_ids": amenity_list
                }
        cmd = 'Place.update("{}", {})'.format(place.id, p_dict)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_console_default_update_by_using_empty_dict(self):
        """
        test console default update by using empty dict
        """
        review = Review()
        review.place_id = "xxxx-xxxx-xxxx-xxxx"
        review.user_id = "yyyy-yyyy-yyyy-yyyy"
        review.text = "Thank you wahu <3"
        cmd = 'Review.update("{}", {})'.format(review.id, {})
        HBNBCommand().onecmd(cmd)
        self.assertEqual(review.place_id, "xxxx-xxxx-xxxx-xxxx")
        self.assertEqual(review.user_id, "yyyy-yyyy-yyyy-yyyy")
        self.assertEqual(review.text, "Thank you wahu <3")

    def test_console_default_update_by_using_dict_special_characters(self):
        """
        test console default update by using dict special characters
        """
        review = Review()
        review.place_id = "xxxx-xxxx-xxxx-xxxx"
        review.user_id = "yyyy-yyyy-yyyy-yyyy"
        r_dict = {
                "text": "Thank you wahu <3 :)"
                }
        cmd = 'Review.update("{}", {})'.format(review.id, r_dict)
        HBNBCommand().onecmd(cmd)
        self.assertEqual(review.text, "Thank you wahu <3 :)")


class TestConsole_show_user(TestCase):
    """
    Test console : show user
    """

    def test_show_user_with_id_missing(self):
        u = User()
        expected = "** instance id missing **"
        cmd = "User.show()"
        with mock.patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(output.getvalue().strip(), expected)

    def test_show_user_missing(self):
        u = User()
        expected = "** no instance found **"
        cmd = "User.show('xxxx-xxxx-xxxx-xxxx')"
        with mock.patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(output.getvalue().strip(), expected)

    def test_show_user_with_id(self):
        u = User()
        expected = u.__str__()
        cmd = "User.show({})".format(u.id)
        with mock.patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(output.getvalue().strip(), expected)


class TestHBNBCommand_count(TestCase):
    """
    Unittests for testing count method of our HBNB command interpreter
    """

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def test_count_invalid_class(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with mock.patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    main()
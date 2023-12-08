#!/usr/bin/python3
from models.base_model import BaseModel
from unittest import TestCase, mock, main
import datetime
import models
from io import StringIO

class TestBaseModel(TestCase):

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
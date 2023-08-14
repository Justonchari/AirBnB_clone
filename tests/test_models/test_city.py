#!/usr/bin/python3
<<<<<<< HEAD

"""Unit tests for the City class."""

from models.city import City
import unittest
from datetime import datetime
import time
import os
from models import storage
from models.base_model import BaseModel
import re
import json
from models.engine.file_storage import FileStorage

class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
=======
import unittest
from datetime import datetime

from models import City, storage, BaseModel


class TestCityClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.city = City()

    def test_city_initialization(self):
        self.assertIsInstance(self.city.id, str)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsNotNone(self.city.updated_at)
        self.assertIsInstance(self.city.updated_at, datetime)

        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

        self.assertIsInstance(self.city, BaseModel)
        self.assertEqual(type(self.city), City)

    def test_city_str(self):
        self.assertEqual(
            self.city.__str__(),
            f"[{self.city.__class__.__name__}] \
({self.city.id}) {self.city.__dict__}",
        )

    def test_city_save(self):
        prev_updated_at = self.city.updated_at
        self.city.save()

        self.assertNotEqual(self.city.updated_at, prev_updated_at)
        self.assertTrue(self.city.updated_at > prev_updated_at)

    def test_city_to_dict(self):
        bm_dict = self.city.to_dict()

        self.assertIsInstance(bm_dict, dict)
        self.assertTrue(all([isinstance(v, str) for k, v in bm_dict.items()]))
        self.assertEqual(
                bm_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(
                bm_dict["updated_at"], self.city.updated_at.isoformat())

    def test_city_from_dict(self):
        bm_dict = self.city.to_dict()
        dummy_city = City(**bm_dict)
        self.assertEqual(bm_dict, dummy_city.to_dict())
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c

#!/usr/bin/python3
<<<<<<< HEAD
"""Unit tests for the Amenity class."""

from models.amenity import Amenity
import unittest
from datetime import datetime
import time
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit Test Cases for the Amenity class."""

    def setUp(self):
        """Set up for the test methods."""
        pass

    def tearDown(self):
        """Tear down after the test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset the FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test the instantiation of the Amenity class."""

        amenity_instance = Amenity()
        self.assertEqual(str(type(amenity_instance)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of the Amenity class."""
        attributes = storage.attributes()["Amenity"]
        amenity_instance = Amenity()
        for attribute, expected_type in attributes.items():
            self.assertTrue(hasattr(amenity_instance, attribute))
            self.assertEqual(type(getattr(amenity_instance, attribute, None)), expected_type)

if __name__ == "__main__":
    unittest.main()

=======
import unittest
from datetime import datetime

from models import Amenity, storage, BaseModel


class TestAmenityClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()

    def test_amenity_initialization(self):
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsNotNone(self.amenity.updated_at)
        self.assertIsInstance(self.amenity.updated_at, datetime)

        self.assertEqual(self.amenity.name, "")

        self.assertIsInstance(self.amenity, BaseModel)
        self.assertEqual(type(self.amenity), Amenity)

    def test_amenity_str(self):
        self.assertEqual(
            self.amenity.__str__(),
            f"[{self.amenity.__class__.__name__}] \
({self.amenity.id}) {self.amenity.__dict__}",
        )

    def test_amenity_save(self):
        prev_updated_at = self.amenity.updated_at
        self.amenity.save()

        self.assertNotEqual(self.amenity.updated_at, prev_updated_at)
        self.assertTrue(self.amenity.updated_at > prev_updated_at)

    def test_amenity_to_dict(self):
        bm_dict = self.amenity.to_dict()

        self.assertIsInstance(bm_dict, dict)
        self.assertTrue(all([isinstance(v, str) for k, v in bm_dict.items()]))
        self.assertEqual(
                bm_dict["created_at"], self.amenity.created_at.isoformat())
        self.assertEqual(
                bm_dict["updated_at"], self.amenity.updated_at.isoformat())

    def test_amenity_from_dict(self):
        bm_dict = self.amenity.to_dict()
        dummy_amenity = Amenity(**bm_dict)
        self.assertEqual(bm_dict, dummy_amenity.to_dict())
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c

#!/usr/bin/python3
<<<<<<< HEAD
"""Unit tests for the Place class."""
from models.place import Place
from datetime import datetime
import time
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage

class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

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
        """Tests instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
=======
import unittest
from datetime import datetime

from models import Place, storage, BaseModel


class TestPlaceClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.place = Place()

    def test_place_initialization(self):
        self.assertIsInstance(self.place.id, str)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsNotNone(self.place.updated_at)
        self.assertIsInstance(self.place.updated_at, datetime)

        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

        self.assertIsInstance(self.place, BaseModel)
        self.assertEqual(type(self.place), Place)

    def test_place_str(self):
        self.assertEqual(
            self.place.__str__(),
            f"[{self.place.__class__.__name__}] \
({self.place.id}) {self.place.__dict__}",
        )

    def test_place_save(self):
        prev_updated_at = self.place.updated_at
        self.place.save()

        self.assertNotEqual(self.place.updated_at, prev_updated_at)
        self.assertTrue(self.place.updated_at > prev_updated_at)

    def test_place_to_dict(self):
        bm_dict = self.place.to_dict()

        self.assertIsInstance(bm_dict, dict)
        self.assertTrue(all([isinstance(v, str) for k, v in bm_dict.items()]))
        self.assertEqual(
                bm_dict["created_at"], self.place.created_at.isoformat())
        self.assertEqual(
                bm_dict["updated_at"], self.place.updated_at.isoformat())

    def test_place_from_dict(self):
        bm_dict = self.place.to_dict()
        dummy_place = Place(**bm_dict)
        self.assertEqual(bm_dict, dummy_place.to_dict())


# if __name__ == "__main__":
# Do stuff
>>>>>>> bf376159e761ccdb4bc604d09db3cf8e555b511c

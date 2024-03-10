#!/usr/bin/python3
"""
Module containing unit tests for the FileStorage class.
"""

import os
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class TestFileStorageInstantiation(unittest.TestCase):
    """
    Unit tests for instantiating the FileStorage class.
    """

    def test_instantiation_no_args(self):
        """
        Test instantiating FileStorage class without arguments.
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_arg(self):
        """
        Test instantiating FileStorage class with argument.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        """
        Test if file_path attribute is a private string.
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        """
        Test if objects attribute is a private dictionary.
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """
        Test if storage initializes correctly.
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """
    Unit tests for testing methods of the FileStorage class.
    """

    def setUp(self):
        """
        Set up method for test cases.
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down method for test cases.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        Test all method of FileStorage class.
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """
        Test all method of FileStorage class with argument.
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    # Additional test methods for new, save, reload, etc.

    def test_reload_with_arg(self):
        """
        Test reload method of FileStorage class with argument.
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()


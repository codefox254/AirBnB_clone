#!/usr/bin/python3
"""
Module containing unit tests for the Amenity class.
"""

import os
import unittest
from datetime import datetime
from time import sleep

from models.amenity import Amenity
import models


class TestAmenityInstantiation(unittest.TestCase):
    """
    Unit tests for the instantiation of the Amenity class.
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

    def test_no_args_instantiates(self):
        """
        Test instantiating Amenity class without arguments.
        """
        self.assertEqual(Amenity, type(Amenity()))

    # Additional test methods for instantiating Amenity class


class TestAmenitySave(unittest.TestCase):
    """
    Unit tests for the save method of the Amenity class.
    """

    # Test methods for save method


class TestAmenityToDict(unittest.TestCase):
    """
    Unit tests for the to_dict method of the Amenity class.
    """

    # Test methods for to_dict method


if __name__ == "__main__":
    unittest.main()


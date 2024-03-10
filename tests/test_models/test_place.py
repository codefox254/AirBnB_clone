#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for verifying the instantiation of the Place class.
    """

    """
    Setting up the environment for testing.
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")  # Renaming file for testing
        except FileNotFoundError:
            pass

    """
    Cleaning up the environment after testing.
    """
    def tearDown(self):
        try:
            os.remove("file.json")  # Removing the temporary file
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")  # Renaming back to the original
        except FileNotFoundError:
            pass

    """
    Verifying that instantiation of Place class works without arguments.
    """
    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    """
    Verifying that a new instance is stored in the objects dictionary.
    """
    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    """
    Verifying that the ID attribute is of type str.
    """
    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    """
    Verifying that the created_at attribute is of type datetime.
    """
    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    """
    Verifying that the updated_at attribute is of type datetime.
    """
    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    """
    Verifying that the city_id attribute is of type str and is a class attribute.
    """
    def test_city_id_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(my_place))
        self.assertNotIn("city_id", my_place.__dict__)

    """
    Verifying that the user_id attribute is of type str and is a class attribute.
    """
    def test_user_id_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(my_place))
        self.assertNotIn("user_id", my_place.__dict__)

    """
    Verifying that the name attribute is of type str and is a class attribute.
    """
    def test_name_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(my_place))
        self.assertNotIn("name", my_place.__dict__)

    """
    Verifying that the description attribute is of type str and is a class attribute.
    """
    def test_description_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(my_place))
        self.assertNotIn("description", my_place.__dict__)

    """
    Verifying that the number_rooms attribute is of type int and is a class attribute.
    """
    def test_number_rooms_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(my_place))
        self.assertNotIn("number_rooms", my_place.__dict__)

    """
    Verifying that the number_bathrooms attribute is of type int and is a class attribute.
    """
    def test_number_bathrooms_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(my_place))
        self.assertNotIn("number_bathrooms", my_place.__dict__)

    """
    Verifying that the max_guest attribute is of type int and is a class attribute.
    """
    def test_max_guest_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(my_place))
        self.assertNotIn("max_guest", my_place.__dict__)

    """
    Verifying that the price_by_night attribute is of type int and is a class attribute.
    """
    def test_price_by_night_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(my_place))
        self.assertNotIn("price_by_night", my_place.__dict__)

    """
    Verifying that the latitude attribute is of type float and is a class attribute.
    """
    def test_latitude_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(my_place))
        self.assertNotIn("latitude", my_place.__dict__)

    """
    Verifying that the longitude attribute is of type float and is a class attribute.
    """
    def test_longitude_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(my_place))
        self.assertNotIn("longitude", my_place.__dict__)

    """
    Verifying that the amenity_ids attribute is of type list and is a class attribute.
    """
    def test_amenity_ids_is_public_class_attribute(self):
        my_place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(my_place))
        self.assertNotIn("amenity_ids", my_place.__dict__)

    """
    Verifying that two places have unique IDs.
    """
    def test_two_places_unique_ids(self):
        my_place1 = Place()
        my_place2 = Place()
        self.assertNotEqual(my_place1.id, my_place2.id)  # Verifying unique IDs

    """
    Verifying that the created_at attribute is different for two places.
    """
    def test_two_places_different_created_at(self):
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.created_at, my_place2.created_at)  # Verifying different created_at

    """
    Verifying that the updated_at attribute is different for two places.
    """
    def test_two_places_different_updated_at(self):
        my_place1 = Place()
        sleep(0.05)
        my_place2 = Place()
        self.assertLess(my_place1.updated_at, my_place2.updated_at)  # Verifying different updated_at

    """
    Verifying the string representation of the Place object.
    """
    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        my_place = Place()
        my_place.id = "987654"  # Updating ID
        my_place.created_at = my_place.updated_at = my_date
        my_place_str = my_place.__str__()
        self.assertIn("[Place] (987654)", my_place_str)  # Verifying string representation
        self.assertIn("'id': '987654'", my_place_str)  # Verifying ID in string representation
        self.assertIn("'created_at': " + my_date_repr, my_place_str)  # Verifying created_at in string representation
        self.assertIn("'updated_at': " + my_date_repr, my_place_str)  # Verifying updated_at in string representation

    """
    Verifying that unused args are not present in the __dict__ attribute.
    """
    def test_args_unused(self):
        my_place = Place(None)
        self.assertNotIn(None, my_place.__dict__.values())  # Verifying unused args not in __dict__

    """
    Verifying instantiation with keyword arguments.
    """
    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        my_place = Place(id="987", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(my_place.id, "987")
        self.assertEqual(my_place.created_at, my_date)
        self.assertEqual(my_place.updated_at, my_date)

    """
    Verifying instantiation with None keyword arguments raises TypeError.
    """
    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests for verifying the save method of the Place class.
    """

    """
    Setting up the environment for testing.
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")  # Renaming file for testing
        except FileNotFoundError:
            pass

    """
    Cleaning up the environment after testing.
    """
    def tearDown(self):
        try:
            os.remove("file.json")  # Removing the temporary file
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")  # Renaming back to the original
        except FileNotFoundError:
            pass

    """
    Verifying that calling save method updates the updated_at attribute.
    """
    def test_one_save(self):
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        self.assertLess(first_updated_at, my_place.updated_at)

    """
    Verifying that calling save method multiple times updates the updated_at attribute.
    """
    def test_two_saves(self):
        my_place = Place()
        sleep(0.05)
        first_updated_at = my_place.updated_at
        my_place.save()
        second_updated_at = my_place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_place.save()
        self.assertLess(second_updated_at, my_place.updated_at)

    """
    Verifying that calling save method with an argument raises TypeError.
    """
    def test_save_with_arg(self):
        my_place = Place()
        with self.assertRaises(TypeError):
            my_place.save(None)

    """
    Verifying that calling save method updates the file content.
    """
    def test_save_updates_file(self):
        my_place = Place()
        my_place.save()
        my_place_id = "Place." + my_place.id
        with open("file.json", "r") as f:
            self.assertIn(my_place_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for verifying the to_dict method of the Place class.
    """

    """
    Setting up the environment for testing.
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")  # Renaming file for testing
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()


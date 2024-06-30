#!/usr/bin/python3
"""Test Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0  # Reset the private class attribute before each test

    def test_id_provided(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)

    def test_id_not_provided(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_mixed_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(100)
        self.assertEqual(b2.id, 100)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_private_class_attribute(self):
        self.assertEqual(Base._Base__nb_objects, 0)
        b1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)
        b3 = Base(50)
        self.assertEqual(Base._Base__nb_objects, 2)
        b4 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)   

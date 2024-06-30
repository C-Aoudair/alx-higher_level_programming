#!/usr/bin/python3
""" Test Square class """

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square1 = Square(5)
        self.square2 = Square(3, 1, 1, 99)

    def test_init(self):
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.width, 5)
        self.assertEqual(self.square1.height, 5)
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square1.y, 0)
        self.assertIsNotNone(self.square1.id)

        self.assertEqual(self.square2.size, 3)
        self.assertEqual(self.square2.width, 3)
        self.assertEqual(self.square2.height, 3)
        self.assertEqual(self.square2.x, 1)
        self.assertEqual(self.square2.y, 1)
        self.assertEqual(self.square2.id, 99)

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)

    def test_area(self):
        self.assertEqual(self.square1.area(), 25)
        self.assertEqual(self.square2.area(), 9)

    def test_str(self):
        self.assertEqual(str(self.square1), "[Square] ({}) 0/0 - 5".format(self.square1.id))
        self.assertEqual(str(self.square2), "[Square] (99) 1/1 - 3")

    def test_update_args(self):
        self.square1.update(5, 7, 8, 9)
        self.assertEqual(self.square1.id, 5)
        self.assertEqual(self.square1.size, 7)
        self.assertEqual(self.square1.width, 7)
        self.assertEqual(self.square1.height, 7)
        self.assertEqual(self.square1.x, 8)
        self.assertEqual(self.square1.y, 9)

    def test_update_kwargs(self):
        self.square1.update(id=10, size=12, x=10, y=10)
        self.assertEqual(self.square1.id, 10)
        self.assertEqual(self.square1.size, 12)
        self.assertEqual(self.square1.width, 12)
        self.assertEqual(self.square1.height, 12)
        self.assertEqual(self.square1.x, 10)
        self.assertEqual(self.square1.y, 10)

    def test_to_dictionary(self):
        square_dict = self.square1.to_dictionary()
        expected_dict = {
            'id': self.square1.id,
            'size': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(square_dict, expected_dict)

        square_dict = self.square2.to_dictionary()
        expected_dict = {
            'id': 99,
            'size': 3,
            'x': 1,
            'y': 1
        }
        self.assertEqual(square_dict, expected_dict)
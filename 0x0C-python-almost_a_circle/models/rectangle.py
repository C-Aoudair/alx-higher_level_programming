#!/usr/bin/python3
"""Defines Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(10, 20)
        self.rect2 = Rectangle(2, 4, 1, 1, 99)

    def test_init(self):
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 20)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)
        self.assertIsNotNone(self.rect1.id)

        self.assertEqual(self.rect2.width, 2)
        self.assertEqual(self.rect2.height, 4)
        self.assertEqual(self.rect2.x, 1)
        self.assertEqual(self.rect2.y, 1)
        self.assertEqual(self.rect2.id, 99)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(10, -20)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "0")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 0, "0")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 0, -1)

    def test_area(self):
        self.assertEqual(self.rect1.area(), 200)
        self.assertEqual(self.rect2.area(), 8)

    def test_display(self):
        # This method prints to stdout, so capturing output is necessary for testing.
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), ("#" * 10 + "\n") * 20)

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.rect2.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n" + " " * 1 + "#" * 2 + "\n" + " " * 1 + "#" * 2 + "\n" + " " * 1 + "#" * 2 + "\n" + " " * 1 + "#" * 2 + "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[Rectangle] ({}) 0/0 - 10/20".format(self.rect1.id))
        self.assertEqual(str(self.rect2), "[Rectangle] (99) 1/1 - 2/4")

    def test_update_args(self):
        self.rect1.update(5, 15, 25, 5, 5)
        self.assertEqual(self.rect1.id, 5)
        self.assertEqual(self.rect1.width, 15)
        self.assertEqual(self.rect1.height, 25)
        self.assertEqual(self.rect1.x, 5)
        self.assertEqual(self.rect1.y, 5)

    def test_update_kwargs(self):
        self.rect1.update(id=10, width=20, height=30, x=10, y=10)
        self.assertEqual(self.rect1.id, 10)
        self.assertEqual(self.rect1.width, 20)
        self.assertEqual(self.rect1.height, 30)
        self.assertEqual(self.rect1.x, 10)
        self.assertEqual(self.rect1.y, 10)

    def test_to_dictionary(self):
        rect_dict = self.rect1.to_dictionary()
        expected_dict = {
            'id': self.rect1.id,
            'width': 10,
            'height': 20,
            'x': 0,
            'y': 0
        }
        self.assertEqual(rect_dict, expected_dict)

        rect_dict = self.rect2.to_dictionary()
        expected_dict = {
            'id': 99,
            'width': 2,
            'height': 4,
            'x': 1,
            'y': 1
        }
        self.assertEqual(rect_dict, expected_dict)

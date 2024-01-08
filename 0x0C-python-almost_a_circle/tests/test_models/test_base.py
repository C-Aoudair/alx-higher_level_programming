#!/usr/bin/python3
"""Test Base class."""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_1(self):

        b1 = Base()
        self.assertTrue(b1.id == 1)

        b2 = Base(12)
        self.assertTrue(b2.id == 12)

        b3 = Base()
        self.assertTrue(b3.id == 2)

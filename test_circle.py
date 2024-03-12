"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math

class Add_area_test(unittest.TestCase):

    def test_add_area_two_positive(self):
        circle1 = Circle(10)
        circle2 = Circle(10)
        expected_area = (math.pi*10*10)*2

        circle3 = circle1.add_area(circle2)
        self.assertEqual(expected_area, circle3.get_area())

        expected_radius = math.hypot(10, 10)
        self.assertEqual(expected_radius, circle3.get_radius())

    def test_add_area_radius_0(self):
        circle1 = Circle(0)
        circle2 = Circle(0)
        expected_area = 0
        circle3 = circle1.add_area(circle2)
        self.assertEqual(expected_area, circle3.get_area())

        expected_radius = math.hypot(0, 0)
        self.assertEqual(expected_radius, circle3.get_radius())

        circle1 = Circle(10)
        circle2 = Circle(0)
        expected_area = math.pi*10*10
        circle3 = circle1.add_area(circle2)
        self.assertEqual(expected_area, circle3.get_area())

        expected_radius = math.hypot(10, 0)
        self.assertEqual(expected_radius, circle3.get_radius())

    def test_creating_negative_circle(self):
        with self.assertRaises(ValueError):
            circle1 = Circle(-1)

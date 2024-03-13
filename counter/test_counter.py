"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest

class Singleton_Test(unittest.TestCase):

    def test_same_instance(self):
        """
        Try to make two instance of the class and compare the instance
        compare the values
        compare the id
        """

        c1 = Counter()
        c2 = Counter()
        self.assertEqual(c1, c2)

        value1 = c1.increment()
        value2 = c2.count

        self.assertEqual(value1, value2)

        self.assertEqual(id(c1), id(c2))

    def test_not_reset_to_0(self):
        """
        Incrementing the instance and in calling it again and then
        compare the values to see if value reset
        """

        c1 = Counter()
        value1 = c1.increment()  # Should be 1

        c1 = Counter()
        value2 = c1.count  # Should be 1

        # If it's reset the value2 should be 0

        self.assertEqual(value1, value2)

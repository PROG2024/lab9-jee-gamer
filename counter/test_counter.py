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
        Try to make two instance of the class and compare it
        """

        c1 = Counter()
        c2 = Counter()
        self.assertEqual(c1, c2)

        value1 = c1.increment() + 1
        value2 = c2.increment()

        self.assertEqual(value1, value2)

    def test_not_reset_to_0(self):
        """
        Incrementing the instance and in calling it again and then
        Incrementing it again then compare the values to see if value reset
        """

        c1 = Counter()
        value1 = c1.increment()

        c1 = Counter()
        value2 = c1.increment()

        self.assertEqual(value1, value2-1)

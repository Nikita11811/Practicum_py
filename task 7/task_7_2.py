import unittest
import random
import math

a = random.randint(1, 100)
b = math.log2(a)**2


class TestMethod(unittest.TestCase):

    def test_test(self):
        for i in range(1, 100):
            with self.subTest(i=i):
                self.assertGreater(a, b)


if __name__ == '__main__':
    unittest.main()

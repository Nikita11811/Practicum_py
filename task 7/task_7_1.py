import unittest
import random
import math


aaa = random.randint(1, 10)
l1 = []
for i in range(57, 90):
    l1.append(i)


def Calc(a, b):
    c = random.randint(a, b)
    d = math.sqrt(a)
    if c > d:
        return True
    elif c == d:
        return False


class TestMethods(unittest.TestCase):

    def test_true(self):
        self.assertTrue(Calc(10, 100))

    def test_false(self):
        self.assertFalse(Calc(1, 1))

    def test_in(self):
        self.assertIn(i, l1)

    def test_not_in(self):
        self.assertNotIn(aaa, l1)

    def test_greater(self):
        self.assertGreater(i, aaa)

    def test_less(self):
        self.assertLess(math.sqrt(aaa), aaa)

    def test_count_equal(self):
        self.assertCountEqual(l1, l1.__reversed__())


if __name__ == '__main__':
    unittest.main()

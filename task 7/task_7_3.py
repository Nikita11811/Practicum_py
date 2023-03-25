import unittest
import os
import time


def CreateFolder(a):
    os.mkdir(a)
    with open(r'C:\Users\test\Desktop\STUDY\1\1.txt', "w") as text:
        text.write(time.strftime('%H-%M-%S_%d-%m-%Y'))


class TestMethod3(unittest.TestCase):

    def setUp(self):
        self.create = CreateFolder(r'C:\Users\test\Desktop\STUDY\1')

    def test_file(self):
        self.assertIsNotNone(r'C:\Users\test\Desktop\STUDY\1\1.txt')

    def tearDown(self):
       os.remove(r'C:\Users\test\Desktop\STUDY\1\1.txt')
       os.rmdir(r'C:\Users\test\Desktop\STUDY\1')


if __name__ == '__main__':
    unittest.main()


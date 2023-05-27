import unittest
import os
import time


text = time.strftime('%H-%M-%S_%d-%m-%Y')


def create_folder(a):
    os.mkdir(a)
    with open(r'C:\Users\Пользователь\Desktop\Новая папка\STUDY\1\1.txt', "w") as f:
        f.write(text)


class TestMethod3(unittest.TestCase):

    def setUp(self):
        self.create = create_folder(r'C:\Users\Пользователь\Desktop\Новая папка\STUDY\1')

    def test_file(self):
        with open ('C:/Users/Пользователь/Desktop/Новая папка/STUDY/1/1.txt') as f:
            self.assertEqual(text, f.read())

    def tearDown(self):
       os.remove(r'C:\Users\Пользователь\Desktop\Новая папка\STUDY\1\1.txt')
       os.rmdir(r'C:\Users\Пользователь\Desktop\Новая папка\STUDY\1')


if __name__ == '__main__':
    unittest.main()

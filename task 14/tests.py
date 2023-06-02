from task14 import TFIDF
import unittest


class TestTFIDF(unittest.TestCase):

    def setUp(self):
        self.object = TFIDF(['1.txt', '2.txt'])
        self.tfidf = self.object.count_tfidf('2.txt')
        self.tfidfs = [('смогут', 0.0), ('ли', 0.046209812037329684), ('люди', 0.046209812037329684),
                       ('научиться', 0.046209812037329684), ('разговаривать', 0.046209812037329684), ('на', 0.0),
                       ('язык', 0.0), ('обезьяна', 0.046209812037329684), ("бонобо", 0.046209812037329684)]

    def test_tfidf(self):
        for i in range(len(self.tfidfs)):
            with self.subTest(i=i):
                self.assertAlmostEqual(self.tfidfs[i][1], self.tfidf[i][1])

    def test_texts_upload(self):
        self.assertIsNotNone(self.object.get_texts())


if __name__ == '__main__':
    unittest.main()

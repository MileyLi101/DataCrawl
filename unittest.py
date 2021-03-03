import unittest


class myTest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 2

    def test_add(self):
        self.assertEqual(self.a + self.b, 12)

    def test_mul(self):
        self.assertNotEqual(self.a * self.b, 15)
        self.assertEqual(self.a * self.b, 20)

if __name__ == '__main__':
    unittest.main()
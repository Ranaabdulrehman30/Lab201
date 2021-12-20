import unittest
from lab8task2 import check


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_string(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_upper(self):
        self.assertEqual('demon'.upper(), 'DEMON')

    def test_strip(self):
        s = 'AlphaOmega'
        self.assertEqual(s.strip('Alpha'), 'Omega', "Test failed")

    def test_split(self):
        x = "Hello World"
        self.assertEqual(x.split(), ["Hello", "World"])
        with self.assertRaises(TypeError):
            x.split(2)




if __name__ == '__main__':
    unittest.main()
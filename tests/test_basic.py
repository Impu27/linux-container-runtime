import unittest

class TestBasic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_string(self):
        self.assertEqual("gpu", "gpu")

if __name__ == "__main__":
    unittest.main()

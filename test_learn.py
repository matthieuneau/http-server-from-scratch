import unittest


# Example function to test
def add(a, b):
    return a + b


class TestBasicFunctionality(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 = 5


if __name__ == "__main__":
    unittest.main()

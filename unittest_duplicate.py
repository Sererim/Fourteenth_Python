import unittest
from find_all_duplicates import duplicate

class TestCaseDuplicate(unittest.TestCase):

    def setUp(self) -> None:
        self.lst_1 = [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10]
        self.lst_2 = list(map(lambda x: -x, self.lst_1))

    def test_unique(self) -> None:
        self.assertEqual([3, 4, 5, 6, 8, 9], duplicate(self.lst_1))
        self.assertEqual([-3, -4, -5, -6, -8, -9], duplicate(self.lst_2))

    def test_duplicate(self) -> None:
        self.assertEqual([1, 2, 7, 10], duplicate(self.lst_1, unique=2))
        self.assertEqual([-1, -2, -7, -10], duplicate(self.lst_2, unique=2))


if __name__ == "__main__":
    unittest.main(verbosity=2)

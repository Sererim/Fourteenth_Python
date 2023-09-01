import doctest
import unittest
import pytest

import transpose_matrix


class TestTranspose(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matrix_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    def testWorkings(self) -> None:
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], transpose_matrix.transpose(self.matrix_1))
        self.assertEqual([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]], transpose_matrix.transpose(self.matrix_2))


if __name__ == '__main__':
    unittest.main(verbosity=2)

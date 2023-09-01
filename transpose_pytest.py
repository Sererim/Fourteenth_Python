import pytest

from transpose_matrix import transpose


def test_simple():
    assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_simple_other():
    assert transpose([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


def test_empty_matrix():
    with pytest.raises(TypeError, match=r'Error!\nMatrix must be a list type'):
        transpose((1, 2))


def test_value_error():
    with pytest.raises(ValueError, match=r'Error!\nMatrix must have elements in it.'):
        transpose([])


def test_len_is_zero():
    with pytest.raises(ValueError, match=r'Error!\nMatrix must have lists in it.'):
        transpose([[], [], []])


if __name__ == "__main__":
    pytest.main(['-v'])

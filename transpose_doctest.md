Function that takes matrix of type list of lists of objects and returns transposed matrix.
===

Test
---

    >>> from transpose_matrix import transpose
    
Let's see if function works correctly.

    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    True
    >>> transpose([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    True

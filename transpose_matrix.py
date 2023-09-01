# Напишите функцию для транспонирования матрицы
def transpose(matrix) -> list:
    """
    Function that takes matrix of type list of lists of objects and returns transposed matrix.
    :param matrix: is a list of lists of objects
    :return: transposed matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("Error!\nMatrix must be a list type")
    elif len(matrix) == 0:
        raise ValueError("Error!\nMatrix must have elements in it.")
    elif len(matrix[0]) == 0:
        raise ValueError("Error!\nMatrix must have lists in it.")

    t_matrix = [[matrix[row][col] for row in range(len(matrix))]
                for col in range(len(matrix[0]))]
    return t_matrix


if __name__ == "__main__":
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(matrix_1))
    matrix_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(transpose(matrix_2))

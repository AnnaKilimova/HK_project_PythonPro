'''Завдання 8. Тестування з використанням doctest та покриття складних сценаріїв (опціонально)
Додайте документацію з прикладами використання більш складних функцій, які включають роботу з матрицями.
Реалізуйте функції для роботи з матрицями:
• matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]: множення двох матриць.
• transpose_matrix(matrix: List[List[int]]) -> List[List[int]]: транспонування матриці.
Додайте doctest для кожної функції:'''

from typing import List


def matrix_multiply(
    matrix1: List[List[int]], matrix2: List[List[int]]
) -> List[List[int]]:
    """
    Multiplication of two matrices.
    :param matrix1: list of lists of integers (two-dimensional matrix).
    :param matrix2: list of lists of integers (two-dimensional matrix).
    :return: matrix (list of lists)

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    >>> matrix_multiply([[1, 0, 2], [-1, 3, 1]], [[3, 1], [2, 1], [1, 0]])
    [[5, 1], [4, 2]]

    >>> matrix_multiply([[1, 2]], [[3], [4]])
    [[11]]

    >>> matrix_multiply([[1, 2]], [[3, 4]])  # Multiplication is impossible
    Traceback (most recent call last):
        ...
    ValueError: Unable to multiply matrices: wrong dimensions.
    """
    # It is checked whether the matrix sizes coincide for their correct multiplication.
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Unable to multiply matrices: wrong dimensions.")

    # row in matrix1: the rows of the first matrix are searched.
    # If matrix1 = [[1, 2], [3, 4]], then on the first iteration row = [1, 2] and on the second one: row = [3, 4].

    # for col in zip(*matrix2): the columns of the second matrix transformed by zip(*matrix2) function are searched.
    # If matrix2 = [[5, 6], [7, 8]] then zip(*matrix2) will give the columns: col1 = (5, 7) and col2 = (6, 8).

    # At each iteration, row from the first matrix and col from the second matrix are combined
    # into pairs of elements using the zip function.
    # If row = [1, 2] and col = (5, 7), then zip(row, col) will give the pairs: (1, 5) and (2, 7).

    # a * b for a, b in zip(row, col): for each pair of elements (a, b), where a is a row element from the first
    # matrix and b is a column element from the second matrix, multiplication is performed.
    # For the pair (1, 5) the result is 1 * 5 = 5, and for the pair (2, 7) the result is 2 * 7 = 14.

    # Once the products of all row and column elements have been calculated, they are summed.
    # 5 (1 * 5) + 14 (2 * 7) = 19.
    result = [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)]
        for row in matrix1
    ]
    return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Matrix transposition - combines the elements of each row of the matrix into columns,
    effectively ‘flipping’ the matrix.
    :param matrix: matrix.
    :return: matrix.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

    >>> transpose_matrix([[1]])
    [[1]]

    >>> transpose_matrix([[1, 2], [3, 4], [5, 6]])
    [[1, 3, 5], [2, 4, 6]]
    """
    # Converts the zip result into a list of lists (matrix). The final result is converted
    # to a regular list using list(...).
    return list(map(list, zip(*matrix)))

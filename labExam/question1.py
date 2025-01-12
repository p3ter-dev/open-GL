import numpy as np

def find_matrix_shape(matrix):
    if not matrix:
        return (0, 0)
    rows = len(matrix)
    columns = len(matrix[0]) if isinstance(matrix[0], list) else 0
    return (rows, columns)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(find_matrix_shape(matrix))
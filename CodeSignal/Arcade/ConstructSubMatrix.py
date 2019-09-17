"""
Given a matrix (i.e. an array of arrays), find its submatrix obtained by deleting the specified rows and columns.

Example

For

matrix = [[1, 0, 0, 2],
          [0, 5, 0, 1],
          [0, 0, 3, 5]]
rowsToDelete = [1], and columnsToDelete = [0, 2], the output should be

constructSubmatrix(matrix, rowsToDelete, columnsToDelete) = [[0, 2],
                                                            [0,5]]

"""

def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):
    for r in sorted(rowsToDelete, reverse=True):
        matrix.pop(r)
    for c in sorted(columnsToDelete, reverse=True):
        for r in matrix:
            r.pop(c)
    return matrix


matrix = [[1, 0, 0, 2],
          [0, 5, 0, 1],
          [0, 0, 3, 5]]
rowsToDelete = [1]
columnsToDelete = [0, 2]

print(constructSubmatrix(matrix, rowsToDelete, columnsToDelete))

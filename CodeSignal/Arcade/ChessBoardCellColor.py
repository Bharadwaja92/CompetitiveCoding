"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.

For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.


"""

def chessBoardCellColor(cell1, cell2):
    whiteEven = ['A', 'C', 'E', 'G']
    blackEven = ['B', 'D', 'F', 'H']
    c1 = 'W' if (cell1[0] in whiteEven and int(cell1[1]) % 2 == 0) or (cell1[0] in blackEven and int(cell1[1]) % 2 == 1) else 'B'
    c2 = 'W' if (cell2[0] in whiteEven and int(cell2[1]) % 2 == 0) or (cell2[0] in blackEven and int(cell2[1]) % 2 == 1) else 'B'
    return c1 == c2

cell1 = "A1"
cell2 = "C3"

cell1 = 'F2'
cell2 = 'C6'
print(chessBoardCellColor(cell1, cell2))
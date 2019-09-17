"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically
 and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image
 below to see all valid moves for a knight piece that is placed on one of the central squares.

Example

For cell = "a1", the output should be
chessKnight(cell) = 2.

For cell = "c2", the output should be
chessKnight(cell) = 6.
"""


def chessKnight(cell):
    col, row = ord(cell[0])-ord('a')+1, int(cell[1])
    count = 0
    print(col, row)
    if 1 <= col+2 <= 8:
        if 1 <= row+1 <= 8:
            count += 1
        if 1 <= row-1 <= 8:
            count += 1
    if 1 <= col-2 <= 8:
        if 1 <= row+1 <= 8:
            count += 1
        if 1 <= row-1 <= 8:
            count += 1
    if 1 <= row+2 <= 8:
        if 1 <= col+1 <= 8:
            count += 1
        if 1 <= col-1 <= 8:
            count += 1
    if 1 <= row-2 <= 8:
        if 1 <= col+1 <= 8:
            count += 1
        if 1 <= col-1 <= 8:
            count += 1
    return count


cell = "a1"
cell = "c2"
cell = "d4"
print(chessKnight(cell))
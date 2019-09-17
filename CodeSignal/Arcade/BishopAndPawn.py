"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can
capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.
"""
import math

def bishopAndPawn(bishop, pawn):
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    bcol, brow, pcol, prow = cols.index(bishop[0]), int(bishop[1]), cols.index(pawn[0]), int(pawn[1])
    print(bcol, brow)
    print(pcol, prow)
    return math.fabs(pcol - bcol) == math.fabs(prow - brow)


bishop = "h1"
pawn = "g2"
print(bishopAndPawn(bishop, pawn)) # = false.

# Pawn Brotherhood

# Chess is a two-player strategy game played on a checkered game board laid out in eight rows
# (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h)
# of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number
# (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture
# an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square.
# For white pawns the front squares are squares with greater row number than the square they currently occupy.

# A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
# With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on
# that square. We have several white pawns on the chess board and only white pawns. You should design your
# code to find how many pawns are safe.

# pawns

# You are given a set of square coordinates where we have placed white pawns. You should count how many
# pawns are safe.

# Input: Placed pawns coordinates as a set of strings.

# Output: The number of safe pawns as a integer.

# Example:

# assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
# assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1
# 1
# 2
# How it is used: For a game AI one of the important tasks is the ability to estimate game state. This concept will show how you can do this on the simple chess figures positions.

# Precondition:
# 0 < pawns ≤ 8

################################################ SOLUTION#####################################################
import numpy as np


def safe_pawns(pawns: set) -> int:
    safe_namb = 0
    for pawn in pawns:
        param_1 = chr(ord(pawn[0])-1)+str(int(pawn[1])-1)
        param_2 = chr(ord(pawn[0])+1)+str(int(pawn[1])-1)
        safe_namb += param_1 in pawns or param_2 in pawns
    return safe_namb


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

################################################### OR########################################################


def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)


def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])


################################################### OR########################################################
o, safe_pawns = lambda l, d=- \
    1: chr(ord(l)+d), lambda P: sum(bool({o(f)+o(r), o(f, 1)+o(r)} & P)for f, r in P)
################################################### OR########################################################


def safe_pawns(pawns):
    return sum((any(chr(ord(l) + i) + str(int(d) - 1) in pawns for i in [-1, 1])) for l, d in pawns)

################################################### OR########################################################


def safe_pawns(pawns):
    dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    tablero = np.zeros((8, 8))

    for coord in pawns:
        i = 8 - int(coord[1])
        j = dict[coord[0]]
        tablero[i, j] = 1

    f, c = tablero.shape
    cont = 0
    for i in range(f):
        for j in range(c):
            if tablero[i, j] == 1:
                if tablero[i + 1:i+2, j-1:j] == 1 or tablero[i + 1:i + 2, j+1:j+2] == 1:

                    cont += 1
    return cont

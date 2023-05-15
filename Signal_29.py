"""
Given two cells on the standard chess board, determine whether they have the same color or not.
Example
    For cell1 = "A1" and cell2 = "C3", the output should be
    solution(cell1, cell2) = true.
    For cell1 = "A1" and cell2 = "H3", the output should be
    solution(cell1, cell2) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [memory limit] 1 GB
    [input] string cell1
    Guaranteed constraints:
    cell1.length = 2,
    'A' ≤ cell1[0] ≤ 'H',
    1 ≤ cell1[1] ≤ 8.
    [input] string cell2
    Guaranteed constraints:
    cell2.length = 2,
    'A' ≤ cell2[0] ≤ 'H',
    1 ≤ cell2[1] ≤ 8.
    [output] boolean
    true if both cells have the same color, false otherwise.
"""


# version_1
def solution(cell1, cell2):
    odd = "ACEG"
    even = "BDFH"
    if (cell1[0] in odd) and (int(cell1[1]) % 2) and (cell2[0] in odd) and (int(cell2[1]) % 2):
        return True
    if (cell1[0] in odd) and (int(cell1[1]) % 2) and (cell2[0] in even) and (int(cell2[1]) % 2 == 0):
        return True
    if (cell1[0] in even) and (int(cell1[1]) % 2 == 0) and (cell2[0] in even) and (int(cell2[1]) % 2 == 0):
        return True
    if (cell1[0] in even) and (int(cell1[1]) % 2 == 0) and (cell2[0] in odd) and (int(cell2[1]) % 2):
        return True
    if (cell1[0] in odd) and (int(cell1[1]) % 2 == 0) and (cell2[0] in odd) and (int(cell2[1]) % 2 == 0):
        return True
    if (cell1[0] in odd) and (int(cell1[1]) % 2 == 0) and (cell2[0] in even) and (int(cell2[1]) % 2):
        return True
    if (cell1[0] in even) and (int(cell1[1]) % 2) and (cell2[0] in even) and (int(cell2[1]) % 2):
        return True
    if (cell1[0] in even) and (int(cell1[1]) % 2) and (cell2[0] in odd) and (int(cell2[1]) % 2 == 0):
        return True
    return False
print(solution("A1", "H3"))



# version_2
def solution(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0
print(solution("A1", "H3"))


# version_3
def solution(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1])) % 2 == (ord(cell2[0]) + int(cell2[1])) % 2
print(solution("A1", "H3"))


# version_4
def solution(cell1, cell2):
    white = {"A2", "A4", "A6", "A8", "B1", "B3", "B5", "B7", "C2", "C4", "C6", "C8", "D1", "D3", "D5", "D7", "E2", "E4", "E6", "E8", "F1", "F3", "F5", "F7", "G2", "G4", "G6", "G8", "H1", "H3", "H5", "H7"}
    if cell1 in white and cell2 not in white or cell1 not in white and cell2 in white:
        return False
    return True
print(solution("A1", "H3"))

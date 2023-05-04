"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine 
have a number in it that indicates the total number of mines in the neighboring cells. 
Starting off with some arrangement of mines we want to create a Minesweeper game setup.
Example
For
matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be
solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]

    A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains 
    a mine, false otherwise.

    Guaranteed constraints:
    2 ≤ matrix.length ≤ 100,
    2 ≤ matrix[0].length ≤ 100.

    [output] array.array.integer

    Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number 
    of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
"""



def solution(matrix):
    lst = [[0] * len(matrix[0])] * len(matrix)
    
    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if j:
                lst[i][j + 1] += 1
                lst[i + 1][j] += 1
                

    return lst

print(solution([[True, False, False],
          [False, True, False],
          [False, False, False]]))

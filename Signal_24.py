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
    rows = len(matrix)
    cols = len(matrix[0])
        
    conv = lambda i , j : 1 if 0 <= i < rows and 0 <= j < cols and matrix[i][j] else 0
    
    nbs = lambda i, j : sum(conv(ii, jj) for ii in range(i-1, i+2) for jj in range(j-1, j+2)) - conv(i, j)
    
    return [[nbs(i, j) for j in range(cols)]for i in range(rows)]

print(solution([[True, False, False],
                [False, True, False],
                [False, False, False]]))

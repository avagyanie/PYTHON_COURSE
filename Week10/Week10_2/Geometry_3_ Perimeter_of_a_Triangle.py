"""
Write a function that takes the coordinates of three points in the form of a 2d array and returns the 
perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
Examples
perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08
perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41
perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
Notes
    The given points always create a triangle.
    The numbers in the argument array can be positive or negative.
    Output should have 2 decimal places
    This challenge is easier than it looks.
"""



def perimeter(lst):
    x1, y1 = lst[0]
    x2, y2 = lst[1]
    x3, y3 = lst[2]

    side1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    side2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1/2)
    side3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1/2)

    perimeter = side1 + side2 + side3

    return round(perimeter, 2)

print(perimeter([[-10, -10], [10, 10 ], [-10, 10]]))
